import json
import os
from typing import Optional

def parse_http(file_name: str) -> Optional[dict[str, str]]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, "r", encoding="utf-8") as file:
        return {
            k.strip(): v.strip()
            for line in file
            if line.strip() and ':' in line and not line.lstrip().startswith('#')
            for k, v in [line.split(':', 1)]
        }


def load_config(*file_names: str) -> dict:
    config = {}
    script_dir = os.path.dirname(os.path.abspath(__file__))

    for file_name in file_names:
        file_path = os.path.join(script_dir, file_name)
        
        with open(file_path, "r", encoding="utf-8") as file:
            config.update(json.load(file))

    return config


if __name__ == "__main__":
    result = parse_http("file2.txt")
    if result:
        print("Parse result:", result)

    config = load_config("file1.json", "file2.json")
    print("Merge result:", config)
