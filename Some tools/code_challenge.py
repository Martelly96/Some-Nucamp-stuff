def fizzbuzz(num):
    for x in range (1, num+1):
        if num // 3:
            print("Fizz")
        elif num // 5:
            print("Buzz")
        elif num // 3 and num // 5:
                print("FizzBuzz")
        else:
             print(num)

fizzbuzz(50)