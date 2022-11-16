import random

for i in range(10):
    print("Число: ", i)
    if random.randint(0, 100) == 1:
        print("[ERROR] БЕГИИИИИИ!!!!")
        break
else:
    print("Мы вышли естественным способом")