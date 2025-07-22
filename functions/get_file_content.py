import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not file_path.startswith(working_dir_abs + os.sep):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(file_path, 'r+', encoding='utf-8') as f:
            content = f.read(MAX_CHARS + 1)

            if len(content) > MAX_CHARS:
                snippet = content[:MAX_CHARS]
                msg = f'[...File "{file_path}" truncated at 10000 characters]'
                return snippet + msg

        return content
    except Exception as e:
        return f"Error: {e}"

