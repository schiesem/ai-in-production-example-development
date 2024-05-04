print(f"Import form {__name__} is working")

import tensorflow as tf
from keras import Sequential, layers, optimizers, Input

def create_model():
    """
    A Function that takes config parameters for a NN and returns a model

    Parameters
    ----------
    file_folder_name : str
        The folder in wich the Data is grouped into.


    Results:
    --------
    model : keras.Sequential 
        The compiled model to be trained.
    """

    model = Sequential(name="my_sequential")
    model.add(layers.Dense(100, input_shape=(100,), activation='relu'))
    model.add(layers.Dense(10, activation="relu"))
    model.add(layers.Dense(1, activation="sigmoid"))
    
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    model.summary()

    return model

def train_model(model, X, y, X_test, y_test, epochs, batch_size):
    import matplotlib.pyplot as plt

    # train the parameters
    history = model.fit(X, y, epochs=epochs, batch_size = batch_size, verbose=1)

    error, accuracy = model.evaluate(X_test, y_test,  verbose=1)
    print('Accuracy: %.2f' % (accuracy*100))

    return history

def save_model(model, file_path, model_name : str):
    import os 
    import pickle
    save_path = os.path.join(file_path, model_name)
    with open(f"{save_path}.pickle", "wb") as pickle_file:
        pickle.dump(model, pickle_file)
    
    print(f"model saved at path:{save_path}")

def load_model(file_path):
    import os
    import pickle
    with open(file_path, "rb") as pickle_file:
        pickle_data = pickle.load(pickle_file)
        print(f"model loaded from path:{file_path}")
        return(pickle_data)

if __name__ == "__main__":
    import sys
    import os
    sys.path.append("D:\\work-hsu\\08_code_programms\\ai-in-production-example-development\\use-case-2") # go to parent dir

    import numpy as np
    from src.data.utils import load_file, MOVING_LABEL, WEIGHT_LABEL

    FEATURE_FILE_NAME = "feature_frame"
    FEATURE_PATH= f"D:\\work-hsu\\08_code_programms\\ai-in-production-example-development\\use-case-2\\data\processed\\{FEATURE_FILE_NAME}.pickle"

    data = load_file(FEATURE_PATH)

    #upwards data witch 1.71t
    select_data = data[(data[MOVING_LABEL]=="up") & (data[WEIGHT_LABEL]== 1710)]
    select_data.reset_index(inplace=True)

    #row1_data = select_data["DEVICE_DATA_FRAME"].iloc[0]
    #row1_names = select_data["DEVICE_DATA_FRAME"].iloc[0].columns
    #x_vec = np.array(select_data["DEVICE_DATA_FRAME"].iloc[0][NAME], dtype=float)

    VALUE_NAME = "Schleppfehler in Anwendereinheiten / Regelverfahren Prozesswerte"
    AXIS_0 = len(select_data)
    AXIS_1 = len(select_data["DEVICE_DATA_FRAME"].iloc[0][VALUE_NAME])
    
    X = np.zeros((AXIS_0,AXIS_1))
    Y = np.zeros(AXIS_0)

    for index, row in select_data.iterrows():
        X[index] = np.array(row["DEVICE_DATA_FRAME"][VALUE_NAME], dtype=float)

        label = np.array(row["FREQUENCY_LABEL"], dtype=int)
        if label == 60:
             # good
             Y[index] = 1
        elif label == 69:
             # bad
             Y[index] = 0
        else:
            print("Label Error")

    #model creation
    model = create_model()

    # model training
    history = train_model(model, X, Y, epochs=25 , batch_size=5)

    #history plots
    print("Accuracy: ")
    print(history.history["accuracy"])
    print("Loss:")
    print(history.history["loss"])

    #prediction
    print(f"Predictions: {model.predict(X)}")

    print("END")