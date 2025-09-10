import sys
import os
from PIL import Image

# Optional: GUI folder pickers if no args given
def pick_dirs_with_gui():
    try:
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        in_dir = filedialog.askdirectory(title="Select input folder (JPG/JPEG)")
        if not in_dir:
            return None, None
        out_dir = filedialog.askdirectory(title="Select output folder (PNG)")
        if not out_dir:
            return None, None
        return in_dir, out_dir
    except Exception:
        return None, None

# 1) Get input/output directories from args or GUI prompts
if len(sys.argv) >= 3:
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
else:
    # Try GUI pickers; if canceled, show usage and exit
    input_dir, output_dir = pick_dirs_with_gui()
    if not input_dir or not output_dir:
        print("Usage: python JPGtoPNGconverter.py <input_folder> <output_folder>")
        sys.exit(1)

# 2) Validate and prepare output folder
if not os.path.isdir(input_dir):
    print(f"Input folder not found: {input_dir}")
    sys.exit(1)

os.makedirs(output_dir, exist_ok=True)

# 3) Convert images
valid_exts = {".jpg", ".jpeg", ".JPG", ".JPEG"}
converted = 0
skipped = 0

for filename in os.listdir(input_dir):
    file_path = os.path.join(input_dir, filename)
    if not os.path.isfile(file_path):
        continue

    name, ext = os.path.splitext(filename)
    if ext not in valid_exts:
        skipped += 1
        continue

    try:
        with Image.open(file_path) as img:
            # Ensure RGB so JPEGs with no alpha save cleanly as PNG
            if img.mode in ("RGBA", "RGB", "L"):
                pass
            else:
                img = img.convert("RGB")

            save_path = os.path.join(output_dir, f"{name}.png")
            img.save(save_path, "PNG")
            print(f"Converted: {filename} -> {save_path}")
            converted += 1
    except Exception as e:
        print(f"Skipping {filename}: {e}")
        skipped += 1

print(f"All done! Converted {converted} file(s). Skipped {skipped}.")
