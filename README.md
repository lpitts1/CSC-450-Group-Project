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
> [!CAUTION]
> To avoid data loss, save before switching the dropdown menu, changing tabs, or closing the app!

Notes files in the following format can also be read as flashcards documents:
> Problem 1:Solution 1
> Problem 2:Solution 2
> Problem 3:Solution 3
### Card Edit
Use the dropdown menu to switch between decks. +New Deck adds a new deck to the dropdown menu. +New Card adds a new card to the current deck. -Delete Deck deletes the current deck from the dropdown and the file system. -Delete Card deletes the current card from the current deck. Save Card adds the current card to the current deck (**not the file system**). Save Deck saves the current deck to the file system.
> [!CAUTION]
> You must click Save Card before switching cards or before saving the deck! Otherwise, your changes will NOT be retained! To avoid data loss, click Save Card and Save Deck before switching the dropdown menu, switching tabs, or closing the app!

Notes files typed in the format above will be interpreted as follows.
> Front		Back
> Problem 1	Solution 1
> Problem 2	Solution 2
> Problem 3	Solution 3
### Study Session
Use the dropdown to select a flashcards file previously made using Card Edit or Notes. Click begin to begin clicking through the fronts and backs one my one. After clicking through all the flashcards, you will be shown five joke flashcards as a reward. You will then have the option to begin a different deck or the same one.

