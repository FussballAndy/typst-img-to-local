import sys
import pathlib
import os
import shutil

TEMPLATE_TYPST_TOML = """
[package]
name = "{}"
version = "0.1.0"
entrypoint = "lib.typ"
"""

TEMPLATE_LIB_TYP = """
#let image = image("{}")
"""

root_dir = None
if sys.platform.startswith("linux"):
    root_dir = pathlib.Path.home() / ".local/share/typst/packages/local"
elif sys.platform.startswith("win32"):
    root_dir = pathlib.Path.home() / "AppData/Roaming/typst/packages/local"
elif sys.platform.startswith("darwin"):
    root_dir = pathlib.Path.home() / "Library/Application Support/typst/packages/local"
else:
    print('Error: Unsupported platform')
    exit(0)

def file_exists(file: str) -> bool:
    return os.path.exists(file)

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        print("Usage: python install.py <logo file> <package name>")
        exit(0)
    logo_file = args[1]
    package_name = args[2]

    if not file_exists(logo_file) or not os.path.isfile(logo_file):
        print("Logo file does not exist. Aborting.")
        exit(0)
    
    package_dir = root_dir / package_name / "0.1.0"

    package_dir.mkdir(parents=True,exist_ok=True)

    with open(package_dir / "typst.toml", "w") as typst_toml:
        typst_toml.write(TEMPLATE_TYPST_TOML.format(package_name))

    with open(package_dir / "lib.typ", "w") as lib_typ:
        lib_typ.write(TEMPLATE_LIB_TYP.format(logo_file))

    shutil.copyfile(logo_file, package_dir / logo_file)

    print(f"Created local package at {package_dir}")
