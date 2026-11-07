import argparse


def sample(video_path, stride=1):
    """Yield consecutive frame triplets from a video."""
    import cv2
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        frames.append(frame)
    for i in range(0, len(frames) - 2, stride):
        yield frames[i], frames[i + 1], frames[i + 2]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("video")
    parser.parse_args()
