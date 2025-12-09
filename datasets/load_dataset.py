#loading dataset from huggingface datasets
#we will be using : https://huggingface.co/datasets/AlmondGod/tinyworlds

from huggingface_hub import hf_hub_download
from pathlib import Path
import sys
import os 
PROJECT_ROOT = Path(__file__).resolve().parent.parent #root folder 

sys.path.append(str(PROJECT_ROOT)) #
from configs import repo_id, dataset_list
#os.makedirs("datasets/tinyworlds", exist_ok=True)
#dataset = load_dataset("AlmondGod/tinyworlds/")
#dataset.save_to_disk("datasets/tinyworlds")

repo_id = repo_id    #initialised in configs/__init__.py 
dataset_list = dataset_list #collected in configs/__init__.py


for id in dataset_list :
    print(f"downlading {id}")
    hf_hub_download(
        repo_id=repo_id,
        repo_type="dataset", 
        filename=id,
        local_dir="datasets/tinyworlds",  # All files go here
        local_dir_use_symlinks=False 
    )
print("dw bro , datasets got downloaded")
