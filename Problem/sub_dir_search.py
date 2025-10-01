import os

def search(dirname):
    filename = os.listdir(dirname)
    for filename in filename:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1]
        if ext == '.py':
            print(full_filename)
    
search("/Users")  # Mac