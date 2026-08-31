class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen= {}
        for str in strs:
            key = "".join(sorted(str))
            if key not in seen.keys():
                seen[key] = []
            seen[key].append(str)
        return list(seen.values())