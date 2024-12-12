import argparse
import os
import UUID_namer

parser = argparse.ArgumentParser("UUID Namer")
parser.add_argument("--dir", nargs=1, help="directory of files to rename as UUIDs")
parser.add_argument("--force", action="store_true", help="force renaming even when existing name is compliant")
args = parser.parse_args()

is_force = args.force
if os.path.isdir(args.dir[0]):
    root = args.dir[0]
    print(f"Process root {root}")
    UUID_namer.process_dir(root, is_force)
else:
    raise Exception("Root is not a valid directory")