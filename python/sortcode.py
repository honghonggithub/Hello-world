#######排序

##冒泡排序
def bubble_sort(list):
	length = len(list)
	for index in range(length):
		for j in range(1,length-index):
			if list[j-1]>list[j]:
				list[j-1],list[j]=list[j],list[j-1]
	return list

print(bubble_sort([1,2,5,6,0,11,23,12]))

##选择排序法
def selection_sort(list):
	n = len(list)
	for i in range(n):
		min1 = i
		for j in range(i+1,n):
			if list[j]<list[min1]:
				min1 = j
		list[min1],list[i]=list[i],list[min1]
	return list
print(selection_sort([1,2,5,6,0,11,23,12]))

###快速排序
def quick_sort(list):
	less = []
	pivotlist = []
	more = []
	if len(list)<=1:
		return list
	else:
		pivot = list[0]
		for i in list:
			if i<pivot:
				less.append(i)
			elif i>pivot:
				more.append(i)
			else:
				pivotlist.append(i)
		less = quick_sort(less)
		more = quick_sort(more)
		return less+pivotlist+more
print(quick_sort([1,2,5,6,0,11,23,12]))




