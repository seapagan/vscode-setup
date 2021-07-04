"""Extension list to JSON.

Create an 'extensions.json' file based on a dumped text file
"""

import json

OUTPUT_JSON = ".extensions.json"

with open("extensions.list") as file:
    result = file.read().splitlines()

# if remote, the first line is the name of the environment we're running this
# on.
if "Extensions installed" in result[0]:
    code_environment = result.pop(0).split(":")[1].strip()
else:
    code_environment = "global"
print(f"Saving extensions.json for the '{code_environment}' environment.")

output_dict = {"recommendations": []}

for extension in result:
    output_dict["recommendations"].append(extension.strip())


with open(f"{code_environment}{OUTPUT_JSON}", "w") as file:
    file.write(json.dumps(output_dict, indent=4))
