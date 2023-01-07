lst = [el**2 for el in range(5)]
print(lst)

lst1 = [[a, b] for a in range(3) for b in range(3)]
print(lst1)

lst2 = [str(rur) * 3 for rur in lst]
print(lst2)

lst3 = [i * 2 for i in range(9)]
print(lst3)

lst4 = [str(a) + str(b) for a in ["x", "y"] for b in ["y", "z", "v"]]
print(lst4)

lst4 = lst4[0: 3]
print(lst4)

lst5 = [str(num + 1) + "x" for num in range(4)]
print(lst5)

lst_remove = lst5.pop(1)
print(lst_remove)
print(lst5)