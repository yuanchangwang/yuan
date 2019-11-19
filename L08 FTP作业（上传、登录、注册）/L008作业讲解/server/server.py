import socketserver
import struct
import json
import os

# 获取当前文件的路径
# 获取当前文件所在的文件夹路径
file_path = os.path.dirname(__file__)


class FTPServer(socketserver.BaseRequestHandler):
    def handle(self):
        # 先接收4个的字节的文件实际大小
        dic_len1 = self.request.recv(4)
        dic_len = struct.unpack('i', dic_len1)[0]
        # 通过文件的实际大小来接收
        dic_info = self.request.recv(dic_len)
        dic_str = dic_info.decode('utf-8')
        dic_info = json.loads(dic_str)
        print(dic_info)

        # 给传过来的文件名拼接完整的路径
        file_abspath = os.path.join(file_path, dic_info['filename'])

        with open(file_abspath, 'wb') as f:
            size = dic_info['filesize']
            while dic_info['filesize']:
                content = self.request.recv(1024 * 10)
                f.write(content)
                dic_info['filesize'] -= len(content)
                print('\r传输中%s>%.2f%%' % ('=' * int((size - dic_info['filesize']) / size * 100),
                                            (size - dic_info['filesize']) / size * 100), end='')
            print()
            print('文件接收完毕')


my_server = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), FTPServer)
my_server.serve_forever()  # 重复调用
