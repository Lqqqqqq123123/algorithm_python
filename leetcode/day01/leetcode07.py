class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        xx, int_max = 0, 2 ** 31 - 1

        t = x
        while t:
            pop = t % 10
            if xx > (int_max - pop) // 10:
                return False
            xx = xx * 10 + pop

        return x == xx