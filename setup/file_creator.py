import os


def create_python_file(file_name, day_number, file_type, contents=None):
    path_components = ["..", file_type, f"day{day_number:02d}"]
    create_file(file_name, path_components, contents)


def create_test_data_file(day_number, file_name):
    path_components = ["..", "tests", f"day{day_number:02d}", "data"]
    create_file(file_name, path_components)


def create_file(file_name, path_components, contents=None):
    script_dir = os.path.dirname(__file__)
    file_dir = os.path.join(script_dir, *path_components)
    os.makedirs(file_dir, exist_ok=True)
    file_path = os.path.join(script_dir, file_dir, file_name)
    print(f"Creating file {file_path}")
    with open(file_path, "w") as f:
        if contents:
            f.write(contents)
