# pyorganize - A Python CLI tool to organize files in folders by type
#
# 📁 Project Goal:
# Build a simple, effective command-line tool that scans a directory,
# identifies files by their extensions (starting with PDFs), and organizes
# them into categorized subfolders like "PDF Files".
#
# 🎯 Learning Objectives:
# - Understand file system manipulation using Python
# - Practice clean coding and modular structure
# - Implement automated testing using PyTest
# - Set up CI/CD pipelines with GitHub Actions
# - Learn how to package and deploy the CLI tool for use on any system
#
# 🚀 This is not just about writing code — it's about learning the full lifecycle of
# developing, testing, and shipping real-world software.
#
# 📌 Milestones:
# [ ] Detect and move .pdf files into a "PDF Files" folder✅
# [ ] Add support for other file types using a dictionary (Images, Videos, Docs, etc.)✅
# [ ] Implement command-line arguments (target folder, dry-run, etc.)✅
# [ ] Refactor into functions and use OOP for extensibility✅
# [ ] Add unit tests using PyTest
# [ ] Add logging and error handling
# [ ] Set up GitHub repo and CI pipeline (GitHub Actions)
# [ ] Publish as a pip-installable CLI tool (local install)
# [ ] Deploy to PyPI for public use
# [ ] Package as a .exe (Windows) using PyInstaller (optional)





#os.path.isfile() – check if it’s a file

#os.path.join() – safely build paths

#.endswith(".pdf") – filter by extension

#os.makedirs() – make folder if not exists

#shutil.move() – move file from A to B

import os
import shutil
import argparse

# 🔖 File Type Mapping
FILE_MAP = {
    # Documents
    "PDF Files": [".pdf"],
    "Word Files": [".doc", ".docx"],
    "PowerPoint Files": [".ppt", ".pptx", ".odp"],
    "Excel Files": [".xls", ".xlsx", ".csv"],
    "Text Files": [".txt", ".md", ".rtf"],

    # Images
    "Image Files": [".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".tiff", ".svg"],

    # Videos
    "Video Files": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],

    # Audio
    "Audio Files": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],

    # Archives & Installers
    "Software Files": [".exe", ".msi", ".apk", ".deb", ".rpm", ".dmg"],
    "Compressed Files": [".zip", ".rar", ".7z", ".tar", ".gz"],

    # Programming & Dev
    "Programming Files": [
        ".py", ".java", ".cpp", ".c", ".cs", ".html", ".css", ".js",
        ".ts", ".json", ".xml", ".yaml", ".yml", ".sh", ".bat"
    ],

    # Design & Creative
    "Design Files": [".psd", ".ai", ".xd", ".fig", ".sketch"],

    # Misc
    "Other Files": [".log", ".bak", ".tmp"]
}

# 🎯 Argument Parser
def parse_args():
    parser = argparse.ArgumentParser(description="Organize Your Files by Extension")
    parser.add_argument("--path", type=str, required=True, help="Folder to scan")
    parser.add_argument("--dry_run", action="store_true", help="Show what would be moved, don't perform")
    parser.add_argument("--verbose", action="store_true", help="Show each file being moved")
    return parser.parse_args()

# 🧠 File Organizer Class
class FileOrganizer:
    def __init__(self, path, dry_run=False, verbose=False):
        self.path = path
        self.dry_run = dry_run
        self.verbose = verbose

    def organize(self):
        try:
            items = os.listdir(self.path)
            print("Number of Items Found:", len(items))
        except FileNotFoundError:
            print("❌ Folder not found. Check your path.")
            return

        moved_any = False  # Track if any file was moved or would be moved
        for item in items:
            full_path = os.path.join(self.path, item)

            if not os.path.isfile(full_path):
                if self.verbose:
                    print(f"[Verbose] Skipping non-file: {item}")
                continue

            ext = os.path.splitext(item)[1].lower()
            if self.verbose:
                print(f"[Verbose] Checking file: {item} (.{ext})")

            matched = False
            for folder, extensions in FILE_MAP.items():
                if ext in extensions:
                    matched = True
                    destination_folder = os.path.join(self.path, folder)
                    os.makedirs(destination_folder, exist_ok=True)
                    dest_path = os.path.join(destination_folder, item)

                    base, extn = os.path.splitext(item)
                    counter = 1

                    while os.path.exists(dest_path):
                        new_name = f"{base}_{counter}{extn}"
                        dest_path = os.path.join(destination_folder, new_name)
                        counter += 1

                    if self.dry_run:
                        # Always show dry-run actions, even if not verbose
                        print(f"[Dry Run] Would move: {item} → {folder}")
                        moved_any = True
                    else:
                        shutil.move(full_path, dest_path)
                        # Only show actual moves when verbose
                        if self.verbose:
                            print(f"Moved: {item} → {folder}")
                        moved_any = True

                    break  # Stop after first match
            if not matched and self.verbose:
                print(f"[Verbose] No category for: {item}")

        if not moved_any:
            print("No files matched any category or needed to be moved.")


# 🚀 Run as script
if __name__ == '__main__':
    args = parse_args()
    organizer = FileOrganizer(args.path, dry_run=args.dry_run, verbose=args.verbose)
    organizer.organize()


    #python pyorganize.py --path C:\Users\BILAL\Downloads --verbose

