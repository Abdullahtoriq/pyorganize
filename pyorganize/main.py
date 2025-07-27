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
# [ ] Add support for other file types using a dictionary (Images, Videos, Docs, etc.)
# [ ] Implement command-line arguments (target folder, dry-run, etc.)
# [ ] Refactor into functions and use OOP for extensibility
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

def move_pdfs(folder_name):

    try:
        items = os.listdir(folder_name)
        print("Number of Items Found: ", len(items))
        # print("📂 Items In Folder: ", items)
    except FileNotFoundError:
        print("❌ Folder not found. Check your path.")
        return

    for item in items:
        # Full Path of File require to change it position later
        full_path = os.path.join(folder_name, item)
        #checking if full_path it ends with a pdf
        if os.path.isfile(full_path) and full_path.lower().endswith(".pdf"):
            pdf_folder = os.path.join(folder_name, "PDF Files")
            os.makedirs(pdf_folder, exist_ok=True)  # Creates if not exists
            dest_path = os.path.join(pdf_folder, item)
            shutil.move(full_path, dest_path)
            print(f"📄 Moved: {item}")


if __name__ == '__main__':
    folder_to_scan = input("Enter The Folder in which You Want to Arrange Your Pdf Into One Folder: ")
    move_pdfs(folder_to_scan)
