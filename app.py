from pathlib import Path
import shutil

# Root directory containing task folders
root_path = Path("/Volumes/Extreme SSD/Desk Reels")

# Destination folder for backups
dest_path = root_path / "for_backup"

# Create destination folder if it doesn't exist
dest_path.mkdir(parents=True, exist_ok=True)

# Loop through all subfolders in root_path
for folder in root_path.iterdir():
    # Skip non-folders and the backup folder itself
    if not folder.is_dir() or folder == dest_path:
        continue

    # Find all .mov files in the current folder
    for file in folder.glob("*.mov"):
        destination_file = dest_path / file.name

        # If file already exists, append a number to the filename
        counter = 1
        while destination_file.exists():
            destination_file = dest_path / f"{file.stem}_{counter}{file.suffix}"
            counter += 1

        # Copy file while preserving metadata
        shutil.copy2(file, destination_file)

print("DONE!")
