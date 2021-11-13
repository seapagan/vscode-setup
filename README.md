# Visual Studio Code Setup files

User and Programming language specific config files, extension lists etc to
reproduce my current VSCode dev setup if needed. They may have some local path
settings etc in them which will need to be sanitised. Also, many of the settings
depend on having the same extensions installed as I do, from the
`global.extensions.json`.

## Files

- [user-settings.json](./user.settings.json) : Complete `User` settings, for
  global use, to replace the existing main settings.
- [remote.settings.json](./remote.settings.json) : `Remote` settings for use in
  WSL or remote SSH sessions.
- [global.extensions.json](./global.extensions.json) : rename this to
  `extensions.json` and place in the `.vscode` subfolder. This will add all the
  listed extensions as suggestions when you next open VSCode in the parent
  directory of that folder.

## Folders

- [.vscode-python](./.vscode-python/) : Settings specific to the Python
  programming language. Rename folder as `.vscode` and place in your project
  folder.
- [.vscode-django](./.vscode-django/) : Settings specific to the Python Django
  framework. Rename folder as `.vscode` and place in your project folder.
- [.vscode-react](./.vscode-react/) : Settings specific to the React
  programming language. Rename folder as `.vscode` and place in your project
  folder.

## Scripts

- [make-extension-config.py](./make-extension-config.py) : A Python script to
  make a `global.extensions.json` file from all the extensions currently loaded
  in your local VSCode installation.
- [make-extension-from-file.py](./make-extension-from-file.py) : Similar script
  that takes its input from a file `extensions.list` in the current folder. This
  file can be created at the command line from your own system using the command
  `code --list-extensions`. TODO : This will be updated to take the filename as
  a command line parameter.
