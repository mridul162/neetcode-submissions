class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = ''.join(ch for ch in s if ch.isalnum())
        lower_text = clean_text.lower()

        left = 0
        right = len(lower_text) - 1

        while left < right:
            if lower_text[left] != lower_text[right]:
                return False
            left += 1
            right -= 1
        return True

        