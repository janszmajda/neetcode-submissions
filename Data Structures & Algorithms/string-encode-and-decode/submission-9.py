class Solution:
    def encode(self, strs: List[str]) -> str:
        bigs = ""
        for elem in strs:
            if bigs == "":
                bigs += "👀"+elem+"👀"
            else:
                bigs += "😁" + "👀"+elem+"👀"
        return bigs
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        split = s.split("😁")
        ans = []
        for elem in split:
            no_periods = elem.split("👀")
            ans.append(no_periods[1])
        return ans

