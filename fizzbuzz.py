class FizzBuzz:

    def play(self, num):
        if (num % 3 == 0 and num % 5 ==0):
            print("FizzBuzz")
            return "FizzBuzz"
        elif num % 3 == 0:
            print("Fizz")
            return "Fizz"
        elif num % 5 == 0:
            print("Buzz")
            return "Buzz"
        else:
            print(num)
            return num
i = 0
while i < 101:
    f = FizzBuzz()
    f.play(i)
    i+=1

# f = FizzBuzz()
# f.play(5)
