def merge(nums1, m, nums2, n):
    nums1[:m] = nums1[:m] + nums2
    nums1.sort(reverse=True)

nums1 = list(map(int, input("Nums1: ").split()))
nums2 = list(map(int, input("Nums2: ").split()))

merge(nums1, len(nums1) - len(nums2), nums2, len(nums2))

print(nums1)