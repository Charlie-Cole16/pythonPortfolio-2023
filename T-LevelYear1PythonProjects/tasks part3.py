file = open("words.txt", "r")

iCount = 0

data = file.read()
words = data.split()
for word in words:
    wordLen = len(word)
    if wordLen < 4:
        iCount += 1

print(iCount)
file.close()