
v = [
	{'name': '日天', 'tid': 1, 'title': '全栈58888期'},
	{'name': '日天', 'tid': 1, 'title': '全栈656期'},
	{'name': '日地', 'tid': 2, 'title': '黑客来了'},
	{'name': '日地', 'tid': 2, 'title': '全栈100期'},
	{'name': '日方少伟', 'tid': 3, 'title': '全栈58888期'},
	{'name': '日方少伟', 'tid': 3, 'title': '全栈656期'},
	{'name': '日方少伟', 'tid': 3, 'title': '黑客来了'}
]

result = {
	# 1: {'name': '日天', 'tid': 1, 'titles':['全栈58888期' '全栈656期']},
	# 2: {'name': '日地', 'tid': 2, 'titles':['黑客来了' ]},
}

for row in v:
	tid =row['tid']
	if tid in result:
		result[tid]['titles'].append(row['title'])
	else:
		result[tid] = {'tid': row['tid'],'name':row['name'],'titles': [row['title'],]}

for item in result.values():
	print(item)
