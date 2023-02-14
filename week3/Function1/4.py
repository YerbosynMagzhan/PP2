def filter_prime(list):
    prime_list = []
    for i in list:
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list
 

lst = filter_prime(int(s) for s in input().split())

print(lst)