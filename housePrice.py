import tensorflow as tf 
from tensorflow.python import keras
from tensorflow.python.keras import layers
import numpy as np
import matplotlib.pyplot as plt 

from keras.src.datasets import boston_housing
# from keras import layers

(train_data, train_targets), (test_data, test_targets) = (boston_housing.load_data())
# print(train_data[0])
mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data/=std

test_data -=mean
test_data /=std

def build_model():
    model = keras.Sequential([
        layers.Dense(64, activation="relu"),
        layers.Dense(64, activation="relu"),
        layers.Dense(1)
    ])
    model.compile(optimizer ="rmsprop",
                  loss= "mse",
                  metrics = "mae")
    
    return model

k = 4
numValSamples =len(train_data)//k
numEpochs = 100
allScores =[]
for i in range(k):
    print(f"Processing fold #{i}")
    valData = train_data[i* numValSamples: (i+1)* numValSamples]
    valTargets = train_targets[i* numValSamples: (i+1)* numValSamples]
    partialTrainData = np.concatenate([train_data[:i*numValSamples], train_data[(i+1)* numValSamples:]], axis=0)

    partialTrainTargets = np.concatenate([train_targets[:i*numValSamples], train_targets[(i+1)* numValSamples:]], axis=0)

    model = build_model()
    model.fit(partialTrainData, partialTrainTargets, epochs= numEpochs, batch_size= 16, verbose=0)

    val_mse, val_mae = model.evaluate(valData, valTargets, verbose=0)
    allScores.append(val_mae)

    print(allScores)
    np.mean(allScores)
