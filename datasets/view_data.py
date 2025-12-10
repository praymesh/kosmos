#we have our dataset in .h5 format , this is a utility to visualize the data samples 
import h5py #for handling h5 files
import numpy as np
import cv2
import os
from pathlib import Path
root = Path(__file__).resolve().parent.parent  # Add parent directory to sys.path
file_path = root / "datasets" / "tinyworlds" / "pong_frames.h5"

def view_h5_data(file_path, num_samples=5):
    with h5py.File(file_path, 'r') as h5_file:
        #print("Available datasets in the file:")
        print(list(f.keys() for f in [h5_file]))
        for key in h5_file.keys():
            print(f" - {key}")
            print(f"   Shape: {h5_file[key].shape}, Dtype: {h5_file[key].dtype}")
            
def play_vid(file_path, fps, max_frames = 1000) :
    with h5py.File(file_path , "r") as h5_file:
        frames = h5_file["frames"][0]
        for frame in frames :
            cv2.imshow("frame" , frame)

play_vid(file_path, fps=30, max_frames=1000)
view_h5_data(file_path, num_samples=5)
