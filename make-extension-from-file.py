"""Extension list to JSON.

Create an 'extensions.json' file based on a dumped text file
"""

import json

OUTPUT_JSON = ".insiders-extensions.json"

with open("extensions.list", encoding="utf-8") as file:
    result = file.read().splitlines()

# if remote, the first line is the name of the environment we're running this
# on.
if "Extensions installed" in result[0]:
    CODE_ENVIRONMENT = result.pop(0).split(":")[1].strip()
else:
    CODE_ENVIRONMENT = "global"
print(f"Saving extensions.json for the '{CODE_ENVIRONMENT}' environment.")

output_dict: dict[str, list[str]] = {"recommendations": []}

for extension in result:
    output_dict["recommendations"].append(extension.strip())


with open(f"{CODE_ENVIRONMENT}{OUTPUT_JSON}", "w", encoding="utf-8") as file:
    file.write(json.dumps(output_dict, indent=2))
