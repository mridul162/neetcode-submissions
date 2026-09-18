class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = ''.join(ch.lower() for ch in s if ch.isalnum())
        return clean_text == clean_text [::-1]

        