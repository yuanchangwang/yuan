# 1. 用户名不能重复
# 2. 输入2次密码，密码正确才能注册
# 3. 用户名和密码不能有空字符
# 用户名|密码
# 注册
"""
with open('user_info.txt', mode='a+', encoding='utf-8') as f1:
    user_list = []
    sign = True
    while sign:
        username = input('请输入用户名：')
        if username == '' or ' ' in username:
            print('用户名不合法，不能有空字符')
            continue
        f1.seek(0)
        res = f1.readlines()
        # print(res)
        for i in res:
            user, pwd = i.strip().split('|')
            user_list.append(user)
        # print(user_list)
        if username in user_list:
            print('该用户名已注册，请重新输入！')
        else:
            # 可以注册
            while 1:
                password = input('请输入密码(按q退出)：')
                if password == '' or ' ' in password:
                    print('密码不能有空字符')
                    continue
                password2 = input('请再次输入密码(按q退出)：')
                if password == password2:
                    print('注册成功')
                    user_var = username + '|' + password
                    f1.write(user_var + '\n')
                    sign = False
                    break
                elif password.upper() == 'Q' or password2.upper() == 'Q':
                    break
                else:
                    print('两次密码不一致，请重新输入')
"""

# 1. 输入3次密码，不正确的话拉入黑名单
# 2. 如果是黑名单用户，不准登录
# 登录 方法1
"""
with open('user_info.txt', mode='r', encoding='utf-8') as f1, \
        open('black.txt', mode='a+', encoding='utf-8') as f2:
    user_list = []
    pwd_list = []
    black_list = []
    res = f1.readlines()
    # 取到每个用户名和每个密码
    for i in res:
        user, pwd = i.strip().split('|')
        user_list.append(user)
        pwd_list.append(pwd)
    f2.seek(0)
    res1 = f2.readlines()
    # 取到黑名单的用户名
    for i in res1:
        black_list.append(i.strip())
    sign = True
    while sign:
        username = input('请输入用户名(按q退出)：').strip()
        if username in black_list:
            print('该用户已被冻结，请联系管理员')
            continue
        elif username.upper() == 'Q':
            break
        if username in user_list:
            user_index = user_list.index(username)
            pwd = pwd_list[user_index]
            count = 3
            while count:
                count -= 1
                password = input('请输入密码：').strip()
                if password == pwd:
                    print('登录成功')
                    sign = False
                    break
                elif count == 0:
                    print('密码错误3次，该用户被冻结')
                    f2.write(username + '\n')
                else:
                    print('密码错误，还剩%d次机会' % count)
        else:
            print('该用户不存在，请重新输入')
"""


# 方法二
# 注册
"""
with open('user_info.txt', mode='a+', encoding='utf-8') as f1:
    user_list = []
    sign = True
    while sign:
        username = input('请输入用户名：')
        if username == '' or ' ' in username:
            print('用户名不合法，不能有空字符')
            continue
        f1.seek(0)
        res = f1.readlines()
        # print(res)
        for i in res:
            user, pwd = i.strip().split('|')
            user_list.append(user)
        # print(user_list)
        if username in user_list:
            print('该用户名已注册，请重新输入！')
        else:
            # 可以注册
            while 1:
                password = input('请输入密码(按q退出)：')
                if password == '' or ' ' in password:
                    print('密码不能有空字符')
                    continue
                password2 = input('请再次输入密码(按q退出)：')
                if password == password2:
                    print('注册成功')
                    user_var = username + '|' + password + '|' + '1'
                    f1.write(user_var + '\n')
                    sign = False
                    break
                elif password.upper() == 'Q' or password2.upper() == 'Q':
                    break
                else:
                    print('两次密码不一致，请重新输入')
"""
# 登录
"""
with open('user_info1.txt', mode='r+', encoding='utf-8') as f1:
    user_list = []
    pwd_list = []
    black_list = []
    res = f1.readlines()
    # 取到每个用户名和每个密码
    for i in res:
        print(i)
        user, pwd, black = i.strip().split('|')
        user_list.append(user)
        pwd_list.append(pwd)
        black_list.append(black)
    sign = True
    while sign:
        username = input('请输入用户名(按q退出)：').strip()
        if username.upper() == 'Q':
            break
        if username in user_list:
            user_index = user_list.index(username)
            pwd = pwd_list[user_index]
            is_black = black_list[user_index]
            if is_black == '0':
                print('该用户已被冻结，请联系管理员')
                continue
            count = 3
            while count:
                count -= 1
                password = input('请输入密码：').strip()
                if password == pwd:
                    print('登录成功')
                    sign = False
                    break
                elif count == 0:
                    print('密码错误3次，该用户被冻结')
                    # print(repr(res[user_index]))
                    res[user_index] = res[user_index].strip()
                    res[user_index] = res[user_index][:-1] + '0\n'
                    f1.seek(0)
                    f1.writelines(res)
                else:
                    print('密码错误，还剩%d次机会' % count)
        else:
            print('该用户不存在，请重新输入')
"""
