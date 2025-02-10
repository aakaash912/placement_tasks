input_str = str(input("Enter your phrase with spaces: "))
words = input_str.split()
reversed_words = []
for i in range(len(words) - 1, -1, -1):
reversed_words.append(words[i])
output_str = " ".join(reversed_words)
print(output_str)
