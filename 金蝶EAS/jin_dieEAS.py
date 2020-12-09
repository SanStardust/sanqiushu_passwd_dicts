# python 3.9
# windows
# 如果遇到什么gbk报错啥的,把你的字典用记事本打开另存为UTF-8即可

def write_to_file(passwd_list_):
    with open("F:\\weakpass_dict\\0.7.jin_dieEAS.txt", "a") as f_:
        for _ in passwd_list_:
            f_.write(_ + "\n")


with open("F:\\weakpass_dict\\0.7.txt", "r") as f:
    lines = f.readlines()  # 全部读到内存里去, 没有大内存能搞好安全吗?
    number = 0
    passwd_list = []
    for i in lines:  # 遍历字典
        passwd = ""
        for j in i[:-1]:  # 不要尾部的回车换行 # %2C61%2C62%2C63%2C64%2C65%2C66
            passwd += "%2C" + str(oct(ord(j)))[2:]  # 对每个密码进行变换
        passwd_list.append(passwd)
        number += 1
        if number == 1000:  # 1千个密码写一次文件, 嗯, 考虑到文件读写比较慢(( • ̀ω•́ )✧)
            write_to_file(passwd_list)
            number = 0
            passwd_list = []
    write_to_file(passwd_list)

#  如果你有幸找到密码了可以用这个解码
"""
a = "%2C120%2C100%2C163%2C163%2C167%2C60%2C162%2C144"
b = a.split("%2C")[1:]

print(b)
c = ""
for i in b:
    c += chr(int(i, 8))
print(c)
"""