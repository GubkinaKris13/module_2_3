my_list  =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
pozit = []
initial = 0
while initial < len(my_list):

    if my_list[initial]< 0 : break
    pozit.append(my_list[initial])
    initial +=1
pozit.remove(0)
for i in pozit:
    if i != pozit[len(pozit) -1]:
        print(f'{i}')
    else:
        print(i)






    #print(len(my_list))
