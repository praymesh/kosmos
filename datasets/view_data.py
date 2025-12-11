#we have our dataset in .h5 format , this is a utility to visualize the data samples 
import h5py #for handling h5 files
import numpy as np
import cv2
import os
import argparse
from pathlib import Path
root = Path(__file__).resolve().parent.parent  # Add parent directory to sys.path
file_path = root / "datasets" / "tinyworlds" / "pole_position_frames.h5"


def view_h5_data(file_path, num_samples=5):
    with h5py.File(file_path, 'r') as h5_file:
        #print("Available datasets in the file:")
        print(list(f.keys() for f in [h5_file]))
        for key in h5_file.keys():
            print(f" - {key}")
            print(f"   Shape: {h5_file[key].shape}, Dtype: {h5_file[key].dtype}")
            
def play_vid(file_path, fps, max_frames = 10000, scale=5.0) : #scale added since the pixels are small
    with h5py.File(file_path , "r") as h5_file:
        frames = h5_file["frames"][:max_frames]
        for frame in frames :
            frame = cv2.cvtColor(frame , cv2.COLOR_RGB2BGR)
            
            if scale != 1.0:
                width = int(frame.shape[1] * scale)
                height = int(frame.shape[0] * scale)
                frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_NEAREST)

            delay = int(1000 / fps)
            
            cv2.imshow("frame" , frame)
            key = cv2.waitKey(delay)
            if key == 27 : #esc key
                break
        cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="View H5 dataset frames")
    parser.add_argument("--fps", type=int, default=30, help="Frames per second playback speed")
    parser.add_argument("--scale", type=float, default=5.0, help="Video scale factor")
    args = parser.parse_args()

    play_vid(file_path, fps=args.fps, max_frames=1000, scale=args.scale)
    view_h5_data(file_path, num_samples=5)
