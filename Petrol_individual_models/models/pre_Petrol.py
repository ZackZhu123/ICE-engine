import os
import pandas as pd
import tensorflow as tf
# from keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Lambda
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import numpy as np
import matplotlib.pyplot as plt

ENGINE_TYPE = 'Petrol'
DATA_SET_TYPE = 'Original Datafiles'
DATA_FOLDER = 'ICE data'

def noise_layer(x):
    import tensorflow as tf
    return x + tf.random.normal(shape=tf.shape(x), mean=0.0, stddev=0.5, dtype=tf.float32)


def get_data_file_name():
    """get_data_file_name returns the data file name that we wish to read."""
    file_name = ENGINE_TYPE + '_clean_master' + '.csv'
    return os.path.join(DATA_FOLDER, DATA_SET_TYPE, file_name)


def read_data():
    """read_data reads the data file and returns the input/output respectively"""
    file_name = get_data_file_name()

    input_col_list = ['Throttle Position (%)', 'Engine Speed (rpm)']
    input_data = pd.read_csv(file_name, usecols=input_col_list)
    # output_col_list = ['Exhaust Temp. (C)', 'Cal Water Out Temp. (C)','Cal Exhaust Out Temp. (C)']
    output_col_list = ['Oil Out Temp. (C)', 'Exhaust Temp. (C)', 'Dyno Out Temp. (C)', 'Oil In Temp. (C)', 'Cal Water Out Temp. (C)',
     'Cal Exhaust Out Temp. (C)', ]
    # output_col_list = ['Oil Out Temp. (C)']
    output_data = pd.read_csv(file_name, usecols=output_col_list)
    return input_data, output_data


def get_model():
    """get_model returns the DNN model"""
    model = Sequential()
    model.add(Dense(30, input_dim=2, activation='relu'))
    # model.add(Dense(30, activation='relu'))
    # model.add(Dense(30, activation='relu'))
    # model.add(Dense(30, activation='relu'))
    #model.add(tf.keras.layers.BatchNormalization())
    # model.add(Dense(128, activation='relu'))
    # model.add(tf.keras.layers.BatchNormalization())
    # model.add(Dense(128, activation='relu'))
    # model.add(tf.keras.layers.BatchNormalization())
    # model.add(Dense(128, activation='relu'))
    # model.add(tf.keras.layers.BatchNormalization())
    # model.add(Dense(128, activation='relu'))
    # model.add(tf.keras.layers.BatchNormalization())
    # model.add(Dense(128))
    # model.add(tf.keras.layers.AlphaDropout(rate=0.1))
    model.add(Dense(6))
    model.compile(loss=['mse'], optimizer=tf.keras.optimizers.Adam(0.0001), metrics=['mae'])
    return model



def train_model(model, input_data, output_data):
    """train_model trains the model"""
    history = model.fit(
            input_data,
            output_data,
            epochs=4000,
            verbose=1,
            validation_split=0.2,)
    return history

def save_mode(model, file_name):
    """save_model saves the model"""
    model.save(file_name)


def eval_model(model, input_data, output_data):
    """eval_model evaluates the model"""
    return model.evaluate(input_data, output_data)


def main():
    import time
    # Read data
    input_data, output_data = read_data()

    print(input_data[:1].shape)
    # Build model
    model = get_model()
    model_summary = []
    model.summary(print_fn=lambda x: model_summary.append(x))
    pretty_print('Model Summary', '\n'.join(model_summary))
    start=time.time()
    # Train model
    history = train_model(model, input_data, output_data)
    print(time.time() - start)
    plt.plot(history.history['loss'], label='train')
    plt.plot(history.history['val_loss'], label='validation')
    plt.legend()
    # plt.savefig('plot/train_plot_' + NAME + '4.png')
    plt.show()

    # Evaluate model
    test_result = eval_model(model, input_data, output_data)
    print(input_data,model.predict(input_data))
    temp = pd.DataFrame(model.predict(input_data))
    temp.to_csv("./pre_level_model/Petrol_hidden_var.csv", index=False, header = ['Oil Out Temp. (C)', 'Exhaust Temp. (C)', 'Dyno Out Temp. (C)', 'Oil In Temp. (C)', 'Cal Water Out Temp. (C)',
     'Cal Exhaust Out Temp. (C)', ])
    pretty_print('Test MSE', test_result)
    # Save model
    model_name = 'Petrol_model' + '.h5'
    save_mode(model, "./pre_level_model/" + model_name)


def pretty_print(secion_name, content):
    """pretty_print wraps the print function so that we will have different sections"""
    print('\n##################################### {}\n'.format(secion_name))
    print(content)
    print('\n##################################### {}\n'.format(secion_name))


if __name__ == "__main__":
    main()
