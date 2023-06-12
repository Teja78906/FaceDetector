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

   ```bash
   git clone https://github.com/your_username/face-detection-recognition.git

