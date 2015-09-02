#print letters the fancy way!
a =  [0,1,1,1,1,1,0,
      1,1,1,0,1,1,1,
      0,0,0,0,0,1,1,
      0,1,1,1,1,1,1,
      1,1,1,0,1,1,1,
      1,1,0,0,0,1,1,
      1,1,1,0,1,1,1,
      0,1,1,1,1,1,0]

b = [0,1,0,0,0,0,0,
     1,1,0,0,0,0,0,
     1,1,0,0,0,0,0,
     1,1,1,1,1,1,0,
     1,1,1,0,1,1,1,
     1,1,0,0,0,1,1,
     1,1,1,0,1,1,1,
     0,1,1,1,1,1,0]

c = [0,1,1,1,1,1,0,
     1,1,1,0,1,1,1,
     1,1,0,0,0,1,1,
     1,1,0,0,0,0,0,
     1,1,0,0,0,0,0,
     1,1,0,0,0,1,1,
     1,1,1,0,1,1,1,
     0,1,1,1,1,1,0]

alphabet = {'a':a, 'b':b, 'c':c}

def printWord(word):
  for i in range(8):
    for j in range(len(word)):
      printSingleLine(word[j], i)
    print('') #Newline

def printSingleLine(fill, whatLine):   #Print one line from one letter
  letterTemplate = alphabet.get(letter)
  for j in range(7):
    if letterTemplate[j + (whatLine * 7)] == 0:
      print(' ', end="")    #print blankspace
    else:
      print(fill, end="")   #print fill
  print(' ', end = "")      #Print spaces

printWord("abca")
