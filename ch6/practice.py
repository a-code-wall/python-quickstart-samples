# 使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。
# 该字典应包含键 first_name 、 last_name 、 age 和 city 。
# 将存储在该字典中的每项信息都打印出来。
acquaintance = {
    'first_name': 'blues',
    'last_name': 'c',
    'age': '27',
    'city': 'qz',
}
print(acquaintance)

# 使用一个字典来存储一些人喜欢的数字。请想出 5 个人的名字，并将这些名字用作字典中的键;
# 想出每个人喜欢的一个数字，并将这些数字作为值存储在字典中。
# 打印每个人的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保数据是真实的。
favorite_numbers = {
	'zhangsan': 1,
	'lisi': 2,
	'wangwu': 3,
	'zhaoliu': 4,
	'sunqi': 5,
}
print("zhangsan love numeber is " + str(favorite_numbers['zhangsan']))
print("lisi love numeber is " + str(favorite_numbers['lisi']))
print("wangwu love numeber is " + str(favorite_numbers['wangwu']))
print("zhaoliu love numeber is " + str(favorite_numbers['zhaoliu']))
print("sunqi love numeber is " + str(favorite_numbers['sunqi']))

# 词汇表
# 想出你在前面学过的 5 个编程词汇，将它们用作词汇表中的键，
# 并将它们的含义作为值存储在词汇表中。
# 以整洁的方式打印每个词汇及其含义。
# 为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇的含义；
# 也可在一行打印词汇，再使用换行符（ \n ）插
# 入一个空行，然后在下一行以缩进的方式打印词汇的含义。
vocabulary = {
    'append': '新增',
    'del': '删除',
    'for': '遍历',
    'if': '判断',
    'print': '打印',
}
print("append" + ": " + vocabulary['append'])
print("del\n")
print(vocabulary['del'])

# 词汇表 2 
for voc, value in vocabulary.items():
	print("voc is " + voc + "and value is " + value)

# 河流
rivers = {
	'china': 'changjiang',
	'nile': 'egypt' ,
	'india': 'henghe'
}
for country, river in rivers.items():
	print("The " + river.title() + " runs through " + country.title())
for river in rivers.values():
	print(river.title())
for country in rivers.keys():
	print(country.title())

# 调查
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
survey_people = {'jen', 'phil'}
for name in favorite_languages:
	if name in survey_people:
		print("Thanks " + name.title())
	else:
		print("Welcome " + name.title())

# 人
people_1 = {
	'first_name': 'zhangsan',
    'last_name': 'z',
    'age': '20',
    'city': 'aa',
}
people_2 = {
	'first_name': 'lisi',
    'last_name': 'l',
    'age': '21',
    'city': 'bb',
}
people = []
people.append(people_1)
people.append(people_2)
people.append(acquaintance)

print(people)

# 宠物
yellow = {
	'type': 'dog',
	'admin': 'zhangsan',
} 
black = {
	'type': 'cat',
	'admin': 'lisi',
}
pets = []
pets.append(yellow)
pets.append(black)
for pet in pets:
	print(pet)

# 喜欢的地方
favorite_places = {
	'zhangsan': ['北京', '天津'],
	'lisi': ['上海'],
	'wangwu': ['南京', '青岛'],
}
for name, place in favorite_places.items():
	print(name.title() + " love ")
	for p in place:
		print('\t' + p.title())

# 城市
cities = {
	'北京': {
		'country': '中国',
		'population': '2000万',
		'fact': '1800万'
	},
	'上海': {
		'country': '中国',
		'population': '1000万',
		'fact': '800万'
	},
	'杭州': {
		'country': '中国',
		'population': '800万',
		'fact': '500万'
	},
}
for name, info in cities.items():
	print(name)
	for k, v in info.items():
		print(k + " : " + v)
