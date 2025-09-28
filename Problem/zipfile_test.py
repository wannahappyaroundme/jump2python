import zipfile

with zipfile.ZipFile("test.zip", "w") as myzip:
    myzip.write("a.txt")
    myzip.write("b.txt")
    myzip.write("c.txt")

with zipfile.ZipFile("test.zip", "r") as myzip:
    myzip.extractall()