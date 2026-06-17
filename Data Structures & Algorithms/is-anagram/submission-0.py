class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def createMap(s: str) -> dict:
            countMap = {}
            for i in s:
                if i in countMap:
                    countMap[i]+=1
                else:
                    countMap[i] = 1
            return countMap
        smap, tmap = createMap(s), createMap(t)
        return smap==tmap
