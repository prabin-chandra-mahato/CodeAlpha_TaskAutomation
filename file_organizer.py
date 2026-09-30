import os
import shutil


SOURCE_FOLDER = "source_files"
DESTINATION_FOLDER = "jpg_files"


def create_folders():
    os.makedirs(SOURCE_FOLDER, exist_ok=True)
    os.makedirs(DESTINATION_FOLDER, exist_ok=True)


def move_jpg_files():
    moved_files = []

    for filename in os.listdir(SOURCE_FOLDER):
        source_path = os.path.join(SOURCE_FOLDER, filename)

        # Ignore folders
        if not os.path.isfile(source_path):
            continue

        # Check for JPG files
        if filename.lower().endswith(".jpg"):
            destination_path = os.path.join(DESTINATION_FOLDER, filename)

            # Avoid overwriting an existing file
            if os.path.exists(destination_path):
                print(f"Skipped: {filename} already exists in the destination folder.")
                continue

            try:
                shutil.move(source_path, destination_path)
                moved_files.append(filename)
                print(f"Moved: {filename}")

            except OSError as error:
                print(f"Could not move {filename}: {error}")

    return moved_files


def main():
    print("=" * 45)
    print("          JPG FILE ORGANIZER")
    print("=" * 45)

    create_folders()

    moved_files = move_jpg_files()

    print("\n" + "-" * 45)

    if moved_files:
        print(f"{len(moved_files)} JPG file(s) moved successfully.")
    else:
        print("No JPG files were found to move.")

    print("-" * 45)
    print("Task completed.")


if __name__ == "__main__":
    main()