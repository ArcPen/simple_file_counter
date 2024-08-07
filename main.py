from pathlib import Path

def count_folder_tree(path, indent=0):
    if indent == 0:
        print("===", path.name, len(list(path.iterdir())))
    for item in path.iterdir():
        if item.is_dir():
            print(" " * indent, item.name, len(list(item.iterdir())))
            count_folder_tree(item, indent+4)
        else:
            # print(" " * indent, item.name)
            pass

if __name__ == "__main__":
    count_folder_tree(Path("."))
  
