#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    
    res = 0
    for i in range(len(list1)):
        res += list1[i]*list2[i]
    return res

if __name__ == '__main__':
    num_1 = input()
    if num_1 == False:
        exit()
    num_2 = input()
    if num_2 == False:
        exit()
    list1 = num_1.split()
    list2 = num_2.split()
    list1 = [int(x) for x in (num_1)]
    list2 = [int(x) for x in (num_2)]
    res = 0
    try:
        test = len(list1)
        list2[test-1]
        test = len(list2)
        list1[test-1]
        print(sum_of_products(list1, list2))
    except:
        print("Error")

