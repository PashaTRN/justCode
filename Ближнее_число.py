def index_of_nearest(numbers, number):
    if len(numbers) == 0:
        return -1
    else:
        return numbers.index(min(numbers, key= lambda x: abs(x-number)))

#Sample Input 3:

#print(index_of_nearest([9, 5, 3, 2, 11], 4))
#Sample Output 3:
#1 #idex/..............
