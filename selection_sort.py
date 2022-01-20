def selection_sort(lst):
	for i in range(len(lst)):
		mini = 9999
		for j in range(i, len(lst)):
			if(lst[j] < mini):
				mini = lst[j]
				mini_index = j
		tmp = lst[mini_index]
		lst[mini_index] = lst[i]
		lst[i] = mini
	print(lst)


if __name__ == '__main__':
	lst = list(map(int, input().strip().split()))
	selection_sort(lst)
