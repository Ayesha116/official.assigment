import random
array = []
for i in range(0,100):
    array.append(random.randint(10,10000))
for j in array:
    print(j)
a = max(array)
print("maximum element of array=", a)
print("index of maximum element of array=", array.index(a))
b = min(array)
print("minimum element of array=", b)
print("index of minimum element of array=",array.index(b))
c = int((sum(array))/len(array))
print("mean of elements of array=",c)