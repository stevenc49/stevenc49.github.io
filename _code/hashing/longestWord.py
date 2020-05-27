import re

def LongestWord(sen):

  # code goes here
  tokens = sen.split(" ")

  maxWord = ""
  maxLength = 0
  for token in tokens:
    
    token = re.sub('[^a-zA-Z]','', token)
    
    if len(token) > maxLength:
      maxLength = len(token)
      maxWord = token
  
  return maxWord

# keep this function call here 
print(LongestWord(input()))