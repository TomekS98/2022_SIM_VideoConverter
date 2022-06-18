import cv2
import numpy as np
cap1 = cv2.VideoCapture("rtsp://localhost:8554/xd")
cap2 = cv2.VideoCapture("rtsp://localhost:8554/xd2")
cap3 = cv2.VideoCapture("rtsp://localhost:8554/xd")
cap4 = cv2.VideoCapture("rtsp://localhost:8554/xd")
cap5 = cv2.VideoCapture("rtsp://localhost:8554/xd")
cap6 = cv2.VideoCapture("rtsp://localhost:8554/xd")
cap7 = cv2.VideoCapture("rtsp://localhost:8554/xd")
cap8 = cv2.VideoCapture("rtsp://localhost:8554/xd")
cap9 = cv2.VideoCapture("rtsp://localhost:8554/xd")

while(cap1.isOpened()):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()
    ret4, frame4 = cap4.read()
    ret5, frame5 = cap5.read()
    ret6, frame6 = cap6.read()
    ret7, frame7 = cap7.read()
    ret8, frame8 = cap8.read()
    ret9, frame9 = cap9.read()

    if ret2 == False:
        cap2 = cv2.VideoCapture("rtsp://localhost:8554/xd2")
    # for index, frame in enumerate(frames):
    #     if frame is not None:
    #         frame[index] = cv2.resize(frame)
    if frame1 is not None:
        frame1 = cv2.resize(frame1, (1000, 1000))
    if frame2 is not None:
        frame2 = cv2.resize(frame2, (1000, 1000))

    if frame1 is not None and frame2 is not None:
        frame1 = cv2.resize(frame1, (1000,500))
        frame2 = cv2.resize(frame2, (1000, 500))
        ostream = np.concatenate((frame1, frame2), axis=0)
        ostream.shape == (frame1.shape[0], 2 * frame2.shape[1])
    elif frame1 is not None:
        ostream = frame1

    cv2.imshow('output', ostream)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()