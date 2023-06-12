# Face Detection and Recognition

This repository contains code for real-time face detection and recognition using the Fisherfaces algorithm.

## Description

The face detection and recognition system uses the OpenCV library to perform real-time face detection and recognition on a live video stream. It detects faces in the video frames, preprocesses the face images, and then classifies them using the Fisherfaces algorithm. The detected faces are surrounded by rectangles, and the recognized faces are labeled with their corresponding IDs and confidence scores.

## Features

- Real-time face detection and recognition
- Preprocessing techniques like histogram equalization for improved recognition performance
- Training of the face classifier using the Fisherfaces algorithm
- Draw rectangles around detected faces and label recognized faces

## Requirements

- Python 3.x
- OpenCV (cv2) library
- PIL library
- Numpy library

## Usage

1. Clone the repository:
``` bash
git clone https://github.com/Teja78906/face-detection-recognition.git
 ```
2. Install the required libraries:

```bash
pip install opencv-python pillow numpy
```
3.  Run the UserDataCapturingUtil.py
```bash
python UserDataCapturingUtil.py
```
 this will capture the training data used by the faceDetector algorithm for face detection

4. Run the faceDetector.py script:
```bash
python faceDetector.py
```
5. The script will open the video capture and start detecting and recognizing faces in real-time.

## Customization
You can adjust the confidence threshold for face recognition by modifying the confidence_threshold parameter in the detect() function.
Experiment with different preprocessing techniques in the preprocess_image() function to enhance the quality of input images.
