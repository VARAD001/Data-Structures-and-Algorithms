class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            L = 0
            R = len(row) - 1
            while L < R:
                if row[L] == row[R]:
                    row[L] ^= 1
                    row[R] ^= 1
                L += 1
                R -= 1
            if L == R:
                row[L] ^= 1
        return image
            