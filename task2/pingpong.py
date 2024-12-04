num=int(input("enter number"))
if num%15==0:
    print("PINPONG")
elif num%3==0:
    print("PING ")
elif num%5==0:
    print("PONG")
else:
    print(f"{num}")