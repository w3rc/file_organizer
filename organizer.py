import os
import shutil

directory = "C:\\Users\\rupay\\Downloads"

file_types = {
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.webp': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.pdf': 'PDFs',
    '.txt': 'Text Files',
    '.docx': 'Documents',
    '.xlsx': 'Spreadsheets',
    '.json': 'Workflows',
    '.mp4': 'Videos',
    '.py': 'Python',
    '.ipynb': 'Notebooks',
    '.pem': 'Secrets'
}

for folder in set(file_types.values()):
    os.makedirs(os.path.join(directory, folder), exist_ok=True)

for filename in os.listdir(directory):
    if filename == "organizer.py":
        continue
    if os.path.isfile(os.path.join(directory, filename)):
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in file_types:
            shutil.move(os.path.join(directory, filename), 
                        os.path.join(directory, file_types[file_ext], filename))

print("Files organized!")
