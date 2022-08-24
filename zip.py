import time
string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 这里加上你想要的字符
stm = time.time()
with open('password.txt', 'a') as dic:  # 在当前目录生成password.txt文件
    for a in range(len(string)):
        for b in range(len(string)):
            for c in range(len(string)):
                for d in range(len(string)):
                    pwd = string[a]+string[b]+string[c]+string[d]  # 生成4位数字字母密码
                    dic.write(pwd)
                    dic.write('\n')
                    print('密码正在写入文件：', pwd)
ent = time.time()
print('成功生成密码本！用时%f分' % ((ent-stm)/60))
