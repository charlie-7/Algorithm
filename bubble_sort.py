def bubble_sort(lst):
	for i in range(len(lst)):
		for j in range(len(lst)-1):
			if(lst[j] > lst[j+1]):
				tmp = lst[j]
				lst[j] = lst[j+1]
				lst[j+1] = tmp
	print(lst)


if __name__ == '__main__':
	lst = list(map(int, input().strip().split()))
	bubble_sort(lst)
