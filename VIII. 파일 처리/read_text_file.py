f = open("file.txt", "r", encoding="utf8")

text0 = f.readline()
print(text0)
text1 = f.readline()
print(text1)
text2 = f.readline()
print(text2)

f.close()