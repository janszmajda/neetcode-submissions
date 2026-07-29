class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #need to check if same length and if same counts of chars
        if len(s) != len(t):
            return False

        #have a dict where can see elements and their counts in s
        letter_dict = {}
        for elem in s:
            if elem not in letter_dict:
                letter_dict[elem] = 1
            else:
                letter_dict[elem] += 1
        
        elem_seen = []
        for elem in t:
            if elem not in elem_seen:
                count = t.count(elem)
                if elem not in letter_dict:
                    return False
                else:
                    if count != letter_dict[elem]:
                        return False
                elem_seen.append(elem)
        return True

