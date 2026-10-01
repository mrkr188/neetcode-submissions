class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert array to hash set for O(1) membership lookups
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # sequence start condition: only check if num - 1 is absent
            # this guarantees each element is processed at most twice -> O(N)
            if (num - 1) not in numSet:
                length = 1
                # expand sequence forward while consecutive elements exist
                while (num + length) in numSet:
                    length += 1

                # update maximum sequence length found
                longest = max(length, longest)

        return longest