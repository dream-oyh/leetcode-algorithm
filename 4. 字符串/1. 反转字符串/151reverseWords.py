class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        i = 0
        word_list = []
        while i <= (len(s_list) - 1):
            if not s_list[i].isspace():
                temp = ""
                while i <= (len(s_list) - 1) and not s_list[i].isspace():
                    temp += s_list[i]
                    i += 1
                word_list.append(temp)
            i += 1

        return " ".join(self.reverse(word_list))

    def reverse(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        head = 0
        rear = len(s) - 1
        while head <= rear:
            temp = s[head]
            s[head] = s[rear]
            s[rear] = temp

            head += 1
            rear -= 1
        return s


so = Solution()
so.reverseWords("the sky is blue")
