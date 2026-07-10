class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortMap = {}
        for i in strs:
            # sortMap[i] = sorted(i)
            key1 = ''.join(sorted(i))
            if key1 in sortMap:
                # print(key1, sortMap)
                sortMap[key1].append(i)
            else:
                sortMap[key1] = [i]
        # print(list(sortMap.values()))
        return list(sortMap.values())
        