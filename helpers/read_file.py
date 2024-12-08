def read_file(file_name):
    with open(file_name, "r") as f:
        content = f.read()
    return content.split("\n")
