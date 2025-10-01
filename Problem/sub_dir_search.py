import os

def search(dirname):
    try:
        filename = os.listdir(dirname)
        for filename in filename:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass
    
search("/Users")  # Mac