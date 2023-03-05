#triangle
for i in range (1, 9):
    print()
    #print() - 1 space \n is 2 spaces
    for j in range (i):
        print('*', end='')
#tempCodeRunner
x = int(input("Enter any number of choice:"))
def prime (x):
    if x > 1:
        for i in range(2, int(x/2)+1):
            if (x % i) == 0:
                print(x, "is not a prime number")
                break
        else:
            print(x, "is a prime number")
    else:
        print(x, "is not a prime number")
prime(x)   

#for loop
##for loop
Mylist=['A','B','C']
for i in range(len(Mylist)):
    print (Mylist[i])
#len() outputs integers of a list
#range(start,stop,step)
#range() start default 0 and step by default is 1
#STOP is mandatory other two are optional  

##nested loop
suits=['diamonds','hearts','spades','club']
values=[1,2,3,4,5,6,7,8,9,10,'jack','queen','king','Ace'] 
for suit in suits:
    for value in values:
        print(f"{value} of {suit}")
        #{} is demarcation to highlight its not a part of the string only in f string
##nested for loops in range
for i in range(5):
    for j in range(3):
        print(i,j)
#this prints (0-4, 0-2)

##while loop
#while loop works with boolean values 
i=0
while i<5:
    print("Hi")
    i += 1 
# += 1 increment by 1
# to break a while loop condition must be False 

#ArrayExercise
#input S output palindrome
#string to list
#check string is convertible
#NO condition 
#fill missing char
#middle missing AND length odd => fill a
#question mark => fill a 
def solution(S):
    S = list(S)
    N = len(S)
    for i in range(N//2):
        if S[i] != '?' and S[N-1-i] != '?' and S[i] != S[N-1-i]:
            return 'NO'
        if S[i] == '?' and S[N-1-i] == '?':
            S[i] = S[N-1-i] = 'a'
        elif S[i] == '?':
            S[i] = S[N-1-i]
        elif S[N-1-i] == '?':
            S[N-1-i] = S[i]
    if N % 2 == 1 and S[N//2] == '?':
        S[N//2] = 'a'
    if S.count('?') > 0:
        for i in range(N):
            if S[i] == '?':
                S[i] = 'a'
    return ''.join(S)

print(solution("?ab??a"))
print(solution("bab??a"))
print(solution("?a?"))



