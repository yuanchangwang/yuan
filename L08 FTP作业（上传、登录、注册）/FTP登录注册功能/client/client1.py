import socket
import json


sk = socket.socket()
sk.connect(('127.0.0.1', 9000))


# 注册、登录
def auth(opt):
    username = input('请输入用户名：').strip()
    password = input('请输入密码：').strip()
    dic = {'username': username, 'password': password, 'operate': opt}
    # 把用户名密码和操作发送给服务端
    str_dic = json.dumps(dic)  # json是把字典序列化成一个 字符串
    print(str_dic, type(str_dic))  # {"username": "yang", "password": "123", "operate": "register"} <class 'str'>
    sk.send(str_dic.encode())

    # 接收返回结果，登录和注册的状态
    res = sk.recv(1024)
    print(res.decode())


res = input('1.注册  2.登录  3.退出\n请选择：').strip()
if res == '1':
    auth('register')
elif res == '2':
    auth('login')
elif res == '3':
    print('bye~')


sk.close()
