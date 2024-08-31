import os
import subprocess
import sys
import re
import shutil

def check_folder_exists(folder_path):
    # Check if the folder is present
    return os.path.exists(folder_path)

def is_steam_running():
    try:
        # Quick check if Steam currently running
        result = subprocess.run(['pgrep', '-x', 'steam'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # If the return code is 0, steam is running
        return result.returncode == 0
    except Exception as e:
        print(f"Error checking Steam status: {e}")
        sys.exit(1)

def delete_folder(folder_path):
    # Delete the Cache dir
    try:
        shutil.rmtree(folder_path)
        print("Folder deleted successfully.")
    except Exception as e:
        print(f"Error deleting folder: {e}")
        sys.exit(1)

def check_precaching_disabled(config_file_path):
    # Checking if the User really disabled pre-caching
    if not os.path.exists(config_file_path):
        print("Steam configuration file not found.")
        return False

    with open(config_file_path, 'r') as file:
        config_content = file.read()

    # Use regex to find the ShaderPreCaching setting
    match = re.search(r'"ShaderPreCaching"\s*"(\d+)"', config_content)
    if match:
        value = match.group(1)
        if value == "0":
            print("Shader Pre-Caching is already disabled.")
            return True
        else:
            print("Shader Pre-Caching is currently enabled. Please disable it in your Steam settings and run this script again.")
            return False
    else:
        print("Shader Pre-Caching setting not found in the configuration file.")
        return False

def main():
    # Path to the shader cache folder
    shader_cache_folder = os.path.expanduser("~/.local/share/Steam/steamapps/shadercache/1172470")
    config_file_path = os.path.expanduser("~/.local/share/Steam/config/config.vdf")
    
    # Check if the folder exists
    if not check_folder_exists(shader_cache_folder):
        print("The specified folder does not exist.")
        sys.exit(0)
    
    # Check if Steam is running
    if is_steam_running():
        print("Steam is currently running. Please close Steam and run this script again.")
        sys.exit(1)
    
    # Check if Shader Pre-Caching is disabled
    if not check_precaching_disabled(config_file_path):
        # Exit the script if Shader Pre-Caching is enabled
        sys.exit(1)
    
    # Delete the folder
    delete_folder(shader_cache_folder)
    
    # Notify the user
    print("Your APEX Pre-Shader Cache has been wiped! Log in to your Steam account and download the available pre-shader.")

if __name__ == "__main__":
    main()
