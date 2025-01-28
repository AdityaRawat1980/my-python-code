def load_key():
    file= open("key.key","rb")
    key = file.read()
    file.close()
    return key