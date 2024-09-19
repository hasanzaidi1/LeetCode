def findMedianSortedArrays(nums1, nums2):
    new_arr = []
    median_ans = 0

    # Merge nums1 and nums2
    new_arr.extend(nums1)
    new_arr.extend(nums2)

    # Sort the merged array
    new_arr_sorted = sorted(new_arr)

    # Check if the length is even
    if len(new_arr_sorted) % 2 == 0:
        # Two middle elements for even length
        median1 = new_arr_sorted[(len(new_arr_sorted) // 2) - 1]
        median2 = new_arr_sorted[len(new_arr_sorted) // 2]
        median_ans = (median1 + median2) / 2.0  # Ensure floating-point division
    else:
        # Single middle element for odd length
        median_ans = new_arr_sorted[len(new_arr_sorted) // 2]

    return median_ans



print(findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
print(findMedianSortedArrays(nums1 = [1,9,2,7], nums2 = [3,4]))

