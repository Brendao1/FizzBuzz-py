class FizzBuzz:
  def play(self, num):
      if num % 3 == 0:
          print("Fizz")
          # return "Fizz"
      else:
          print(num)


f = FizzBuzz()
f.play(3)
