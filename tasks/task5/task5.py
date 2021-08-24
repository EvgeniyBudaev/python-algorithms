tex_length = int(input())
text = str(input())

array_words = text.split()
list_length = []
for i in array_words:
    list_length.append(len(i))

wordMax = array_words[list_length.index(max(list_length))]
wordLengthMax = len(wordMax)

print(wordMax)
print(wordLengthMax)
