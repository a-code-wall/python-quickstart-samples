# 城市和国家
# def city_country(city, country):
# 	full_name = city + ", " + country
# 	return full_name.title()

# 人口数量
def city_country(city, country, population=''):
	full_name = city + ", " + country
	if population:
		full_name += " - population " + str(population)
	return full_name.title()