import os
import uuid
import re

expression = "[a-fA-F0-9]{32}"
p = re.compile(expression, re.IGNORECASE)

ingore_ext = [".db", ".md"]

def gen_uuid():
    u = uuid.uuid4().hex
    c = u.replace("-", "")
    return c


# unused for now
def is_collection_dir(dir):
    for o in os.listdir(dir):
        item = os.path.join(dir,o)
        if os.path.isfile(item):
            return o == ".collection"
        
        
def is_file_valid_uuid(file):
    basename = os.path.basename(file)
    return p.match(basename)


def process_file(file, is_force):
    if not is_file_valid_uuid(file) or is_force:
        ext = os.path.splitext(file)[1]
        if ext in ingore_ext:
            return
        print(f"Fixing {file}")
        uuid_basename = gen_uuid()
        new_basename = uuid_basename+ext
        idx = file.find(os.path.basename(file))
        filepath = file[:idx]
        new_file = os.path.join(filepath,new_basename)
        os.rename(file, new_file)


def process_dir(dir, is_force):
    print(f"process_dir: {dir}")
    if is_force:
        print("Forcing rename")
    for o in os.listdir(dir):
        item = os.path.join(dir,o)
        if os.path.isfile(item):
            process_file(item, is_force)
        elif os.path.isdir(item):
            process_dir(item, is_force)
        else:
            print(f"{item} is a {type(item)}")




