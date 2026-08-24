class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # num -> count
        for num in nums:
            count[num] += 1
        
        res = []
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in count.items():
            buckets[count].append(num)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res