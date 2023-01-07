"""
Model takes video data as input and outputs the hand gesture being made.

Supported gestures are scroll up (hand moves up), scroll down (move hand down),
    scroll left (move hand left), scroll right (move hand right), click (move hand forward),
    zoom in (move hands together), zoom out (move hands apart), minimize (close hand),
    and maximize (open hand).

Inputs:
    5 frames of image data condensed to 50 by 50 pixels.

Outputs:
    4 numbers representing likelihood that each motion has been done.
"""

# Code made by Isaac Joffe

import tf as tensorflow

def make_data():
    pass

def make_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=(12500,)))    # inputs of select frames from video
    model.add(tf.keras.layers.Dense(512, activation='relu'))    # hidden layer in the network
    model.add(tf.keras.layers.Dense(256, activation='relu'))    # hidden layer in the network
    model.add(tf.keras.layers.Dense(128, activation='relu'))    # hidden layer in the network
    model.add(tf.keras.layers.Dense(4))    # outputs representing gestures

    model.compile(optimizer='adam',
        loss=tf.keras.losses.binary_crossentropy,
        metrics=[
            tf.keras.metrics.BinaryAccuracy(name='accuracy'),
            tf.keras.metrics.Precision(name='precision'),
            tf.keras.metrics.Recall(name='recall'),
            tf.keras.metrics.TruePositives(name='tp'),
            tf.keras.metrics.TrueNegatives(name='tn'),
            tf.keras.metrics.FalsePositives(name='fp'),
            tf.keras.metrics.FalseNegatives(name='fn')]
    )

    model.fit(input_data, output_data, epochs=100)

    model.save("golden_model")

def main():
    make_data()
    make_model()

if __name__ == "__main__":
    main()
