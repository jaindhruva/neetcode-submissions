class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A,B = B,A
        
        total = len(A)+len(B)
        half = total//2

        l, r = 0, len(A)-1

        while True:
            m_a = (l+r)//2
            m_b = half - m_a - 2

            a_left = A[m_a] if m_a >=0 else float("-infinity")
            a_right = A[m_a + 1] if m_a+1<=len(A)-1 else float("infinity")
            b_left = B[m_b] if m_b >=0 else float("-infinity")
            b_right = B[m_b + 1] if m_b+1<=len(B)-1 else float("infinity")

            if a_left <= b_right and b_left <= a_right:
                #odd
                if total%2 :
                    return min(a_right, b_right)
                # even
                else:
                    return (max(a_left,b_left) + min(a_right, b_right))/2
            elif a_left > b_right:
                r = m_a - 1
            else:
                l = m_a + 1
                

