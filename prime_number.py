'''
Program to find is a number is prime
'''
def prime(num):
    '''
    Checks if a n is prime.
    '''
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        return True
    return False
