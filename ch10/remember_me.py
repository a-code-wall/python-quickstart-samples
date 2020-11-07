import json

# username = input("What is your name? ")

# filename = 'username.json'
# with open(filename, 'w') as f_obj:
# 	json.dump(username, f_obj)
# 	print("We'll remember you when you come back, " + username + "!")

# 如果以前存储了用户名, 就加载它
# 否则, 就提示用户输入用户名并存储它
# filename = 'username.json'
# try:
# 	with open(filename) as f_obj:
# 		username = json.load(f_obj)
# except FileNotFoundError:
# 	username = input("What is your name? ")
# 	with open(filename, 'w') as f_obj:
# 		json.dump(filename, f_obj)
# 		print("We'll remember you when you come back, " + username + "!")
# else:
# 	print("Welcome back, " + username + "!")

# 重构
def get_stored_username():
	"""如果存储了用户名, 就获取它"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""提示用户输入用户名"""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	"""问候用户, 并指出其名字"""
	username = get_stored_username()
	if username:
		active = True
		while active:
			result = input("are you sure this username ? (Y/N)")
			if result == 'N':
				get_new_username()
				active = False
			elif result == 'Y':
				active = False
				print("Welcome back, " + username + "!")		
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")

greet_user()