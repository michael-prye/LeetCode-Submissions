def getCommon( nums1: list[int], nums2: list[int]) -> int:
       common = set(nums1).intersection(set(nums2))
       if len(common):
              return min(common)
       return -1
print(getCommon([1,2,3],[2,4]))