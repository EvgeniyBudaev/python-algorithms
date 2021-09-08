numbersLength = int(input())
listNumbers = list(map(int, input().split()))  # масив из чисел
k = int(input())

numberParsed = ''.join(map(str, listNumbers))
numberTotal = int(numberParsed) + k
numberOutput = ' '.join(map(str, str(numberTotal)))
print(numberOutput)
