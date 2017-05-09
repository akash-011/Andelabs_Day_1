def data_type(x):
  if  isinstance (x , str):
    return len(x)
  elif isinstance (x, bool):
    return x
  elif isinstance (x,int):
    if x < 100:
      return "less than 100"
    elif x > 100:
      return "more than 100"
    else:
      return "equal to 100"
  elif isinstance (x,list):
    if len(x) > 2:
      return x[2]
    else:
      return None 
  else:
    return "no value"

print data_type("andela")