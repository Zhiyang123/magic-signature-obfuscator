import os
import sys

# Dictionary of magic signatures with their respective byte lengths
MAGIC_SIGNATURES = {
    "exe": b"\x4D\x5A\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xFF\xFF\x00\x00\xB8\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00",          # EXE signature (16 bytes)
    "php": b"\x3C\x3F\x70\x68\x70",  # PHP signature (5 bytes)
    "jpg": b"\xFF\xD8\xFF\xE0",  # JPEG signature (4 bytes)
    "png": b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0d\x49\x48\x44\x52\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x9A\x99\x9A\x00\x00\x00\x00\x00\x00\x00\x00",  # PNG signature (40 bytes)
    "gif": b"\x47\x49\x46\x38",  # GIF signature (4 bytes)
}

ascii_art = """
__  __             _         ___  _      __                     _             
|  \/  | __ _  __ _(_) ___   / _ \| |__  / _|_   _ ___  ___ __ _| |_ ___  _ __ 
| |\/| |/ _` |/ _` | |/ __| | | | | '_ \| |_| | | / __|/ __/ _` | __/ _ \| '__|
| |  | | (_| | (_| | | (__  | |_| | |_) |  _| |_| \__ \ (_| (_| | || (_) | |   
|_|  |_|\__,_|\__, |_|\___|  \___/|_.__/|_|  \__,_|___/\___\__,_|\__\___/|_|   
              |___/                                                            
Author: Zhi Yang
              """

def change_magic_signature(file_path, target_signature, output_file_path):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return

    # Get the target magic signature and its length
    new_signature = MAGIC_SIGNATURES[target_signature]
    
    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        # Read the entire content of the file
        original_content = file.read()
    
    # Prepend the new magic signature to the original content
    new_content = new_signature + original_content
    
    # Write the updated content back to the file without overwriting the original bytes
    with open(output_file_path, 'wb') as file:
        file.write(new_content)

    print(f"Magic signature changed successfully to {target_signature}.")

if __name__ == "__main__":
    print(ascii_art)
    # Check if the correct number of arguments is passed
    if len(sys.argv) != 4:
        print("Usage: python script.py <file_path> <target_signature> <output_file_path>")
        print("Available signatures: exe, php, jpg, png, gif")
        sys.exit(1)

    # Get the file path and the target signature from the arguments
    file_path = sys.argv[1]
    target_signature = sys.argv[2].lower()
    output_file_path = sys.argv[3]

    # Check if the target signature is supported
    if target_signature not in MAGIC_SIGNATURES:
        print(f"Error: Unsupported target signature '{target_signature}'.")
        print("Available signatures: exe, php, jpg, png, gif")
        sys.exit(1)

    # Change the magic signature
    change_magic_signature(file_path, target_signature, output_file_path)

