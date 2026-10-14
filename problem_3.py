class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # append to a dict = dict_name[new_key] = new_value
        characters = {}
        start_index = 0
        answer = 0

        for i, char in enumerate(s):
            if char in characters:
                old_occurance = characters[char]
                range_limit = old_occurance + 1

                if range_limit >= start_index:
                    start_index = old_occurance + 1

                characters[char] = i

                new_answer = (i-start_index) + 1

                if new_answer > answer:
                    answer = new_answer

            else:
                characters[char] = i

                new_answer = (i-start_index) + 1

                if new_answer > answer:
                    answer = new_answer

        return answer
