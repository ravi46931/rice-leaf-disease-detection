# import os
# import sys
# import json
# import time
# import warnings
# from src.logger import logging
# from src.exception import CustomException
# from src.constants import *
# from src.constants.hyperparameter import *
# from src.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
# from src.entity.config_entity import ModelTrainerConfig
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import tensorflow as tf
import matplotlib.pyplot as plt
# from tensorflow.keras.preprocessing.image import ImageDataGenerator 

train_dir = "data/model/train"
val_dir = "data/model/dev"

image_height, image_width = 64, 64
batch_size = 32

# Load the training dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(
    train_dir,
    labels="inferred",
    label_mode="int",  # For multiclass classification
    batch_size=batch_size,
    image_size=(image_height, image_width),
    shuffle=True
)

# Load the validation dataset
val_dataset = tf.keras.utils.image_dataset_from_directory(
    val_dir,
    labels="inferred",
    label_mode="int",
    batch_size=batch_size,
    image_size=(image_height, image_width),
    shuffle=False
)

from tensorflow.keras import layers, models
num_classes = 4
model = models.Sequential([
    layers.Input(shape=(image_height, image_width, 3)),  # Use Input layer to specify input shape
    layers.Rescaling(1./255),
    # layers.Rescaling(1./255, input_shape=(image_height, image_width, 3)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),  # Add dropout to reduce overfitting
    layers.Dense(num_classes, activation='softmax')
])

model.compile(
    optimizer='adam',                          # Optimizer
    loss='sparse_categorical_crossentropy',   # Loss function for multi-class classification
    metrics=['accuracy']                       # Metrics to track
)

# Assuming the model is already defined and compiled
epochs = 5
history = model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=epochs
)

# Evaluate the model on the validation set
val_loss, val_accuracy = model.evaluate(val_dataset)
print(f"Validation Loss: {val_loss}")
print(f"Validation Accuracy: {val_accuracy}")

