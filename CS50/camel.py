# camel_case = input('Please input the word in camel notation:   ')
# snake = []
# for letter in camel_case:
#     if letter.islower():
#         snake.append(letter)
#     else:
#         snake.append('_')
#         snake.append(letter.casefold())
 
# for letter in snake:
#     print(letter, end="")

camel_case = input('PLEASE INPUT YOUR TEXT IN CAMEL CASE:  ')
for letter in camel_case:
    if letter.isupper():
        camel_case = camel_case.replace(letter, f'_{letter.casefold()}')
    else:
        continue
print(camel_case)