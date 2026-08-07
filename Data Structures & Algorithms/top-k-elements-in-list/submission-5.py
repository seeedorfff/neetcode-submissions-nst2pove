class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in count.items():
            buckets[count].append(num)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res