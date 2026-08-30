class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        seen = {}
        for i in intervals:
            if i[0] not in seen.keys():
                seen[i[0]] = []
            seen[i[0]].append(i)
        key_s = sorted(seen.keys())
        new = []
        for k in key_s:
            for l in seen[k]:
                new.append(l)
        print(new)
        j = 0
        while j < len(new)-1:
            if new[j][1]>= new[j+1][0]:
                if new[j][1] < new[j+1][1]:
                    new[j][1] = new[j+1][1]

                new.pop(j+1)
            else:
                j += 1
        return new

        