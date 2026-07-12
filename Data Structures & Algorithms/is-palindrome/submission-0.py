import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(cleaned_text)
        t = cleaned_text[::-1]
        return cleaned_text==t