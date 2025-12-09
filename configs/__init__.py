

import yaml
from pathlib import Path
import sys
#sys.path.append(str(Path(__file__).resolve().parent))
#yaml_path = Path(__file__).resolve().parent / "dataset.yaml"
yaml_path = Path(__file__).resolve().parent / "dataset.yaml"
try :
    with open(yaml_path, "r") as f:
        config = yaml.safe_load(f)
        
    repo_id = config.get("repo_id")
    dataset_list = config.get("dataset_list")

except FileNotFoundError :
    print("dataset.yaml not found.")
except ImportError:
    pass
