import urllib.request
import zipfile
import io
import os
import shutil
import msvcrt
import sys

def admin_privileges_needed():
    try:
        # Attempt to create a file in the working directory
        with open("test.txt", "w") as f:
            f.write("test")
        # If successful, delete the file and return False (admin privileges not needed)
        os.remove("test.txt")
        return False
    except PermissionError:
        # If not successful, return True (admin privileges needed)
        return True

url = 'https://github.com/barteqcz/ctn/archive/refs/heads/main.zip' # URL to the release
src_dir = "ctn-main"
dst_dir = "."

# If admin is needed, print error and exit
if admin_privileges_needed():
    print("Please run the program as admin")
    input("Press any key to exit...")
    sys.exit()

print("Downloading the files...")

# Removing directories if they exist
if os.path.exists("config.js"):
    os.remove("config.js")
if os.path.exists("cities"):
    shutil.rmtree("cities")
if os.path.exists("stations"):
    shutil.rmtree("stations")

# Download the zip file
response = urllib.request.urlopen(url)
zip_file = io.BytesIO(response.read())

# Extract the zip file to the current directory
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(os.getcwd())

# Move the files to its parent directory
for filename in os.listdir(src_dir):
    src_file = os.path.join(src_dir, filename)
    dst_file = os.path.join(dst_dir, filename)
    shutil.move(src_file, dst_file)

# Remove the source directory
os.rmdir(src_dir)

# Remove unnecessary files
os.remove("README.md")
os.remove("LICENSE.md")
print("Downloaded the files successfully ^^")

# Wait for the user to press any key
print("Press any key to exit...")
while True:
    if msvcrt.kbhit():
        msvcrt.getch()  # read and discard the key pressed
        sys.exit()
