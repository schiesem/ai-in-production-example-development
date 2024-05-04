# programm reads the raw data paths 
# loads a raw data json-file
# transforms the data into an array
# saving the data as a pickle

import glob
import os
# from os.path import join as join 
from tqdm import tqdm

# file items 
FILE_NAME = "FILE_NAME"
FILE_PATH = "FILE_PATH"
FILE_TYPE = "FILE_TYPE"
FILE_FOLDER = "FILE_FOLDER"
FILE_DEVICES = "FILE_DEVICES"

# device items
SAMPLE_TIME = "SAMPLE_TIME"
CHANNEL_DESCRIPTIONS = "CHANNEL_DESCRIPTIONS"
SAMPLES = "SAMPLES"

# sample items
EC_SYSTEM_TIMESTAMP = "EC_SYSTEM_TIMESTAMP"
CHANNEL_DATA = "CHANNEL_DATA"
SCALED_CHANNEL_DATA = "SCALED_CHANNEL_DATA"

# setable lables
WEIGHT_LABEL = "WEIGHT_LABEL"
FREQUENCY_LABEL = "FREQUENCY_LABEL"
MOVING_LABEL = "MOVING_LABEL"

DEVICE = "DEVICE"
DEVICE_DATA_FRAME = "DEVICE_DATA_FRAME"

def parse_files(parse_dir, file_ending="json", recursive = False):
    """
    A function to parse a directory and return a list of files with a defined ending

    Parameters
    ----------
    parse_dir : realstring (r"")
        The directory that should be parsed

    file_ending : string (json, pickle)
        The file ending parsed for

    recursive : bool
        The sub directories got browsed too.
    
    Results:
    --------
    file_list : list 
        a list of files in parse_dir with the file_ending
    """
    if recursive == False:
        file_ending = f"*.{file_ending}"
        parse_dir = os.path.join(os.path.abspath(parse_dir), file_ending)
    
    if recursive == True:
        file_ending = os.path.join("**",f"*.{file_ending}")
        parse_dir = os.path.join(os.path.abspath(parse_dir), file_ending)

    file_list = glob.glob(parse_dir)
    print(f"Name of File Path: {parse_dir}")
    print("Number of Files Parsed: {}".format(len(file_list)))
    return(file_list)

def load_file(file_path : str):
    """
    A function that loads data from a given path. 

    Parameters
    ----------
    file_path : string
        The path to a concrete file that should be loaded

    Results:
    --------
    json_data : python_object
        An structured object with the json data

    pickle_data : python_object 
        An structured object with the json data
    """
    match file_path.split(".")[-1]:
        case "json":
            import json
            with open(file_path) as json_file:
                json_data = json.load(json_file)
                return(json_data)
        case "pickle":
            import pickle
            with open(file_path, "rb") as pickle_file:
                pickle_data = pickle.load(pickle_file)
                return(pickle_data)
            
def save_file(data, file_path, file_name : str, type : str):
    """
    A function that saves an python object to a defined type in a defined path.

    Parameters
    ----------
    data : python_object
        The data that should be saved

    file_path : string
        The path in that the data should be saved

    file_name : string
        The file name for the new file.

    type : string
        The data-type of the new file
    
    Results:
        A new file saved at file_path
    --------
    """
    save_path = os.path.join(file_path, file_name)
    match type:
        case "pickle":
            import pickle
            with open(f"{save_path}.pickle", "wb") as pickle_file:
                pickle.dump(data, pickle_file)
        case"json":
            import json
            with open(f'{save_path}.json', 'w') as json_file:
                json.dump(data, json_file, indent=3)

def create_data_dict(file_list : list):
    """
    A function that loads data and sorts it into a dictionary. 
    The loaded data needs to be recorded with the SmartDataCollector from SEW. 
    The strucure of the data dictionary is describted in the README.md

    Parameters
    ----------
    file_list : list
        a list of absolut paths to data-files
    
    Results:
    --------
    data_dict : returns a dictionary with the data
    """
    
    data_dict = {}

    for file_path in file_list:
        file_data = load_file(file_path)

        file_dict = {}
        file_dict[FILE_NAME] = file_path.split("\\")[-1].split(".")[0]
        file_dict[FILE_PATH] = file_path
        file_dict[FILE_TYPE] = file_path.split(".")[-1]
        file_dict[FILE_FOLDER] = file_path.split("\\")[-2]
        file_dict[FILE_DEVICES] = None
        # create a new file-entry in data-dict
        data_dict[file_dict[FILE_NAME]] = file_dict
        # dictionary with all devices
        file_devices_dict = {}
        file_dict[FILE_DEVICES] = file_devices_dict

        for device in list(file_data.get("devices").keys()):
            # new dictionary for information about device
            device_dict = {}
            device_dict[SAMPLE_TIME] = file_data.get("devices")[device].get("data").get("sampleTime")
            device_dict[CHANNEL_DESCRIPTIONS] = file_data.get("devices")[device].get("data").get("channelDescriptions")
            device_dict[SAMPLES] = []
            
            for sample_element in file_data.get("devices")[device].get("data").get("samples"):
                # new dictionary for sample data of one device
                sample_dict = {}
                sample_dict[EC_SYSTEM_TIMESTAMP] = sample_element.get("ecSystemTimestamp")
                sample_dict[CHANNEL_DATA] = sample_element.get("channelData")
                sample_dict[SCALED_CHANNEL_DATA] = sample_element.get("scaledChannelData")
                device_dict[SAMPLES].append(sample_dict)

        # creates a new device in devices
        file_devices_dict[device] = device_dict

    return(data_dict)

def create_data_frame(device_data_dict):
    """
    A function to parse a data_dictionary from a "create_data_dict" function element.

    Parameters
    ----------
    device_data_dict : dictionary
        A dictionary that contains the data of one file.
        For example: data_dict[file_name] or data_dict.values()
    
    Results:
    --------
    device_data_frame : pandas.dataFrame()
        A data_frame with the samples data of the file.
    """
    import pandas as pd
    from copy import copy

    # creating the column names
    col_names = [item.get("name") for item in device_data_dict[CHANNEL_DESCRIPTIONS]]
    col_names.insert(0,EC_SYSTEM_TIMESTAMP)
    # creating the data_frame
    device_data_frame = pd.DataFrame(columns=col_names)
    for data in device_data_dict[SAMPLES]:
        data_list = copy(data[SCALED_CHANNEL_DATA])
        time_stamp = data[EC_SYSTEM_TIMESTAMP]
        data_list.insert(0, time_stamp)
        temp_data_row = pd.DataFrame([data_list], columns=col_names)
        # wrtining into the dataframe
        device_data_frame = pd.concat([device_data_frame, temp_data_row], axis=0, copy=False)
        device_data_frame.reset_index(drop=True, inplace=True)
    return(device_data_frame)

def create_feature_frame(data_dict):
    """
    Takes a data dictionary and converts it into a pandas Data Frame that can be used for Training and Plotting

    Parameters
    ----------
    data_dict : dictionary 
        The path where the folder should be created
    
    Results:
    --------
    feature_frame : pd.DataFrame

    |file_name|file_path|frequency_label|weight_label|moving_label|device|sample_time|   device_data_frame   |
    |---------|---------|---------------|------------|------------|------|-----------|-----------------------|
    |   str   |   str   |       int     |     int    |     str    | str  |     int   |  list[pd.DataFrame()] |
    
    """
    import pandas as pd

    file_elements = [FILE_NAME, FILE_PATH, FREQUENCY_LABEL, WEIGHT_LABEL, MOVING_LABEL]

    col_names = [FILE_NAME, FILE_PATH, FREQUENCY_LABEL, WEIGHT_LABEL, MOVING_LABEL, DEVICE, SAMPLE_TIME, DEVICE_DATA_FRAME]

    feature_frame = pd.DataFrame(columns=col_names)
    
    for file_name in tqdm(data_dict, desc= "Feature Frame"):
        temp_file_row = {}
        for file_item in file_elements:
            # set the items of file_elements
            temp_file_row.update({file_item:data_dict[file_name].get(file_item)})
            # get device data
        for device_name, device_values in data_dict[file_name][FILE_DEVICES].items():
            temp_file_row.update({DEVICE:device_name})
            temp_file_row.update({SAMPLE_TIME:device_values[SAMPLE_TIME]})
            
            # get device data frame
            df = create_data_frame(device_values)
            temp_file_row.update({DEVICE_DATA_FRAME:(df)})
            temp_data_row = pd.DataFrame([temp_file_row])
            # append data frame
            feature_frame = pd.concat([feature_frame, temp_data_row], axis = 0, copy=False)

    feature_frame.reset_index(drop=True, inplace=True)
    return(feature_frame)

def create_dict_item(data_dict, new_item_key, new_item_value):
    """
    A function that appends a item with a label into an dictionary.

    Parameters
    ----------
    data_dict : dict
        The dictionary where the label should be appended at.
    
    new_item_key : str
        The item Key for identifying the new entry.
    new_item_value : all
        The Value of the new key entry.
    Results:
    --------
    """
    #function that thats a label at the file level
    data_dict.update({new_item_key:new_item_value})

def search_dict_item(obj, key):
    """
    A function that searches a dictionary for a given key

    Parameters
    ----------
    obj : dictionary
        The dictionary through that the function browses.

    key : str
        The name of the key that is searched

    Results:
    --------
    item : str
        The founded item.
    """
    if key in obj: return obj[key]
    for k, v in obj.items():
        if isinstance(v,dict):
            item = search_dict_item(v, key)
            if item is not None:
                return item 

#function that appends a movement_label to the dataframe
def get_moving_label(data_frame, pos_col_name):
    """
    A function that determines the moving direction of a data_frame.

    Parameters
    ----------
    data_frame : pandas.dataFrame
        The dataFrame where the positional Data is.

    pos_col_name: str
        The name of the column with the positional data

    Results:
    --------
    label : str ("up" or "down")
        The label of the file.
    """
    # input is a data-frame
    # output is a label of movement
    import numpy as np
    is_position = data_frame[pos_col_name]
    mean_gradient = np.diff(is_position).mean()
    # if the mean_gradient is positive, the tool moves upwards
    if mean_gradient > 0:
        return("up")
    # if the mean_gradient is negavtive, the tool moves upwards
    if mean_gradient < 0:
        return("down")
    
def get_frequency_label(file_folder_name):
    """
    A function that determines the frequency-label of a folder_name.

    Parameters
    ----------
    file_folder_name : str
        The folder in wich the Data is grouped into.


    Results:
    --------
    label : int 
        The drive belt frequency of the file.
    """
    #input a data_dict
    name_parts = file_folder_name.split("_")
    frequency = int(name_parts[0].split("H")[0])
    return(frequency)

def get_weight_label(folder_name):
    """
    A function that determines the weight-label of a folder_name.

    Parameters
    ----------
    file_folder_name : str
        The folder in wich the Data is grouped into.


    Results:
    --------
    label : int 
        The drive belt frequency of the file.
    """
    name_parts = folder_name.split("_")
    weight = int(name_parts[-1].split("Z")[-1].split("k")[0])
    return(weight)

print(f"Import form {__name__} is working")

if __name__ == "__main__":
    print("Main Running")