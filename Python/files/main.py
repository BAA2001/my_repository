__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"
import os
from zipfile import ZipFile

cache_file = "cache"
data = "data.zip"
cache_dir = os.getcwd()
cache_path = os.path.join(cache_dir, cache_file)
zip_path = os.path.join(cache_dir, data)


def clean_cache():
    if not os.path.isdir(cache_path):
        os.makedirs(cache_path)
    else:
        for files in os.listdir(cache_path):
            os.remove(os.path.join(cache_path, files))


def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path, "r") as zObject:
        zObject.extractall(cache_dir_path)


def cached_files():
    files = [os.path.join(cache_path, file) for file in os.listdir(cache_path)]
    return files


def find_password(files=cached_files()):
    for file in files:
        with open(file) as f:
            for item in f:
                if "password" in item:
                    print(item[10:])


if __name__ == "__main__":
    clean_cache()
    cache_zip(zip_file_path=zip_path, cache_dir_path=cache_path)
    cached_files()
    find_password(cached_files())
