class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        if M==0 or N==0:
            return 0
        A.sort()
        if N<M:
            return -1
        mini=A[N-1]-A[0]
        for i in range(len(A)-M+1):
            mini=min(mini,A[i+M-1]-A[i])
        return mini
