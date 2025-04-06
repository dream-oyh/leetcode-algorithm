class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        head = 0
        rear = 0
        n = len(fruits)
        max_ans = 0
        
        kind_dict = {fruits[head]:1}

        while rear < n:
            if len(kind_dict) <= 2:
                max_ans = max(max_ans, rear - head + 1)
                rear += 1
                if rear >= n:
                    return max_ans
                if fruits[rear] not in kind_dict:
                    kind_dict[fruits[rear]] = 1
                else:
                    kind_dict[fruits[rear]] += 1
            else :
                head += 1
                if head >= n:
                    return max_ans
                kind_dict[fruits[head-1]] -= 1
                if kind_dict[fruits[head-1]] == 0:
                    kind_dict.pop(fruits[head-1])
        return max_ans
so = Solution()
print(so.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))