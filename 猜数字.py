import random
secret = random.randint(1, 100)  
count = 0                        
print("我想了一个 1 到 100 之间的整数，你猜猜看！")
while True:
    guess = int(input("请输入你的猜测（1-100中的整数）："))  
    count += 1
    if guess < secret:
        print("太小了，再大一点！")
    elif guess > secret:
        print("太大了，再小一点！")
    else:
        print(f"猜对了！答案就是 {secret}，你一共猜了 {count} 次。")
        break