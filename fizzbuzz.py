class FizzBuzz:

    def play(self, num):
        if (num % 3 == 0 and num % 5 ==0):
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

i = 0
while i < 101:
    f = FizzBuzz()
    f.play(i)
    i+=1


# f = FizzBuzz()
# f.play(5)
