'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    new_dict={}
    
    for item in arr:
        if new_dict.get(item) is None:
           new_dict[item]=1
        else:
            new_dict[item]+=1
    # return new_dict

    for key in new_dict:
        if new_dict[key]==1:
            return key
           

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")