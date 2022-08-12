api_nasa = 'DRIdSstSRoLwmkZcnJZ7hcNk06TesamKjjcTkA6U'

"""Электронная почта учетной записи: dizel260412@gmail.com Идентификатор
учетной записи: b9744fa6-1e0c-4fcc-9bc9-9d8ad2d1273e"""

#
# import requests
# import json
#
# r = requests.get(
#             f"https://api.nasa.gov/planetary/apod?api_key={api_nasa}"
#         )
# data = r.json()
# print(r)
# with open('test.json', 'w') as f:
# 	f.write(r.text)

# n, m = int(input()), int(input())
# a = []
# b = []
# print()
# for _ in range(n * m):
# 	s = input()
# 	a.append(s)
# 	if len(a) == m:
# 		print(*a)
# 		b.append(a)
# 		a = []
# print()
# for j in range(m):
# 	for i in b:
# 		print(i[j], end=' ')
# 	print()

# n = int(input())
# a = []
# b = 0
# c = 0
# for _ in range(n):
# 	s = input().split()
# 	a.append(s)
# for i in a:
# 	c += int(i[b])
# 	b += 1
# print(c)

a = [list(map(int, input().split())) for _ in range(int(input()))]
for _ in a:
	b = 0
	for __ in _:
		if __ > sum(_) / len(_):
			b += 1
	print(b)



