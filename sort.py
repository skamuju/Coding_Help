import random

num_list = []

num_gen = 1

for x in range(1000):
    x += 1
    num_list.append(x)

rand_set = random.sample(num_list, 4)
 
print(rand_set)

def maximum():
    return max(rand_set)

def max_order():
    order_l = []
    for x in range(4):
        order_l.append(max(rand_set))
        rand_set.remove(max(rand_set))
    return order_l

print(max_order())
#print(maximum())