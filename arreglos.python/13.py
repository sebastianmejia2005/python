import random

vec = [round(random.random()*100) for i in range(10)]
print(vec)

num = [x if x < 10 else 0 for x in vec]
print(num)