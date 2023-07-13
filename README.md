# Mediapipe_Arduino_Gesture_Project

Video explanation of the program: https://drive.google.com/file/d/1Oz6MXWD0tKj6Fwb92aZvmz7JsJYtKyVg/view?usp=sharing

This code uses the Mediapipe library and OpenCV to track hand gestures and communicate the detected gestures to an Arduino board. Here is a breakdown of the code:

The code imports the necessary libraries: mediapipe, cv2 (OpenCV), serial, time, and MessageToDict from google.protobuf.json_format.
It sets up the serial connection with an Arduino board connected to the COM3 port at a baud rate of 9600.

The code initializes the webcam video capture using cv2.VideoCapture(0) and sets up the hand tracking using the mp_hands.Hands() module from Mediapipe. It also initializes the mp_draw module for drawing landmarks on the camera video.

There are several utility functions:
  write_read_to_arduino: Writes data to the Arduino and reads the response.
  detect_if_hand_right: Checks if the detected hand is the right hand based on the classification label. It also displays a message on the camera video if 
  the hand is not the right hand or if both hands are detected.
  track_tumb: Tracks the thumb landmarks and returns relevant coordinates for gesture detection.
  is_thumb_up: Checks if the thumb is raised in a thumbs-up gesture based on the thumb landmarks and other coordinates.
  track_finger: Tracks the landmarks of a specific finger and returns relevant coordinates for gesture detection.
  is_finger_up: Checks if a specific finger is raised based on the finger landmarks and coordinates.

The main function is the main entry point of the program. It reads frames from the webcam, flips the frames horizontally, and processes them using the hand tracking model. It draws landmarks on the camera video and checks for various hand gestures. If the hand is detected as the right hand, it sends the number of raised fingers to the Arduino board using the write_read_to_arduino function.

The program continues to run until the user presses 'q' to quit. It releases the webcam video capture and closes all windows.
Overall, this code demonstrates how to use Mediapipe and OpenCV to track hand gestures in real-time and communicate the detected gestures with an Arduino board.
