# 汽车租赁
ask = "Hello, What are you want a car ?"
car = input(ask)
print("Let me see if I can find you a " + car)

# 餐馆订位
aks = "How many people eat ?"
number = input(aks)
if 8 <= int(number):
	print("有空桌")
else:
	print("没有空桌")

# 10的整数倍
message = "Please input a number"
number = input(message)
flag = int(number) % 10 == 0
if flag:
	print("数字是10的整数倍")
else:
	print("数字不是10的整数倍")

# 披萨配料
active = True
message = "请输入披萨配料:"
while active:
	value = input(message)
	if value != 'quit':
		print(value)
	elif value == 'quit':
		active = False

# 电影票
ask = "您的年龄是?"
active = True
while active:
	age_str = input(ask)
	if age_str == 'quit':
		break
	age_num = int(age_str)
	if age_num < 3:
		print("免费")
	elif 3 <= age_num <= 12:
		print("10美元")
	else:
		print("15美元")

# 熟食店
sandwich_orders = ['培根三明治', '鸡蛋三明治', '草莓三明治']
finished_sandwiches = []
while sandwich_orders:
	sandwish = sandwich_orders.pop();
	print("I made your " + sandwish)
	finished_sandwiches.append(sandwish)
print(finished_sandwiches)

# 五香烟熏牛肉
sandwich_orders = ['培根三明治', '鸡蛋三明治', '草莓三明治', '牛肉三明治', '培根三明治']
print("熟食店的五香烟熏牛肉卖完了")
while '草莓三明治' in sandwich_orders:
	sandwich_orders.remove('草莓三明治')
print(sandwich_orders)

# 梦想的度假胜地
ask = "If you could visit one place in the world, where would you go?"
results = {}
active = True
while active:
	name = input("Hello, What's your name? ")
	place = input(ask)
	results[name] = place
	flag = input("continue ? (yes/no)")
	if flag == 'no':
		active = False
print(results)

