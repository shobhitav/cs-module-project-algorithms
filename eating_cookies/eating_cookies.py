'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n <= 1:
        return 1
    elif n==2:
        return 2
    else:
        prev_value=[1,1,2]        
        return sum(prev_value)
            
    

# 1

# 2
# 11

# 3
# 21
# 12
# 111


# 31
# 22
# 211
# 13
# 121
# 1111
# 112



# 32
# 311
# 23
# 221
# 2111
# 212
# 14
# 131
# 122
# 1211
# 113
# 1121
# 1112
# 11111

    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
