import os
import json
import sys

def get_device_info(uuid, devices):
    # Look for the device info with a given UUID
    for device in devices:
        if device["uuid"] == uuid:
            return device["name"], device["cameraID"]
    return None, None

def get_take_info(uuid, scenes):
    # Look for the take info with a given UUID
    for scene in scenes:
        for take in scene["takes"]:
            if take["uuid"] == uuid:
                # Handle calibration takes separately
                if scene["type"] == 0: 
                    return f"calibration_{take['name']}".lower()
                else:
                    return take["name"].lower()
    return None

def rename_files(directory, json_file):
    with open(json_file) as f:
        # Fetches the first session data
        session_data = json.load(f)["project"]["sessions"][0]
        devices = session_data["peers"]
        scenes = session_data["scenes"]

        # Iterate through each .mov file in the directory
        for original_filename in os.listdir(directory):
            if original_filename.endswith(".mov"):
                # Remove the .mov extension and split the filename into 3 uuids
                filename = original_filename[:-4]  
                uuids = filename.split("_")[0:3] 

                device_name, camera_id = get_device_info(uuids[1], devices)
                take_name = get_take_info(uuids[2], scenes)
                # Replace spaces with underscores
                take_name = take_name.replace(" ", "") 

                if device_name and take_name:
                    new_name = f"cam{camera_id}_{take_name}.mov"

                    # Check if file with new_name already exists
                    suffix = 1
                    while os.path.exists(os.path.join(directory, new_name)):
                        base, extension = os.path.splitext(new_name)
                        new_name = f"{base}_{suffix}{extension}"
                        suffix += 1

                    print(f"Renaming {original_filename} to {new_name}")
                    os.rename(
                        os.path.join(directory, original_filename),
                        os.path.join(directory, new_name),
                    )
                else:
                    print(f"Could not find matching data for {filename}")


if __name__ == "__main__":
    # Check for correct command line arguments
    if len(sys.argv) != 3:
        print("Usage: python rename.py directory session.json")
        sys.exit(1)
    rename_files(sys.argv[1], sys.argv[2])
