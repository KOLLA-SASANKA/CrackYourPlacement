class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        p={'(':')','{':'}','[':']'}
        for i in range(len(s)):
            if s[i] in p:
                st.append(s[i])
            elif len(st)==0 or s[i]!=p[st.pop()]:
                return False
        return len(st)==0
