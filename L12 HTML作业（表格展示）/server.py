import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9002))
sk.listen(5)

while 1:
    conn, addr = sk.accept()

    data = conn.recv(1024)
    print('data:', data)

    data = data.decode()
    info = data.split('\r\n\r\n')[1]  # 取到浏览器提交过来的数据（用户名和密码）
    if info:
        user_info, pwd_info = info.split('&')
        user = user_info.split('=')[1]  # 取到用户名
        pwd = pwd_info.split('=')[1]  # 取到密码
        """下面就可以写注册的逻辑代码，比如说判断该用户是否存在，不存在则写入到用户名文件中"""
        ...

    with open('register.html', 'rb') as f:
        res = f.read()
    conn.send(b'HTTP:/1.1 200 OK\r\n\r\n' + res)
