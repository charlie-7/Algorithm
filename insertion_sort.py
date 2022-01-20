lst = list(map(int, input().strip().split()))
for i in range(1, len(lst)):
	itr = i-1
	tmp = lst[i]
	while(lst[itr] > tmp and itr >= 0):
		lst[itr+1] = lst[itr]
		itr -= 1
	lst[itr+1] = tmp	
	print(lst)
