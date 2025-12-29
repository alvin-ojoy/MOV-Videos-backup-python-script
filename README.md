# Desk Reels Backup Script 🎬

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
Desk Reels/
├── Shoot_01/
│ ├── A001.mov
│ └── A002.mov
├── Shoot_02/
│ ├── A001.mov
│ └── B001.mov


### After running the script:

Desk Reels/
├── for_backup/
│ ├── A001.mov
│ ├── A001_1.mov
│ ├── A002.mov
│ └── B001.mov
