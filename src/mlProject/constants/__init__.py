from pathlib import Path
import os
CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Adarsh63/MLOps_Project.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="Adarsh63"
os.environ["MLFLOW_TRACKING_PASSWORD"]="b82416e02e08e727dd58201b443b8b9d051ec776"