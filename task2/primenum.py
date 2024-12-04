def next_prime(number):
    number=number+1
    while True:
        for i in range(2,number):
            if number%i==0:
                number=number+1
                break
        else:
                
          print(number)
          break
        
                
            

            

user_input=int(input("enter number"))
next_prime(user_input)



    

