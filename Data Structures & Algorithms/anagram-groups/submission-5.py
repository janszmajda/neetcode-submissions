class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #have strs which is list of strings
        #want to iterate through strs and find anagrams to given element
        #then remove the elements and continue iteration

        big_L = []

        while len(strs) > 1:
            first_elem = strs[0]
            anagrams = [first_elem]
            for i in range(1,len(strs)):
                if self.isAnagram(first_elem, strs[i]):
                    anagrams.append(strs[i])
            big_L.append(anagrams)
            
            for elem in anagrams:
                strs.remove(elem)
        
        if len(strs) == 1:
            big_L.append([strs[0]])
            
        return big_L
    
    def isAnagram(self, s, t) -> bool:
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
            