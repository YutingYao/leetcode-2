"""
Array Of Products:

Write a function that takes in a non-empty array of integers and returns an array of the same length,
 where each element in the output array is equal to the product of every other number in the input array.
In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].

Note that you're expected to solve this problem without using division.
https://www.algoexpert.io/questions/Array%20Of%20Products
"""


# O(n) time | O(n) space - where n is the length of the input array (O(3n) time)
def arrayOfProducts(array):
    if len(array) <= 2:
        return array

    products = []
    # We know that for each element, the product of all other elements
    #  will be equal to the the products of the elements to its right and and the products of the elements to its left
    # we can try to calculate that beforehand

    left_products = [1]  # we will skip the first element
    left_running_prod = 1
    for i in range(1, len(array)):
        left_running_prod *= array[i-1]  # multiply by prev element
        left_products.append(left_running_prod)

    right_products = [1]  # we will skip the last element
    right_running_prod = 1
    for i in reversed(range(len(array)-1)):
        right_running_prod *= array[i+1]  # multiply by prev element
        right_products.insert(0, right_running_prod)

    for idx in range(len(array)):
        products.append(left_products[idx] * right_products[idx])

    return products


y = [5, 1, 4, 2]
x = [1, 2, 3, 4, 5]
print(arrayOfProducts(x))
print(arrayOfProducts(y))


# O(n) time | O(n) space - where n is the length of the input array (O(3n) time)
def arrayOfProducts0(array):

    # calculate products to the left of elements
    left_products = [1] * len(array)
    left_running_product = 1
    for idx in range(len(array)):
        left_products[idx] = left_running_product
        left_running_product *= array[idx]

    # calculate products to the right of elements
    right_products = [1] * len(array)
    right_running_product = 1
    for idx in reversed(range(len(array))):
        right_products[idx] = right_running_product
        right_running_product *= array[idx]

    # multiply left & right products for each element
    products = [0] * len(array)
    for idx in range(len(array)):
        products[idx] = left_products[idx] * right_products[idx]

    return products
