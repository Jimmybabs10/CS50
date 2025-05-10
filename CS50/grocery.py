def main():
    fruit_lists = grocery_lists()
    fruit_lists.sort()
    fruits_in_cart = number_of_fruits(fruit_lists)
    print(fruits_in_cart)
    for fruits in fruits_in_cart:
        print(f'{fruits}  {fruits_in_cart[fruits]}')


#store the fruits in a list
def grocery_lists():
    fruits_list = []
    try:
        while True:
            fruit = input('please write your fruit       ')
            fruits_list.append(fruit.capitalize())
    except EOFError:
        return fruits_list

#count the numbers of fruits in the list
def number_of_fruits(sorted_list):
    #sorted_list = ['apple', 'banana', 'banana', 'banana', 'orange']
    fruit_quantity = {}   
    for fruit in sorted_list:
        fruit_quantity[fruit] = sorted_list.count(fruit)
    return fruit_quantity


main()



# fruits = ['apple', 'banana', 'banana', 'orange']
# print(fruits.count(fruits[3]))
# print('apple' in fruits)