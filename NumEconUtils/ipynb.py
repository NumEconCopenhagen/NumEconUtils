import json
import os
import re

def ipynb_clear_regex(path, regex="^#fillin"):
        ipynb_json = read_ipynb(path)
        ipynb_json_updated = remove_content(read_cells(ipynb_json), regex)
        copy_ipynb(ipynb_json_updated, path)

def read_ipynb(path):
    with open(path, 'r') as f:
        return json.load(f)

def copy_ipynb(ipynb, path):
    path_, ext = os.path.splitext(path)
    new_path = f"{path_}_fillin{ext}"     
    with open(new_path, 'w') as f:
        return json.dump(ipynb, f)

def read_cells(jsondic):
    return [cell for cell in jsondic['cells']]

def remove_content(jsondic, regex):
        for idx, cell in enumerate(jsondic):
                if cell['cell_type'] == 'code' and re.search(regex, cell['source'][0]):
                        jsondic[idx]['source'] = []
        return jsondic