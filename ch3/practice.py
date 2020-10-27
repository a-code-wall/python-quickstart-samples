names = ['zhangsan','lisi','wangwu']
print(names)
print(names[0])
print(names[1])
print(names[2])
message = names[0] + ", 你好!"
print(message) 
message = names[1] + ", 你好!"
print(message) 
message = names[2] + ", 你好!"
print(message) 
commuteWays = ['骑自行车', '骑摩托车', '开汽车']
message = '我在工作日选择' + commuteWays[0] + "或者" + commuteWays[-2] + ",而在周末会" + commuteWays[-1]
print(message)

persons = ['zhangsan','lisi','wangwu']
print(persons)
print(persons[-1] + "无法赴约")
persons[-1] = 'zhaoliu'
print("发出邀请" + persons[0] + "," + persons[1] + "," + persons[2])
print("找到了更大的餐桌,还可以再邀人")
persons.insert(0,"sunqi")
persons.insert(2,"wangba")
persons.append("maojiu")
print("再次发出邀请" + persons[0] + "," + persons[1])
print("只能邀请两位嘉宾共进晚餐")
print(persons.pop() + ",抱歉,不能邀请你了")
print(persons.pop() + ",抱歉,不能邀请你了")
print(persons.pop() + ",抱歉,不能邀请你了")
print(persons.pop() + ",抱歉,不能邀请你了")
print(persons[0] + ",你依然在受邀人之列")
print(persons[-1] + ",你依然在受邀人之列")
print("我邀请了" + str(len(persons)) + "人")
del persons[-1]
del persons[0]
print(persons)

trip_place = ['japan', 'china', 'american', 'london', 'canada']
print(trip_place)
print(sorted(trip_place))
print(trip_place)
print(sorted(trip_place,reverse=True))
print(trip_place)
trip_place.reverse()
print(trip_place)
trip_place.reverse()
print(trip_place)
trip_place.sort()
print(trip_place)
trip_place.sort(reverse=True)
print(trip_place)

