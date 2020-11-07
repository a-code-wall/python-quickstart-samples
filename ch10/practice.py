# Python 学习笔记
filename = 'learning_python.txt'

with open(filename) as file_object:
	# 第一次
	content = file_object.read()
	print(content)
	# 第二次
	for line in file_object:
		print(line)
	# 第三次
	lines = file_object.readlines()
for line in lines:
	print(line)

# C语言学习笔记
with open(filename) as file_object:
	for line in file_object:
		line = line.replace('Python', 'C')
		print(line)

# 访客
filename = 'guest.txt'
with open(filename, 'w') as file_object:
	name = input("please input you name: ")
	file_object.write(name + "\n")

# 访客名单
filename = 'guest_book.txt'
with open(filename, 'w') as file_object:
	while True:
		name = input("wellcome, what's your name? ")
		print("hello, " + name.title())
		file_object.write("new guest: " + name + "\n")

# 加法运算
try:
	first_number = input('please input your first number: ')
	second_number = input('please input your second number: ')
	f = int(first_number)
	s = int(second_number)
except ValueError:
	print("input error, please try again.")
else:
	result = f + s
	print(result)

# 加法计算器
print("Enter 'q' at any time to quit.\n")
while True:
	try:
		first_number = input('please input your first number: ')
		if first_number == 'q':
			break
		second_number = input('please input your second number: ')
		if second_number == 'q':
			break
		f = int(first_number)
		s = int(second_number)
	except ValueError:
		print("input error, please try again.")
	else:
		result = f + s
		print(result)

# 猫和狗
first_file_name = 'cats.txt'
second_file_name = 'dogs.txt'
file_list = []
file_list.append(first_file_name)
file_list.append(second_file_name)
try:
	for filename in file_list:
		with open(filename) as file_object:
			str = file_object.read()
			print(str)
except FileNotFoundError:
	print("sorry, file not fount.")

# 沉默的猫和狗
first_file_name = 'cats.txt'
second_file_name = 'dogs.txt'
file_list = []
file_list.append(first_file_name)
file_list.append(second_file_name)
try:
	for filename in file_list:
		with open(filename) as file_object:
			str = file_object.read()
			print(str)
except FileNotFoundError:
	pass

# 喜欢的数字
import json
filename = 'favorite_number.json'

def dump_number():
	try:
		favorite_number = input("what is your favorite number? ")
		with open(filename, 'w') as f_obj:
			json.dump(favorite_number, f_obj)
			print("save success!")
	except FileNotFoundError:
		print("sorry, file not found!")
def load_number():
	try:
		with open(filename) as f_obj:
			favorite_number = json.load(f_obj)
			print("I know your favorite number! It's " + favorite_number)
	except FileNotFoundError:
		print("sorry, file not found!")

dump_number()
load_number()

# 记住喜欢的数字
import json
filename = 'favorite_number.json'
def remember_favorite_number():
	try:
		with open(filename) as f_obj:
			favorite_number = json.load(f_obj)
			print("I know your favorite number! It's " + favorite_number)
	except FileNotFoundError:
		favorite_number = input("what is your favorite number? ")
		with open(filename, 'w') as f_obj:
			json.dump(favorite_number, f_obj)

remember_favorite_number()
remember_favorite_number()