from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = Counter(magazine)

        for c in ransomNote:
            if c not in cnt or cnt[c] < 1:
                return False

            cnt[c] -= 1

        return True
