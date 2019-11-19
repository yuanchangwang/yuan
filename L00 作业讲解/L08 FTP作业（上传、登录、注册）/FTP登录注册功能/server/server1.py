import json
import os
import socketserver
import hashlib

# 获取当前文件的路径
path = os.path.dirname(__file__)
# 把用户信息表的路径拼接上去
user_path = os.path.join(path, 'db', 'user_info.txt')


class Auth:
    # 通过hashlib动态加密密码
    @classmethod
    def md5(cls, user, pwd):
        # 先实例化一个md5的对象，通过用户名加盐
        md5_obj = hashlib.md5(user.encode())
        # 这个对象调用update方法给密码加密
        md5_obj.update(pwd.encode())
        # 返回加密的字符串
        return md5_obj.hexdigest()

    # 注册的方法
    @classmethod
    def register(cls, opt_dic):
        with open(user_path, mode='a+', encoding='utf-8') as f:
            """用户信息文件：  用户名|密码  """
            f.seek(0)
            for line in f:
                user = line.split('|')[0]
                if user == opt_dic['username']:
                    return '该用户名已存在'
            # cls.md5(opt_dic['username'], opt_dic['password']) 调用md5的方法加密密码
            f.write('%s|%s\n' % (opt_dic['username'], cls.md5(opt_dic['username'], opt_dic['password'])))
            return '注册成功'

    # 登录的方法
    @classmethod
    def login(cls, opt_dic):
        with open(user_path, mode='r', encoding='utf-8') as f:
            for line in f:
                user, pwd = line.strip().split('|')
                # cls.md5(opt_dic['username'], opt_dic['password']) 调用md5的方法加密密码
                if user == opt_dic['username'] and pwd == cls.md5(opt_dic['username'], opt_dic['password']):
                    return '登录成功'
            else:
                return '用户名或者密码错误'


class FTPServer(socketserver.BaseRequestHandler):
    def handle(self):
        opt_dic = self.my_recv()
        print(opt_dic)

        # 方法一：
        # if opt_dic['operate'] == 'register':
        #     # 这是注册操作
        #     res = Auth.register(opt_dic)
        #     self.my_send(res)
        # elif opt_dic['operate'] == 'login':
        #     # 这是登录操作
        #     res = Auth.login(opt_dic)
        #     self.my_send(res)

        # 方法二：
        # 通过反射区分登录还是注册
        # if hasattr(Auth, opt_dic['operate']):
        #     # 调用getattr返回一个对象
        #     obj = getattr(Auth, opt_dic['operate'])
        #     print(obj)
        #     # 调用这个对象执行登录或者注册方法
        #     res = obj(opt_dic)
        #     print(res)
        #     # 把结果返回给客户端
        #     self.my_send(res)

        # 简化版
        if hasattr(Auth, opt_dic['operate']):
            res = getattr(Auth, opt_dic['operate'])(opt_dic)
            self.my_send(res)

    # 收消息的方法
    def my_recv(self):
        res = self.request.recv(1024)
        str_dic = res.decode()
        return json.loads(str_dic)  # 快捷导入模块  Alt + Enter ，选择要导包的模块名，再按回车即可

    # 发消息的方法
    def my_send(self, info):
        self.request.send(info.encode())


myServer = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), FTPServer)
myServer.serve_forever()  # 循环调用
