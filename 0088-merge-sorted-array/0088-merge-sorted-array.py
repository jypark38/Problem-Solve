class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        tIdx = m+n-1
        idx1 = m-1
        idx2 = n-1
        if(idx2<0):
            return
        
        while(idx2>=0 and idx1>=0):
            if(nums2[idx2]>=nums1[idx1]):
                nums1[tIdx] = nums2[idx2]
                idx2-=1
                tIdx-=1
            else:
                nums1[tIdx] = nums1[idx1]
                idx1-=1
                tIdx-=1
        
        while(idx2>=0):
            nums1[tIdx] = nums2[idx2]
            idx2-=1
            tIdx-=1
            