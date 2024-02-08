#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    
    res = 0
    for i in range(len(list1)):
        res += list1[i]*list2[i]
    return res

if __name__ == '__main__':
    num_1 = input()
    num_2 = input()
    list1 = num_1.split()
    list2 = num_2.split()
    list1 = [int(x) for x in (list1)]
    list2 = [int(x) for x in (list2)]
    res = 0
    print(sum_of_products(list1, list2))
#test