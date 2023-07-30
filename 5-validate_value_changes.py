import os
import subprocess
import yaml

def validate_and_update_values(file_path, keys):
    if not os.path.isfile(file_path):
        print(f"The file '{file_path}' does not exist in the current directory.")
        return

    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)
            return

    if any(key not in data for key in keys):
        print("Validation failed. Some keys are missing in the YAML file.")
        return

    try:
        cmd = f"yq eval '.replicaCount = 3 | .serviceName = \"mynginx\" | .image = \"nginx:1.18.0\"' -i {file_path}"
        subprocess.run(cmd, shell=True, check=True)
        print("YAML file has been updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Command '{e.cmd}' returned non-zero exit status '{e.returncode}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

keys_to_check = ['replicaCount', 'serviceName', 'image']
yaml_file_path = 'values.yaml'
validate_and_update_values(yaml_file_path, keys_to_check)

