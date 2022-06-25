import cv2
import numpy as np
import sys
import _thread as thread

rtsp_stream_paths = []

video_capture = []
status_of_captured_frames = []
captured_frames = []
opened_streams_count = 0
def init():
    for path in rtsp_stream_paths:
        video_capture.append(cv2.VideoCapture(path))

    for video in video_capture:
        input_shape = np.shape(video.read()[1])
        captured_frames.append(np.empty(shape=input_shape))

def get_output(opened_streams_count, opened_streames_indexes):
    if opened_streams_count == 1:
        resolution = (1280, 720)
        captured_frames[opened_streames_indexes[0]] = cv2.resize(captured_frames[opened_streames_indexes[0]],
                                                                 resolution)
        return captured_frames[opened_streames_indexes[0]]
    elif opened_streams_count == 2:
        resolution = (768, 432)
        return np.concatenate(tuple((cv2.resize(captured_frames[index], resolution) for index in opened_streames_indexes)),
                                 axis=1)
    elif opened_streams_count == 3:
        resolution = (512, 288)
        return np.concatenate(tuple((cv2.resize(captured_frames[index], resolution) for index in opened_streames_indexes)),
                                 axis=1)
    elif opened_streams_count == 4:
        resolution = (640, 360)
        frames = list(captured_frames[index] for index in opened_streames_indexes)
        for index, frame in enumerate(frames):
            frames[index] = cv2.resize(frame, resolution)
        ostream1 = np.concatenate((frames[0], frames[1]), axis=0)
        ostream2 = np.concatenate((frames[2], frames[3]), axis=0)
        return np.concatenate((ostream1, ostream2), axis=1)
    elif opened_streams_count == 5:
        resolution = (480, 270)
        resolution2 = (960, 540)
        frames = list(captured_frames[index] for index in opened_streames_indexes)
        for index, frame in enumerate(frames[:-1]):
            frames[index] = cv2.resize(frame, resolution)
        frames[-1] = cv2.resize(frames[-1], resolution2)
        ostream1 = np.concatenate((frames[0], frames[1]), axis=0)
        ostream2 = np.concatenate((frames[2], frames[3]), axis=0)
        ostream3 = np.concatenate((ostream1, ostream2), axis=1)
        return np.concatenate((ostream3, frames[-1]), axis=0)
    else:
        resolution = (640, 360)
        frames = list(captured_frames[index] for index in opened_streames_indexes)
        for index, frame in enumerate(frames):
            frames[index] = cv2.resize(frame, resolution)
        ostream1 = np.concatenate((frames[0], frames[1], frames[4]), axis=0)
        ostream2 = np.concatenate((frames[2], frames[3], frames[5]), axis=0)
        return np.concatenate((ostream1, ostream2), axis=1)


def renew_connection(index):
    global video_capture
    video_capture[index] = cv2.VideoCapture(rtsp_stream_paths[index])

def connect_inputs():
    while any(video.isOpened() for video in video_capture):
        opened_streams_count = 0
        opened_streames_indexes = []
        for index, video in enumerate(video_capture):
            status, frame = video.read()
            status_of_captured_frames.append(status)
            if status:
                opened_streams_count += 1
                opened_streames_indexes.append(index)
                captured_frames[index] = frame
            else:
                thread.start_new_thread(renew_connection, (index,))
        ostream = get_output(opened_streams_count, opened_streames_indexes)
        cv2.imshow('output', ostream)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break


def main():
    global rtsp_stream_paths
    args = []
    for arg in sys.argv[1:]:
        args.append(arg)
    rtsp_stream_paths = args
    init()
    connect_inputs()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    sys.exit(main())