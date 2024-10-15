import os


def create_bd_file(path, name):
    full_path = os.path.join(path, name)

    if not os.path.exists(full_path):
        os.makedirs(full_path)
        return True, f"Folder was  '{name}' create on '{path}'"
    else:
        return False, f"Folder '{name}' already exists on '{path}'"
