import zipfile


def extractfile(zip_file, pwd):
    try:
        zip_file.extractall(pwd=bytes(pwd, "utf8"))
        print(pwd)
    except:
        print(pwd)
        pass


def main():
    zip_file = zipfile.ZipFile(
        r'C:\Users\86138\Downloads\Compressed\pycharm.zip', 'r')
    pwd_list = open('password.txt')
    for i in pwd_list.readline():
        pwd = i.strip('\n')
        extractfile(zip_file=zip_file, pwd=pwd)


if __name__ == '__main__':
    main()
