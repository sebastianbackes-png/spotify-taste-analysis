import glob
import pandas as pd
import json
import pathlib
from pathlib import Path


def load_streaming_history(data_path: Path):
    json_files = data_path.glob("*.json")
    all_data = []

    for file in json_files:
        print(file)
        data = pd.read_json(file)
        all_data.append(data)

    df = pd.concat(all_data, ignore_index=True)
    return df