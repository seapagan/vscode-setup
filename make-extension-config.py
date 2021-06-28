"""
Create a 'global.extensions.json' file based on a test file listing
VSCode extensions, this should be renamed to 'extensions.json' and placed in
the final vscode directiory
"""

import json

EXTENSION_LIST = "raw-extension-list.txt"
OUTPUT_JSON = "global.extensions.json"


output_dict = {"recommendations": []}

with open(EXTENSION_LIST, "r") as file:
    for line in file:
        output_dict["recommendations"].append(line.strip())

with open(OUTPUT_JSON, "w") as file:
    file.write(json.dumps(output_dict, indent=4))
