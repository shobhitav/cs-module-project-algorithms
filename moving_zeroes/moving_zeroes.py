'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    new_arr=[]
    count=0
    for i in range(len(arr)):
        if arr[i] != 0:
            new_arr.append(arr[i])
            count+=1
    while len(new_arr) < len(arr):
        new_arr.append(0) 
    return new_arr    
    



    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")