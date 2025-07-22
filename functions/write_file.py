import os


def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target = os.path.abspath(os.path.join(working_directory, file_path))

        if not target.startswith(working_dir_abs + os.sep):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        parent_dir = os.path.dirname(target)
        if parent_dir and not os.path.isdir(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)

        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
