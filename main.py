#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    
    res = 0
    for i in range(len(list1)):
        res += list1[i-1]*list2[i-1]
    return res

if __name__ == '__main__':
    num_1 = input("first number")
    num_2 = input("second number")
    list1 = [int(x) for x in (num_1)]
    list2 = [int(x) for x in (num_2)]
    res = 0
    if len(list1) != len(list2):
       exit
    else:
       pass

    print(sum_of_products(list1, list2))

