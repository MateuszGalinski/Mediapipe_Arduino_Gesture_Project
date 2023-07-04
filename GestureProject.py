import mediapipe as mp
import cv2
import serial
import time
from google.protobuf.json_format import MessageToDict

arduino = serial.Serial(port = 'COM3', baudrate = 9600)

vid = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

def write_read_to_arduino(write_data):
    arduino.write(str.encode(write_data))
    time.sleep(0.05)
    read_data = arduino.read()
    return read_data

def detect_if_hand_right(results, camera_vid):
    for i in results.multi_handedness:
        label = MessageToDict(i)['classification'][0]['label']
    if label == 'Right' and len(results.multi_handedness)!=2:
        return True

    height, width, channels = camera_vid.shape
    cv2.putText(camera_vid, 'Use only right hand', (height//3, width//20),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.9, (0, 255, 0), 2)
    return False
    
def track_tumb(landmarks, camera_vid):
    height, width, channels = camera_vid.shape
    index_sec_seg_x = landmarks.landmark[6].x * width
    index_sec_seg_y = landmarks.landmark[6].y * height
    thumb_sec_seg_y = landmarks.landmark[3].y * height
    thumb_tip_x = landmarks.landmark[4].x * width
    thumb_tip_y = landmarks.landmark[4].y * height
    thumb_base_x = landmarks.landmark[1].x * width

    return index_sec_seg_x, index_sec_seg_y, thumb_sec_seg_y, thumb_tip_x, thumb_tip_y, thumb_base_x

def is_thumb_up(landmarks, camera_vid):
    ind_sec_seg_x, ind_sec_seg_y, thumb_sec_seg_y, thumb_t_x, thumb_t_y, thumb_b_x = track_tumb(landmarks, camera_vid)
    #thumb on the left detection
    if thumb_t_x < thumb_b_x and thumb_t_y < thumb_sec_seg_y and thumb_t_x < ind_sec_seg_x:
        return 1
    #thumb up detection
    if thumb_t_y < ind_sec_seg_y and thumb_t_y < thumb_sec_seg_y:
        return 1
    return 0

def track_finger(landmarks, camera_vid, finger_tip_number):
    height, width, channels = camera_vid.shape
    
    tip_position_y = landmarks.landmark[finger_tip_number].y * height
    segment_position_y = landmarks.landmark[finger_tip_number - 1].y * height
    second_segment_position_y = landmarks.landmark[finger_tip_number - 2].y * height
    base_position_y = landmarks.landmark[finger_tip_number - 3].y * height

    return tip_position_y, segment_position_y, second_segment_position_y, base_position_y

def is_finger_up(landmarks, camera_vid, finger_tip_number):
    tip_y, seg_y, sec_seg_y, base_y = track_finger(landmarks, camera_vid, finger_tip_number)
    if tip_y < base_y and tip_y < seg_y and tip_y < sec_seg_y:
        return 1
    return 0

def main():
    num_of_fingers = 0
    while(True):
        succ, camera_vid = vid.read()
        
        camera_vid = cv2.flip(camera_vid, 1)
        camera_vid_RGB = cv2.cvtColor(camera_vid, cv2.COLOR_BGR2RGB)

        hand_result = hands.process(camera_vid_RGB)

        if hand_result.multi_hand_landmarks:
            for hand_landmarks in hand_result.multi_hand_landmarks:
                mp_draw.draw_landmarks(camera_vid, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                for finger_number in range(8, 21, 4):
                    num_of_fingers += is_finger_up(hand_landmarks, camera_vid, finger_number)
                
                num_of_fingers += is_thumb_up(hand_landmarks, camera_vid)

                if detect_if_hand_right(hand_result, camera_vid):
                    write_read_to_arduino(str(num_of_fingers))
            
                num_of_fingers = 0

        cv2.imshow('Hand tracking', camera_vid)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()