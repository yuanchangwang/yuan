import socket
import os
import struct
import json

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

print(__file__)  # 当前文件的完整路径

# 获取当前文件所在的文件夹路径
file_path = os.path.dirname(__file__)
# 拼接测试文件的绝对路径
file_abspath = os.path.join(file_path, '薛之谦 - 演员.flac')
print(file_abspath)
# 获取要发送的文件大小
filesize = os.path.getsize(file_abspath)
print(filesize)

# 1. 先把文件名和文件大小发过去
file_info = {'filename': '薛之谦 - 演员.flac', 'filesize': filesize}
# 通过json把字典序列化成字符串，然后在encode成字节流
dic_info = json.dumps(file_info).encode('utf-8')
# 通过struct模块把字典的长度转成4个字节
dic_len = struct.pack('i', len(dic_info))

# send只能发送字节流
sk.send(dic_len)
sk.send(dic_info)

# 2. 开始文件传输
with open(file_abspath, 'rb') as f:
    size = filesize
    while filesize:
        content = f.read(1024 * 10)
        sk.send(content)
        filesize -= len(content)

        """
        \r的作用是把后面的代码拉到前面，覆盖掉代码
        size: 文件的总大小
        filesize： 文件剩余的大小
        size-filesize： 文件传输的大小
        []里面一共可以放20个等号，我们用空格代表没传输的位置  
        """
        print('\r传输中[%s%s]%.2f%%' % ('=' * int((size-filesize) / size * 30),
                                        ' ' * (30 - int((size-filesize) / size * 30)),
                                        (size-filesize) / size * 100), end='')
    print()
    print('文件传输完毕')

sk.close()
