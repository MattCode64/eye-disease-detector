from typing import List, Any, Tuple
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator

# Import libraries for data manipulation
import numpy as np
import pandas as pd
import os
import glob
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping, ModelCheckpoint


# Define a function to create a CNN model that takes in input images of eye diseases and classifies them into 2
# classes : 0 for NoDisease and 1 for Disease
def create_model(activation='relu', optimizer='adam', dropout_rate=0.2, learn_rate=0.01, momentum=0):
    # Create a Sequential model
    model = Sequential()

    # Add a convolutional layer
    model.add(layers.Conv2D(32, (3, 3), activation=activation, input_shape=(224, 224, 3)))

    # Add a pooling layer
    model.add(layers.MaxPooling2D((2, 2)))

    # Add a convolutional layer
    model.add(layers.Conv2D(64, (3, 3), activation=activation))

    # Add a pooling layer
    model.add(layers.MaxPooling2D((2, 2)))

    # Add a convolutional layer
    model.add(layers.Conv2D(128, (3, 3), activation=activation))

    # Add a pooling layer
    model.add(layers.MaxPooling2D((2, 2)))

    # Add a convolutional layer
    model.add(layers.Conv2D(128, (3, 3), activation=activation))

    # Add a pooling layer
    model.add(layers.MaxPooling2D((2, 2)))

    # Add a flattening layer
    model.add(layers.Flatten())

    # Add a dropout layer
    model.add(layers.Dropout(dropout_rate))

    # Add a dense layer
    model.add(layers.Dense(512, activation=activation))

    # Add a dense layer
    model.add(layers.Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(loss='binary_crossentropy',
                  optimizer=optimizer,
                  metrics=['accuracy'])

    # Return the model
    return model


# Specify the path to the folder containing the images of no disease
no_disease_path = r"C:\Data\Projet CODE\Code Python\DataCamp Code\data\preparing_model\images_train\No_Disease_Risk"
no_disease_image_paths = glob.glob(no_disease_path + "/*.png")

# Specify the path to the folder containing the images of disease
disease_path = r"C:\Data\Projet CODE\Code Python\DataCamp Code\data\preparing_model\images_train\Disease_Risk"
disease_image_paths = glob.glob(disease_path + "/*.png")


# Define a function to create a dataframe containing the image paths and the corresponding labels
def create_dataframe(image_paths: List[Any], label: int) -> pd.DataFrame:
    # Create a dataframe
    df = pd.DataFrame(image_paths, columns=['image_path'])

    # Add a column containing the labels
    df['label'] = label

    # Return the dataframe
    return df


# Create a dataframe containing the image paths and the corresponding labels
no_disease_df = create_dataframe(no_disease_image_paths, 0)
disease_df = create_dataframe(disease_image_paths, 1)

# Concatenate the 2 dataframes
df = pd.concat([no_disease_df, disease_df], ignore_index=True)


# Define a function to split the dataframe into train and test sets
def split_dataframe(df: pd.DataFrame, test_size: float) -> tuple[Any, Any]:
    # Split the dataframe into train and test sets
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=42, stratify=df['label'])

    # Return the train and test sets
    return train_df, test_df


# Split the dataframe into train and test sets
train_df, test_df = split_dataframe(df, test_size=0.2)

# Specify the path to the two folders NoDisease and Disease that will contain the images of the train set
train_no_disease_path = r"C:\Data\Projet CODE\Code Python\DataCamp Code\data\preparing_model\images_train\No_Disease_Risk"
train_disease_path = r"C:\Data\Projet CODE\Code Python\DataCamp Code\data\preparing_model\images_train\Disease_Risk"

# Split the train images in train and test
train_df, val_df = split_dataframe(train_df, test_size=0.2)

# Training the model
# Specify the batch size
batch_size = 32

# Specify the image size
img_height = 224
img_width = 224

# Create a data generator for the train set
train_datagen = ImageDataGenerator(rescale=1. / 255)

# Create a data generator for the validation set
val_datagen = ImageDataGenerator(rescale=1. / 255)

# Create a data generator for the test set
test_datagen = ImageDataGenerator(rescale=1. / 255)

# Create a data generator for the train set
train_generator = train_datagen.flow_from_dataframe(
    dataframe=train_df,
    x_col='image_path',
    y_col='label',
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary')

# Create a data generator for the validation set
val_generator = val_datagen.flow_from_dataframe(
    dataframe=val_df,
    x_col='image_path',
    y_col='label',
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary')

# Create a data generator for the test set
test_generator = test_datagen.flow_from_dataframe(
    dataframe=test_df,
    x_col='image_path',
    y_col='label',
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary')

# Create a CNN model
model = create_model()

# Specify the number of epochs
epochs = 30

# Specify the path to the folder containing the model checkpoints
checkpoint_path = r"C:\Data\Projet CODE\Code Python\DataCamp Code\data\preparing_model\checkpoints"

# Create a callback that saves the model's weights
cp_callback = ModelCheckpoint(filepath=checkpoint_path,
                              save_weights_only=True,
                              verbose=1)

# Fit the model
history = model.fit(train_generator,
                    validation_data=val_generator,
                    epochs=epochs,
                    callbacks=[cp_callback])

# Evaluate the model
model.evaluate(test_generator)

# Save the model
# model.save(r"C:\Data\Projet CODE\Code Python\DataCamp Code\data\ressources\H5\kkkkkeras_model.h5")