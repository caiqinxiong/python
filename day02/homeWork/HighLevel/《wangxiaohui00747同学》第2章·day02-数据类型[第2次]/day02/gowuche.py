
# 作业：购物车
# 	1. 用户先给自己的账户充钱：比如先充3000元。
# 	2. 页面显示 序号 + 商品名称 + 商品价格，如：
# 		1 电脑 1999
# 		2 鼠标 10
# 		…
# 		n 购物车结算
# 	3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品。
#  	4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 	5. 用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。
# 	6. 用户输入Q或者q退出程序。
# 	7. 退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少。
commodityList = {
    "1": {
        "name": "电脑",
        "price": 1000
    },
    "2":{
        "name": "鼠标",
        "price": 10
    },
    "3":{
        "name": "充电器",
        "price": 99
    },
    "4":{
        "name": "数据线",
        "price": 35
    }
}
money = int(input("请充值："))
carList = {}
isAdd = True
print(commodityList)

while isAdd:
    serial = input("请选择商品序列号：")
    if not commodityList.get(serial):
        print("输入有误，并重新输入")
    else:
        print(commodityList.get(serial)["name"] + "：" + str(commodityList.get(serial)["price"]) + "元")
        if carList.get(serial):
            carList[serial]["数量"] += 1
        else:
            li = commodityList.get(serial)
            li["数量"] = 1
            carList[serial] = li
        isGo = input("是否继续添加：")
        if isGo == "n":
            print(carList)
            sum = 0
            for k,v in carList.items():
                sum = sum + v["数量"] * v["price"]
            while sum > money:
                delItem = input("余额不足，请删除部分商品：")
                if carList[delItem]["数量"] > 1:
                    carList[delItem]["数量"] -= 1
                else:
                    carList.pop(delItem)
                sum -= carList[delItem]["price"]
            money -= sum
            print("支付成功")
            isExit = input("是否退出：")
            if isExit.upper() == "Q":
                print("购物清单：",carList)
                print("消费金额：",sum)
                print("余额：", money)
                isAdd = False