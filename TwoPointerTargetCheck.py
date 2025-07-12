'''Given a sorted (in ascending order) integer array nums of n elements and a target value, find if there exists any pair of elements (nums[i], nums[j], i!=j) such that their sum is equal to target.

Solve this problem using the Two-pointers concept. The complexity should not be O(N-square) or more

Input Format

5
-3 -1 0 1 2
-2

Constraints

1 < nums.length <100

Output Format

Yes

Sample Input 0

5
-3 -1 0 1 2
-2
Sample Output 0

Yes
Sample Input 1

5
-2 0 1 1 5
0
Sample Output 1

No
'''
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
start=0
end=n-1
count=0
while start<end:
    if arr[start]+arr[end]>target:
        end-=1
    elif arr[start]+arr[end]==target:
        count=1
        break
    else:
        start+=1
      
        

if count==1:
    print('Yes')
else:
    print('No')


    
