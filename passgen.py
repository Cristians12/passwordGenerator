import random
from string import punctuation


# Function to shuffle the list
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


uppcaseLetter = chr(random.randint(65, 90))
uppcaseLetter1 = chr(random.randint(65, 90))
lowCaseLetter = chr(random.randint(97, 122))
lowCaseLetter1 = chr(random.randint(97, 122))
digit1 = chr(random.randint(48, 57))
digit2 = chr(random.randint(48, 57))
punctuation1 = chr(random.randint(33, 47))
punctuation2 = chr(random.randint(33, 47))

password = uppcaseLetter + uppcaseLetter1 + lowCaseLetter + lowCaseLetter1 + digit1 + digit2 + punctuation1 + punctuation2

password = shuffle(password)
print(password)
