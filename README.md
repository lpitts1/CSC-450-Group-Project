# CSC-450-Group-Project
## Requirements
- Windows 11 or later with Python 3.14.2 or later and Git on PATH, or
- Ubuntu 24.04 or later
## Setup
### Windows
```
git clone https://github.com/lpitts1/CSC-450-Group-Project.git flashcards
py -m venv flashcards
.\flashcards\Scripts\pip.exe install PyQt6
```
### Linux
```
git clone https://github.com/lpitts1/CSC-450-Group-Project.git flashcards
python3 -m venv flashcards
flashcards/bin/pip install PyQt6
```
## Use
### Windows
```
cd \path\to\flashcards
.\Scripts\python.exe ProjectUI.py
```
### Linux
```
cd /path/to/flashcards
bin/python ProjectUI.py
```
### Notes
Use the dropdown menu to switch between documents. +New Document adds a new document to the dropdown. -Delete Document deletes the current document from the dropdown menu and the file system. Save adds the current document to the file system. The first line of text is the file name.
