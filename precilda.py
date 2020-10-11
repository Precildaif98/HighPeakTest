inputfile = open("/Users/irol/Documents/input.txt","r")
lines = inputfile.readlines()
read = lines[0]
read =read.rstrip("\n")
key = read.split(':')
t = (int(key[1]))
q = list()
list1 = list()
list2 = list()

for i in range(5,15):
    e1 = lines[i-1]
    e1 = e1.rstrip("\n")
    a1 = e1.split(':')
    list1.append(a1[0])
    a2= (int(a1[1]))
    list2.append(a2)
di = dict(zip(list2, list1))


# Sorting the list
lis = list()
for j in range(10):
    s1 = max(list2)+1
    for i in list2:
        if i < s1:
            s1 = i
    lis.append(s1)
    list2.remove(s1)


# finding min difference
list2 = lis
min_value = list2[len(list2)-1]
index =0
for i in range(0, len(list2)-1-t):
    if min_value > list2[i+t-1]-list2[i]:
        min_value = list2[i+t-1]-list2[i]
        index = i
outputfile = open("output.txt", "w")
print("The goodies selected for distribution are:\n", file = outputfile)
print(file = outputfile)
#Writing string1 into output file
for i in range (index, index+t):
     print(di[list2[i]],": ",list2[i],file = outputfile)
#Writing string2 into output file
s3 = print("\nThe difference between the chosen goodie with highest price and the lowest price is", min_value,file = outputfile)
outputfile.close()
