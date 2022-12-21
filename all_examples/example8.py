from copy import deepcopy

lst_1 = [1, 2]
lst_2 = [1, 2, lst_1]

lst_3 = lst_2.copy()

print(lst_3 == lst_2) # True
print(lst_3 is lst_2) # False

print(lst_1, id(lst_1))
print(lst_2, id(lst_2))
print(lst_3, id(lst_3))

print(id(lst_2[2]))
print(id(lst_3[2]))

lst_3[2][1] = 0

print(lst_1)

lst_4 = deepcopy(lst_2)
print(id(lst_4))
print(id(lst_4[2]))

# ==
# is