goods_list = [
    {"name": "电脑", 'price': 1999},
    {"name": "鼠标", 'price': 10},
    {"name": "游艇", 'price': 20},
    {"name": "美女", 'price': 998},
    {"name": "油精", 'price': 30},
]

# 初始金额
money = 0
# 购物车
car = {}
'''
car = {
    1: {"name": "电脑", 'price': 1999},
    2: {"name": "鼠标", 'price': 10},
    3: {"name": "游艇", 'price': 20},
    4: {"name": "美女", 'price': 998},
    5: {"name": "油精", 'price': 30},
}
'''


# 充钱
def chongqian():
    global money
    while 1:
        money1 = input('请输入您要充值的金额：').strip()
        if money1.isdigit():
            money1 = int(money1)
            money += money1
            print('您本次充值%d元，您的总金额有%d元' % (money1, money))
            break
        else:
            print('请输入正确的金额')


# 商品展示
def show_goods():
    print('[===========有如下商品供您选择：===========]')
    print('序号  商品名称  商品价格')
    for index, dic in enumerate(goods_list, start=1):
        print(index, dic['name'].rjust(8), str(dic['price']).rjust(9))


# 选项不存在
def error1():
    print('您输入的选项不存在')


# 超出范围
def error2():
    print('超出范围')


# 退出
def quie():
    global flag
    flag = False
    print('[===========欢迎下次光临===========]')


# 添加购物车
def add_car(sn):
    # 如果购物车内不存在，则创建一条记录
    if sn not in car:
        car[sn] = {
            'name': goods_list[sn - 1]['name'],
            'price': goods_list[sn - 1]['price'],
            'amount': 1
        }
    # 存在则数量加一
    else:
        car[sn]['amount'] += 1
    print('您成功将%s加入购物车，价格为%d元' % (car[sn]['name'], car[sn]['price']))


# 展示购物车明细
def show_car():
    total = 0
    print('[===========您的购物车明细如下===========]')
    print('序号  商品名称  商品价格  数量  商品总价')
    for k, dic in car.items():
        print(k, dic['name'].rjust(8), str(dic['price']).rjust(9), str(dic['amount']).rjust(6),
              str(dic['price'] * dic['amount']).rjust(8))
        total += dic['price'] * dic['amount']
    print('您的购物车总价格为%d元，您的余额为%d元' % (total, money))
    return total


# 购买的商品明细
def goods():
    print('[===========您购买的商品明细如下===========]')
    print('序号  商品名称  商品价格  数量  商品总价')
    for k, dic in car.items():
        print(k, dic['name'].rjust(8), str(dic['price']).rjust(9), str(dic['amount']).rjust(6),
              str(dic['price'] * dic['amount']).rjust(8))


# 删除商品
def del_goods():
    print('序号  商品名称  商品价格  数量  商品总价')
    for k, dic in car.items():
        print(k, dic['name'].rjust(8), str(dic['price']).rjust(9), str(dic['amount']).rjust(6),
              str(dic['price'] * dic['amount']).rjust(8))
    sn = input('请输入您要删除的商品序号：').strip()
    if sn.isdigit():
        sn = int(sn)
        if sn in car:
            car[sn]['amount'] -= 1
            if car[sn]['amount'] == 0:
                car.pop(sn)
        else:
            error2()
    else:
        error1()


# if __name__ == '__main__':
print('[===========欢迎光临===========]')
# 1. 充钱
chongqian()

flag = True
while flag:
    # 2. 商品展示
    show_goods()
    # 3. 开始购物
    sn = input('请输入您要购买的商品序号（按n结算，按q退出程序）：').strip()
    # 选择商品序号
    if sn.isdigit():
        sn = int(sn)
        if 0 < sn <= len(goods_list):
            # 添加到购物车
            add_car(sn)
        else:
            error2()
    # 结算
    elif sn.upper() == 'N':
        # 钱够了，可以结算
        while 1:
            if not car:
                print('您的购物车是空的')
                break
            total = show_car()
            res = input('按y确认购买，按c充值，按d删除商品，按q结束购物，按任意键返回购物页面').strip()
            if res.upper() == 'Y':
                if money - total >= 0:
                    goods()
                    print('购物成功，您本次消费%d元，还剩余%d元' % (total, money - total))
                    quie()
                    break

                # 钱不够，让用户删除一些商品
                else:
                    print('余额不足')
            # 充钱
            elif res.upper() == 'C':
                chongqian()
            # 删除商品
            elif res.upper() == 'D':
                del_goods()
            elif res.upper() == 'Q':
                quie()
                break
            else:
                break
    # 退出
    elif sn.upper() == 'Q':
        quie()
        break
    else:
        error1()
