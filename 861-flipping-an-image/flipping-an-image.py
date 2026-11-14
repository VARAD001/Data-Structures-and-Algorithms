class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        res = []
        for row in image:
            row.reverse()
            for i in range(len(row)):
                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0   
            res.append(row)
        return res