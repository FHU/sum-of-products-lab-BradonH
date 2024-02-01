#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    
    res = 0
    for i in range(len(list1)):
        res += list1[i]*list2[i]
    return res

if __name__ == '__main__':
    num_1 = input()
    if num_1.isdigit() == False:
        exit()
    num_2 = input()
    if num_2.isdigit() == False:
        exit()
    list1 = [int(x) for x in (num_1)]
    list2 = [int(x) for x in (num_2)]
    res = 0
    try:
        test = len(list1)
        list2[test]
        test = len(list2)
        list1[test]
        print(sum_of_products(list1, list2))
    except:
        print("Error")

