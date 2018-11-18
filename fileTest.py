file = input("file path:")
fp = open(file, "r")
text = fp.readlines()
print(text)