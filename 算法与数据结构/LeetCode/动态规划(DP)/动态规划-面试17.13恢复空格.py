from typing import List
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        length = len(sentence)
        if length == 0: return 0
        if dictionary == [] : return len(sentence) 

        dictionary.sort(key = lambda x: len(x))
        dp = [0] * (length+1)
        dp[0] = 0

        for i in range(1,length+1): #i表示第i+1个字符
            dp[i] = dp[i-1] + 1
            for j in dictionary:
                if len(j) > i:
                    break
                if sentence[i-len(j):i] == j:
                    dp[i] = min(dp[i],dp[i-len(j)])
        return dp[-1]
s = Solution()
print(s.respace(["looked","just","like","her","brother"],"jesslookedjustliketimherbrother"))
print(s.respace([
"aaysaayayaasyya",
"yyas","yayysaaayasasssy",
"yaasassssssayaassyaayaayaasssasysssaaayysaaasaysyaasaaaaaasayaayayysasaaaa",
"aya","sya","ysasasy","syaaaa","aaaas","ysa","a","aasyaaassyaayaayaasyayaa",
"ssaayayyssyaayyysyayaasaaa","aya",
"aaasaay",
"aaaa",
"ayyyayssaasasysaasaaayassasysaaayaassyysyaysaayyasayaaysyyaasasasaayyasasyaaaasysasy",
"aaasa","ysayssyasyyaaasyaaaayaaaaaaaaassaaa",
"aasayaaaayssayyaayaaaaayaaays"
,"s"]
,"asasayaayaassayyayyyyssyaassasaysaaysaayaaaaysyaaaa"))