import random
num_list = []
num_gen = 1
for x in range(1000):
    x += 1
    num_list.append(x)

def maximum():
    return max(random.sample(num_list, 4))

def max_order():
    order_l = []
    og_sample = []
    copy_rand = random.sample(num_list, 4)
    og_sample.append(copy_rand)
    for x in range(4):
        order_l.append(max(copy_rand))
        copy_rand.remove(max(copy_rand))
    return og_sample, order_l

def min_order():
    order_l2 = []
    copy_rand2 = random.sample(num_list, 4)
    for x in range(4):
        order_l2.append(min(copy_rand2))
        copy_rand2.remove(min(copy_rand2))
    return order_l2

def n_max():
    order_l3 = []
    copy_rand3 = random.sample(num_list, 4)
    for x in range(4):
        order_l3.append(max(copy_rand3))
        copy_rand3.remove(max(copy_rand3))
    n = int(input("n = "))-1
    return order_l3, order_l3[n]

print(max_order())

