# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         newlist=[]
#         palindrome=[]
#         for j in range(len(s)):
#             for i in range(j+1,len(s)+1):
#                 newlist.append(s[j:i])
    
          
          
#         for i in newlist:
#             if (i==i[::-1]):
#                 palindrome.append(i)
                
#         max_word = ""
#         for word in palindrome:
#           if len(word) > len(max_word):
#             max_word = word

#         return max_word


class Solution(object):
    def longestPalindrome(self, s):
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]  

        longest = ""
        for i in range(len(s)):
            
            p1 = expand(i, i)
            p2 = expand(i, i+1)

            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2

        return longest
