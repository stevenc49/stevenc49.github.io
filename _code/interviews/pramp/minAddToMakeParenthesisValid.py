  numInvalid=0
  stack=[]
  
  for c in text:
    if c=='(':
      stack.append(c)
      numInvalid+=1
      
    elif c==')':
      if not stack:
        numInvalid+=1
      else:
        stack.pop()
        numInvalid-=1
    
  return numInvalid + len(stack)


res = 0
stack = 0
  for bracket in text:
    if bracket == '(':
      stack += 1
    if bracket == ')' and stack != 0:
      stack -= 1
    elif bracket == ')' and stack == 0:
      res += 1
  return res + stack
  