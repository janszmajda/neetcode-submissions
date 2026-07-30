class Solution:
    def encode(self, strs: List[str]) -> str:
        bigs = ""
        for elem in strs:
            if bigs == "":
                bigs += "."+elem+"."
            else:
                bigs += "😁" + "."+elem+"."
        return bigs
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        split = s.split("😁")
        ans = []
        
        print(split)
        for elem in split:
            correct_elem = elem[1:len(elem) - 1]
            ans.append(correct_elem)
            
        return ans