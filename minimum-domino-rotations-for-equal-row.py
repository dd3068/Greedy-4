'''
TC: O(n)
SC: O(n)
'''
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        tlen = len(tops)
        if not tlen:
            return 0
        
        hmap = dict()
        target = -1
        
        for i in range(tlen):
            hmap[tops[i]] = hmap.get(tops[i], 0) + 1
            hmap[bottoms[i]] = hmap.get(bottoms[i], 0) + 1
            
            if hmap[tops[i]] >= tlen:
                target = tops[i]
                break
            if hmap[bottoms[i]] >= tlen:
                target = bottoms[i]
                break
        
        trot = 0
        brot = 0
        
        for i in range(tlen):
            if tops[i] != target and bottoms[i] != target:
                return -1
            if tops[i] != target:
                trot += 1
            elif bottoms[i] != target:
                brot += 1
        
        return min(trot, brot)
        