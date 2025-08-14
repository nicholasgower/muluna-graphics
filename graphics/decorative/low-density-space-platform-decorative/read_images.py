import os
from PIL import Image

def is_image_file(filename):
    ext = filename.lower().rsplit('.', 1)[-1]
    return ext in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp', 'tiff']
def is_python_or_lua(filename):
    ext = filename.lower().rsplit('.', 1)[-1]
    return ext in ['py', 'lua']

def generate_lua_filelist(folder_path, lua_filename="img_list.lua"):
    filenames = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    filenames.sort()

    lua_lines = ["return {"]
    for name in filenames:
        full_path = os.path.join(folder_path, name)
        if is_image_file(name):
            try:
                with Image.open(full_path) as img:
                    width, height = img.size
                    lua_lines.append(f'    ["{name}"] = {{"{name}", {width}, {height}}},')
            except Exception as e:
                print(f"Warning: Could not read image '{name}': {e}")
        elif not is_python_or_lua(name):
            lua_lines.append(f'    ["{name}"] = "{name}",')
    lua_lines.append("}")

    lua_path = os.path.join(folder_path, lua_filename)
    with open(lua_path, 'w', encoding='utf-8') as lua_file:
        lua_file.write('\n'.join(lua_lines))

    print(f"Lua file list saved to: {lua_path}")

# Example usage
if __name__ == "__main__":
    # folder = input("Enter the path to the folder: ").strip()
    generate_lua_filelist(os.getcwd())