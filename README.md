# CodeAlpha JPG File Organizer

A small Python automation tool that finds `.jpg` files in a folder and moves them into a separate folder automatically.

I built this project as part of my CodeAlpha Python Programming Internship to practice file handling and Python's `os` and `shutil` modules.

## About the Project

Instead of manually searching through a folder for JPG images and moving them one by one, this program does the job automatically.

When the program runs, it checks the `source_files` folder for JPG files and moves them to the `jpg_files` folder.

The required folders are created automatically if they don't already exist.

# What the Program Can Do

- Creates the required folders automatically
- Finds `.jpg` files in the source folder
- Handles `.JPG` and other uppercase/lowercase variations
- Moves JPG files to the destination folder
- Leaves non-JPG files untouched
- Prevents accidental overwriting of existing files
- Reports which files were moved
- Handles file-system errors
- Shows a message when no JPG files are found

## How It Works

The program uses two folders:

text
source_files


    Example:

source_files/
 photo1.jpg
 photo2.JPG
 document.pdf
 notes.txt

After running the program:

source_files/
 document.pdf
 notes.txt

jpg_files/
 photo1.jpg
 photo2.JPG


How to Run:

Make sure Python 3 is installed.

Open a terminal in the project folder and run:

python file_organizer.py

The program will automatically create:

source_files
jpg_files

Place your JPG files inside source_files and run the program again.

Example Output
=============================================
          JPG FILE ORGANIZER
=============================================

Moved: photo1.jpg
Moved: photo2.JPG

---------------------------------------------
2 JPG file(s) moved successfully.
---------------------------------------------
Task completed.

If there are no JPG files:

No JPG files were found to move.