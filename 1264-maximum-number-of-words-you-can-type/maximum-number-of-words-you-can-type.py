class Solution(object):
    def canBeTypedWords(self,text, brokenLetters):
        broken_set = set(brokenLetters)  # Convert to set for fast lookup
        words = text.split()  # Split text into words
        count = 0
        print("words",words)
        print("broken_set",broken_set)

        for word in words:
            # If none of the letters in the word are broken, increment count
            if not any(char in broken_set for char in word):
                count += 1

        return count
        