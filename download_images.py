import requests
import os
import re

def download_image(url, file_path, file_name):
    full_path = os.path.join(file_path, file_name)
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(full_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

def rename_image(file_path, file_name):
    match = re.match(r"^[0-9]{13}(.*)$", file_name)
    if match:
        new_file_name = match.group(1)
    else:
        new_file_name = file_name[0:13]

    if os.path.exists(os.path.join(file_path, new_file_name)):
        new_file_name = new_file_name + "_1"

    os.rename(os.path.join(file_path, file_name), os.path.join(file_path, new_file_name))

def main():
    url = "https://example.com/images"
    file_path = "/path/to/save/images"

    for image_url in requests.get(url).json():
        file_name = image_url["filename"]
        download_image(image_url["url"], file_path, file_name)
        rename_image(file_path, file_name)

if __name__ == "__main__":
    main()
