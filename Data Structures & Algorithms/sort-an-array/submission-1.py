import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        #     +-----------------+-----------------+---------------+-----------------+
        #     |     < pivot     |    == pivot     |  unexamined   |     > pivot     |
        #     +-----------------+-----------------+---------------+-----------------+
        #                       ^                 ^               ^
        #                       lt                i               gt
        #
        #     invariants:
        #     - before lt : < pivot
        #     - before i  : <= pivot
        #     - after gt  : > pivot
        def partition(l, r):
            ix = random.randint(l, r)
            nums[ix], nums[r] = nums[r], nums[ix]
            pivot = nums[r]
            lt, rt = l, r-1
            i = l

            while i <= rt:
                if nums[i] < pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    # we change i also here because every value before i is already <= pivot
                    # no need to verify again
                    i += 1
                    lt += 1
                elif nums[i] > pivot:
                    nums[i], nums[rt] = nums[rt], nums[i]
                    rt -= 1
                    # dont change i since we swapped value at rt to i
                    # that value needs to be compared with pivot in next round
                    # notice how we also do `while i <= rt` to facilitate another check
                else:
                    i += 1
            return lt, rt

        def quickSort(l, r):
            if l >= r:
                return
            
            lt, rt = partition(l, r)
            
            quickSort(l, lt - 1)
            quickSort(rt + 1, r)
        
        quickSort(0, len(nums)-1)
        return nums

