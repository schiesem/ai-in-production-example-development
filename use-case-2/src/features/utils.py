def import_check():
    print(f"Import form {__name__} is working")

def ff_dropper(data_frame):
    """
    A function that eleminates rows of a feature frame, if a condition is not fulfilled.

    Parameters
    ----------
    data_frame : data_frame
        


    Results:
    --------
    label : int 
        The drive belt frequency of the file.
    """
    for index, row in data_frame.iterrows():
        try:
            temp_df = row["DEVICE_DATA_FRAME"]
            
            # converting time stamps
            temp_df["EC_SYSTEM_TIMESTAMP"] = pd.to_datetime(temp_df["EC_SYSTEM_TIMESTAMP"], unit = "ns")

            # converting length to active positioning phase
            temp_df = temp_df[(temp_df['Aktueller Wert / DigitalausgÃ¤nge GrundgerÃ¤t ']==1)]

            # resampling the data
            RESAMPLETIME = '0.05s'
            temp_df = temp_df.resample(RESAMPLETIME, on="EC_SYSTEM_TIMESTAMP").mean()
            # resample element number
            MIN_ELEMENTS = 0
            MAX_ELEMENTS = 100

            temp_df = temp_df[MIN_ELEMENTS:MAX_ELEMENTS]

            data_frame.iloc[index]["DEVICE_DATA_FRAME"] = pd.DataFrame(temp_df)
        except:
            print(f"Error with data row {index}, name: {row.FILE_NAME}")
            data_frame.drop(index)
            print(f"DATA row {index} deleted from dataset")
            

print(f"Import form {__name__} is working")

if __name__ == "__main__":
    import os, sys
    import warnings
    import pandas as pd
    from scipy.interpolate import interp1d


    # set relativ import of own package data
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'data'))

        # Suppress FutureWarning messages
    warnings.simplefilter(action='ignore', category=FutureWarning)

    
    DATA_DIR= "D:\\work-hsu\\08_code_programms\\ai-in-production-example-development\\use-case-2\\data\processed\\df_feature_frame.pickle"

    # load data frame
    data_frame = load_file(DATA_DIR)

    for index, row in data_frame.iterrows():
        try:
            temp_df = row["DEVICE_DATA_FRAME"]

            # converting time stamps
            temp_df["EC_SYSTEM_TIMESTAMP"] = pd.to_datetime(temp_df["EC_SYSTEM_TIMESTAMP"], unit = "ns")

            # converting length to active positioning phase
            temp_df = temp_df[(temp_df['Aktueller Wert / DigitalausgÃ¤nge GrundgerÃ¤t ']==1)]

            # resampling the data
            RESAMPLETIME = '0.05s'
            temp_df = temp_df.resample(RESAMPLETIME, on="EC_SYSTEM_TIMESTAMP").mean()
            # resample element number
            MIN_ELEMENTS = 0
            MAX_ELEMENTS = 100

            temp_df = temp_df[MIN_ELEMENTS:MAX_ELEMENTS]

            data_frame.iloc[index]["DEVICE_DATA_FRAME"] = pd.DataFrame(temp_df)
        except:

            print(f"Error with data row {index}, name: {row.FILE_NAME}")
            data_frame.drop(index)
            print(f"DATA row {index} deleted from dataset")
            
    data_frame.head()
    print("end")