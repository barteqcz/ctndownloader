import urllib.request
import zipfile
import io
import os
import shutil

url = 'https://github.com/barteqcz/ctn/archive/refs/heads/main.zip' # URL to the release
src_dir = "ctn-main"
dst_dir = "."

print("Downloading the files...")

# Checking whether the directories and file exist
if os.exists(config.js):
    os.remove(config.js)

if os.path.exists(cities):
    os.rmdir(cities)

if os.path.exists(stations):
    os.rmdir(stations)
    
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

os.remove("README.md")
os.remove("LICENSE.md")
print("Downloaded the files successfully ^^")

# Wait for the user to press a key
input("Press any key to exit...")
