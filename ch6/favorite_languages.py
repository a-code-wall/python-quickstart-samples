# 由类似对象组成的字典
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
print("Sarah's favorite_languages is " + favorite_languages['sarah'].title() + ".")

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite_languages is " + language.title() + ".")

# 遍历字典中的所有键
for name in favorite_languages.keys():
	print(name.title())

friens = {'phil', 'sarah'}
for name in favorite_languages.keys():
	print(name.title())
	if name in friens:
		print(" Hi " + name.title() +
			", I see your favorite_languages is " + 
			favorite_languages[name].title() + "!")
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

print("\n")

for language in set(favorite_languages.values()):
	print(language.title())

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are")
	for language in languages:
		print("\t" + language.title())