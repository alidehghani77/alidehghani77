"""
        find missing number
        getMissingNo takes list as argument
"""
def getMissingNumber_Method1(A):
    l = len(A)
    solicitedSum = (l+1) * (l + 2) /2
    sumOfA = 0
    # method 1
    # for i in A :
    #     sumOfA += i
        
    #mothod 2
    sumOfA = sum(A)
        
    return int(solicitedSum - sumOfA)


# a represents the array
# n : Number of elements in array a
def getMissingNumber_Method2(a, n):
    i, total = 0, 1
 
    for i in range(2, n + 2):
        total += i
        total -= a[i - 2]
    return total

def getMissingNumber_Method3(a, n):
    x1 = a[0]
    x2 = 1
     
    for i in range(1, n):
        x1 = x1 ^ a[i]
         
    for i in range(2, n + 2):
        x2 = x2 ^ i
     
    return x1 ^ x2

def getMissingNumber_Method4(a, n):
    n_elements_sum=n*(n+1)//2
    return n_elements_sum-sum(a)
 

 
# This code is contributed by Mohit kumar


#arr = [1,2,3,5,6,7,8]
arr = [1, 2, 4, 5, 6]
print(getMissingNumber_Method1(arr))
print(getMissingNumber_Method2(arr, len(arr)))
print(getMissingNumber_Method3(arr, len(arr)))
print(getMissingNumber_Method4(arr, len(arr)))