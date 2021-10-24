x = int(input())
y = int(input())
z = int(input())
n = int(input())
final_list = []
sublist = []
for first in range(x+1):
    for second in range(y+1):
        for third in range(z+1):
            sublist.append(x)
            sublist.append(y)
            sublist.append(z)
    final_list.append(sublist)
                