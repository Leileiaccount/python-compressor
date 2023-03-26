import zipfile
import pathlib


def zip_creator(filepaths, des_path):
    des_dir_name = pathlib.Path(des_path, "compressor.zip")
    with zipfile.ZipFile(des_dir_name, "w") as dest_file:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            # as we only want the file name as the filename
            dest_file.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    zip_creator(["test1.py", "test2.py"], "")
