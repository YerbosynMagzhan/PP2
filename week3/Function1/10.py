def unique(lst):
    new_lst = []
    for uniq in lst:
        if uniq not in new_lst:
            new_lst.append(uniq)
    return new_lst

lst = [str(s) for s in input().split()]
print(unique(lst)) 