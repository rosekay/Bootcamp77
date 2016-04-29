def data_type(x):
  if type(x) == str:
    return len(x)
  elif type(x) == bool:
    return x
  elif type(x) == int:
    if x < 100:
      return ("less than 100", (x))
    elif x > 100:
      return ("more than 100", (x))
    return ("equal to 100"(x))
  elif type(x) == list:
    return x[2]
  return None  
  if x == None:
    return "no value"