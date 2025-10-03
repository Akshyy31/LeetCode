class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = re.sub(r'[^a-zA-Z0-9]',"",s).lower()
        return string == string[::-1]

        