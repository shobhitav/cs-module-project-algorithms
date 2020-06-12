'''
Input: a List of integers
Returns: a List of integers
'''
 # o(n^2)
def product_of_all_other_numbers(arr):   
    new_arr =[0]*len(arr)
    for i in range(len(arr)):
        product=1
        for j in range(len(arr)) :
            if j != i :
                product*=arr[j]
        new_arr[i]=product
    return new_arr


#O(2n) ~ o(n)
# Does not work if any of list element is 0  
# def product_of_all_other_numbers(arr):
#     new_arr=[0]*len(arr)
#     product=1
#     for i in range(len(arr)):
#         product=product*arr[i]

#     for j in range(len(arr)):
#         new_arr[j]=product//arr[j]

#     return new_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
