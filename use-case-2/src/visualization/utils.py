import matplotlib.pyplot as plt
import numpy as np
from copy import copy

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=SMALL_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=MEDIUM_SIZE)  # fontsize of the figure title

plot_arguments = {
        "title":"default_title", 
        "x_label":"default_x_label", 
        "y_label":"default_y_label", 
        "autoscale": True,
        "x_limits":None,
        "y_limits":None,
        "alpha":1,
        "color":"b",
        "linewidth":1.5,
        "plot_custom_legend" : False,
        "custom_label" : "default_label"
        }

def custom_plot(ax, x_values, y_values, **kwargs):
    from matplotlib.lines import Line2D
    arguments = copy(plot_arguments)
    arguments.update(kwargs)

    ax.set_title(arguments["title"])
    ax.set_ylabel(arguments["y_label"])
    ax.set_xlabel(arguments["x_label"])

    if arguments["autoscale"] == True:
        ax.autoscale_view()

    if arguments["autoscale"] == False:
        ax.set_xlim([arguments["x_limits"][0], arguments["x_limits"][1]])
        ax.set_ylim([arguments["y_limits"][0], arguments["y_limits"][1]])

    if arguments["plot_custom_legend"] == True:
        custom_handle = Line2D([0],[0],color=arguments["color"], lw=4, label='line')
        # create new label entry
        new_entries = {arguments["custom_label"]:custom_handle}
        # get current labels of ax
        legend = ax.get_legend()
        # if no legend is existing before
        if legend == None:
            ax.legend(handles = new_entries.values(), labels = new_entries.keys())
        # if an legend already exists
        else: 
            # get the current handles and texts of the axis object
            old_handles =  legend.legendHandles
            old_labels = [element.get_text() for element in legend.texts]
            # create label dict of current elements
            label_dict = dict(zip(old_labels, old_handles))
            # append new labels to existing in merging dict
            merged_dict = {**new_entries, **label_dict} #priority from right to left
            # plot merged axis
            ax.legend(handles = merged_dict.values(), labels = merged_dict.keys())

    #plot the new axis element
    ax.plot(x_values, y_values, color = arguments["color"], alpha = arguments["alpha"], linewidth = arguments["linewidth"])

def custom_fig_solo(x_values, y_values, **kwargs):
    """
    A function that takes x-values, y-values and a dictionary of parameters.

    Parameters
    ----------
    x_values : numpy.array
        Values to plot on the x-axis.

    y_values: numpy.array
        Values to plot on the y-axis.

    **kwargs : dictionary
        title : string
        x_label : string
        y_label : string
        autoscale : bool

    Results:
    --------
    fig : matplotlib-object
        A plottable python object. 
    --------
    """
    arguments = copy(plot_arguments)
    arguments.update(kwargs)
    
    fig, ax = plt.subplots(1,1, figsize=(8,5))
    
    ax.set_title(arguments["title"])
    ax.set_ylabel(arguments["y_label"])
    ax.set_xlabel(arguments["x_label"])

    if plot_arguments["autoscale"] == True:
        ax.autoscale_view()

    ax.plot(x_values, y_values)

    return(fig)

def custom_fig_multi(x_value_list, y_value_list, label_list, **kwargs):
    """
    A function that plots more than one line into a figure.

    Parameters
    ----------
    x_value_list : numpy.array of numpy.arrays
        An array with numpy arrays of x_value data to be polotted.

    y_values: numpy.array
        An array with numpy arrays of y_value data to be polotted.

    label_list: list
        A list with labes of the plots.

    **kwargs : dictionary
        title : string
        x_label : string
        y_label : string
        alpha : int
        autoscale : bool

    Results:
    --------
    fig : matplotlib-object
        A plottable python object. 
    --------
    """
    from copy import copy
    arguments = copy(plot_arguments)
    arguments.update(kwargs)

    fig, ax = plt.subplots(1,1, figsize=(8,5))

    ax.set_title(arguments["title"])
    ax.set_ylabel(arguments["y_label"])
    ax.set_xlabel(arguments["x_label"])
    if arguments["autoscale"] == True:
        ax.autoscale_view()

    # create a dictionary with unique colors for unique items
    uniqe_labels = list(set(label_list))
    cmap = plt.cm.get_cmap("gist_rainbow", len(uniqe_labels)+1)
    color_dict = {}
    for color_number, label in enumerate(uniqe_labels):
        color_dict[label] = color_number
    print(color_dict)
    
    # create the plot with respect to the color dict
    for x_values, y_values, label in zip(x_value_list, y_value_list, label_list):
        #create the plot
        ax.plot(x_values, y_values, color=cmap(color_dict[label]), alpha=arguments["alpha"])
    
    return(fig)

def save_fig(fig, save_path, fig_name, file_ending="png", dpi="600", overwrite = True):
    from os.path import join
    file_path = join(save_path,f"{fig_name}.{file_ending}")

    fig.savefig(file_path, dpi=600,  bbox_inches="tight")

def cm2in(value):
    return value/2.54

print(f"Import form {__name__} is working")

if __name__ == "__main__":
    import sys, os

    from tqdm import tqdm
    import matplotlib.pyplot as plt
    import numpy as np

    # set relativ import of own package data
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'data'))

    DATA_DIR = "D:\\work-hsu\\08_code_programms\\ai-in-production-example-development\\use-case-2\\data\\processed\\df_data.pickle"
    FIG_DIR = "D:\\work-hsu\\08_code_programms\\ai-in-production-example-development\\use-case-2\\reports\\figures"
 #------------------------- visualisations -------------------------#
    
    # load feature frame
    feature_frame = dt.load_file(DATA_DIR)
    print("Start Printing")
    
    # selecting the upwards data with mass
    select_data = feature_frame[(feature_frame[dt.MOVING_LABEL]=="up") & (feature_frame[dt.WEIGHT_LABEL]== 1710)]

    # begin the first printing figure
    fig1, ax1 = plt.subplots(1,1, figsize=(8,5))
    fig2, (ax2, ax3) = plt.subplots(1,2, figsize=(8,5))
    for index, row in tqdm(select_data.iterrows(), desc="Creating Plot 1"):
        column_names = row[dt.DEVICE_DATA_FRAME].columns
        x_col = column_names[0]
        y_col = column_names[5]
        y_values = row[dt.DEVICE_DATA_FRAME][y_col]
        x_values = row[dt.DEVICE_DATA_FRAME][x_col].subtract(row[dt.DEVICE_DATA_FRAME][x_col].iloc[0]).divide(1e9)
        # set the printing color
        if row[dt.FREQUENCY_LABEL] == 60:
            temp_color = "r"
            temp_custom_label = "60Hz (bad)"
            custom_plot(ax2, x_values, y_values, alpha = 0.2, color = temp_color, linewidth = 0.25, 
                           autoscale = False, x_limits=(0, 10), y_limits=(-0.5, 2), 
                           title="Technikum BBG \n 1710kg (open)", x_label= x_col, y_label=y_col,
                           plot_custom_legend = True, custom_label = temp_custom_label)
        if row[dt.FREQUENCY_LABEL] == 69:
            temp_color = "g"
            temp_custom_label = "69Hz (good)"
            custom_plot(ax3, x_values, y_values, alpha = 0.2, color = temp_color, linewidth = 0.25, 
                           autoscale = False, x_limits=(0, 10), y_limits=(-0.5, 2),
                           title = "Technikum BBG \n 1710kg (open)", x_label=x_col, y_label=y_col,
                           plot_custom_legend = True, custom_label = temp_custom_label)

        custom_plot(ax1, x_values, y_values, alpha = 0.2, color = temp_color, linewidth = 0.25,
                       title = "Technikum BBG \n 1710kg (open)", x_label=x_col, y_label=y_col,
                       plot_custom_legend=True, custom_label=temp_custom_label)
    
    save_fig(fig1, FIG_DIR, "test_file", overwrite=True)
    save_fig(fig2, FIG_DIR, "test_file2", overwrite=True)

    fig1.show()
    fig2.show()


    print("END")