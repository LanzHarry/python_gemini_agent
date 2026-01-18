import os

def get_files_info(working_directory, directory="."):
    try:
        # validate path to directory is inside working directory
        working_dir_abs = os.path.abspath(working_directory)

        # construct full path from abs path and relative path
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        # check if target_dir falls within working_dir_abs to working directory
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    except Exception as e:
        return f"Error checking working and target directory: {e}"

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    try:
        dir_contents = os.listdir(target_dir)
    except FileNotFoundError:
        return f'Error: "{target_dir}" not found'
    except NotADirectoryError:
        return f'Error: "{target_dir}" is not a directory'
    except PermissionError:
        return f'Error: Program does not have permission to access "{target_dir}"' 

    dir_contents_string = ""
    
    for elt in dir_contents:
        try:
            elt_path = os.path.join(target_dir, elt) 
            fsize = os.path.getsize(elt_path) 
            is_dir = os.path.isdir(elt_path)
            dir_contents_string += f"- {elt}: file_size={fsize}, is_dir={is_dir}\n"
        except Exception as e:
            return f'Error: {str(e)}'

    return dir_contents_string
