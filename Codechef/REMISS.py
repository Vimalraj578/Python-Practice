loop = int(input())
for _ in range(loop):
	a,b = map(int,input().split())
	print(max(a,b),a+b)