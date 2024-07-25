def merge_sort(arr):
    n=len(arr)
    if n<=1:
        return 
    mid=n//2
    lp=arr[:mid][:]
    rp=arr[mid:][:]
    merge_sort(lp)
    merge_sort(rp)
    merge(lp,rp,arr)
def merge(arr1,arr2,sa):
    p1=0
    p2=0
    n1=len(arr1)
    n2=len(arr2)
    ind=0
    while p1<n1 or p2<n2:
        if p1==n1 or(p2!=n2 and arr2[p2]<arr1[p1]):
            sa[ind]=arr2[p2]
            p2+=1
        elif p2==n2 or arr1[p1]<=arr2[p2]:
            sa[ind]=arr1[p1]
            p1+=1
        ind+=1

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        merge_sort(nums)
        return nums
