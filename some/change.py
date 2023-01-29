import images

if __name__ == '__main__':
    print("bingimages:1\nrandomimages:2")
    change_input = int(input("请输入:"))
    if bool(change_input - 1):
        images.change_random()
    else:
        images.change_bing()
