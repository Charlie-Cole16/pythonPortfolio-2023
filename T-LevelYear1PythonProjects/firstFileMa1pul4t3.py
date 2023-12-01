firstFile = open("Test.txt", "w")

firstFile.write("Hello world")

firstFile.close()

firstFile = open("Test.txt","r")

data = firstFile.read()

print(data)

firstFile.close()