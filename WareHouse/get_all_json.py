import os
import json
from pprint import pprint


def get_json(file_path):
    base_dir = "D:\\project\\python\\ChatDev\\WareHouse"

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf8') as f:
                    data = json.load(f)
                    
                folder_name = os.path.basename(root)
                new_file_name = f"{folder_name}___{file}"
                
                # sub_dir = os.path.basename(root)
                new_file_path = ','.join(os.path.split(root)[0:-2])
                new_file_path = os.path.join(new_file_path, 'json_out', new_file_name)
                # print(root, new_file_name)
                # print(new_file_path)
                with open(new_file_path, 'w', encoding='utf8') as f:
                    json.dump(data, f)
            # break
        # break


def get_sub_dirs(base_dir):
    return [os.path.join(base_dir, f) for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]


if __name__ == "__main__":
    base_dir = "D:\\project\\python\\ChatDev\\WareHouse"
    result  = get_sub_dirs(base_dir)
    result = [' '.join(os.path.basename(f).split('_')[:2]) for f in result]
    pprint(result)