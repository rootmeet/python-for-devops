my_list = ["Yellow","Red","Green"]
my_list.sort()
print(my_list)
# for loop
for i in range(100):
    if i > len(my_list) -1:
        break
    else:
        print(my_list[i])

i=0
while i < 3:
    print(my_list[i])
    i += 1