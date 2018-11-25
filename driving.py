Language = input('choose your Language,English or Chinese?: ')
if Language =='Chinese':
	Country = input('请问你是哪国人?： ')
	age = input('请问你的年龄?: ')
	age = int(age)
	if Country == '中国':
		if age >= 18:
			print('你可以考驾照')
		else:
			print('你不可以考驾照')
elif Language == 'English':
	Country = input('where are you from?: ')
	age = input('What is your age?: ')
	age = int(age)
	if Country == 'America':
		if age >= 16:
			print('You can take a driving test')
		else:
			print('You cannot take a driving test')

