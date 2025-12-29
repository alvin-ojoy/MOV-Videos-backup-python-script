# MOV Backup Script 🎬

A simple Python script that automatically collects and backs up all `.mov` files from subfolders into a single backup directory — while preserving file metadata and avoiding overwrites.

This is ideal for creators, videographers, and editors who want a fast way to consolidate footage from multiple project folders (e.g., SD card dumps or daily shoot folders).

---

## 📂 What This Script Does

- Scans a root directory for subfolders
- Finds all `.mov` files inside those folders
- Copies them into a single backup folder
- Preserves original metadata (timestamps, etc.)
- Avoids filename overwrites by auto-renaming
- Safe to re-run multiple times

---

## 🗂 Example Folder Structure

### Before running the script:
Root_Folder/ <br>
├── Shoot_01/ <br>
│ ├── A001.mov <br>
│ └── A002.mov <br>
├── Shoot_02/ <br>
│ ├── A001.mov <br>
│ └── B001.mov


### After running the script:

Root_Folder/<br>
├── for_backup/<br>
│ ├── A001.mov<br>
│ ├── A001_1.mov<br>
│ ├── A002.mov<br>
│ └── B001.mov<br>
