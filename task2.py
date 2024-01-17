import shutil
import os
import datetime


def file_backup(source_paths, destination_):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder = os.path.join(destination_, f"backup_{timestamp}")

    # backup folder
    os.makedirs(backup_folder)

    for source_path in source_paths:
        base_name = os.path.basename(source_path)

        # Destination path
        dest_file = os.path.join(backup_folder, base_name)

        try:
            if os.path.isfile(source_path):
                shutil.copy2(source_path, dest_file)
                print(f"File '{base_name}' backed up successfully.")
            elif os.path.isdir(source_path):
                shutil.copytree(source_path, dest_file)
                print(f"Directory '{base_name}' backed up successfully.")
        except Exception as e:
            print(f"Error backing up '{base_name}': {str(e)}")


if __name__ == "__main__":
    # files or directories to back up
    source_paths = [
        r"C:\Users\srida\OneDrive\Desktop\Internship\python\phase1",
        r"C:\Users\srida\OneDrive\Desktop\CERTIFICATES",
        # Add more
    ]

    # estination path for the backup
    destination_ = r"C:\Users\srida\OneDrive\Desktop\1"

    # backup function
    file_backup(source_paths, destination_)
