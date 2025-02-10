user_input = [1,2,4,5,6]
user_input = sorted(user_input)
for i in range(min(user_input),max(user_input)+1):
  if i not in user_input:
    print(i)
