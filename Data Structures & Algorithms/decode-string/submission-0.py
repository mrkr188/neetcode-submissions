class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []
        cur_char = ""
        cur_num = 0

        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == "[":
                string_stack.append(cur_char)
                count_stack.append(cur_num)
                cur_char = ""
                cur_num = 0
            elif c == "]":
                temp = cur_char
                cur_char = string_stack.pop()
                count = count_stack.pop()
                cur_char += temp * count
            else:
                cur_char += c

        return cur_char