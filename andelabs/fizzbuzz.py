# fizz buzz
def fizz_buzz(A):
  
  if A % 3 ==0 and A % 5 == 0:
    return "FizzBuzz"
  elif A % 3 == 0:
    return "Fizz"
  elif A % 5 == 0:
    return "Buzz"
  
  return A  
