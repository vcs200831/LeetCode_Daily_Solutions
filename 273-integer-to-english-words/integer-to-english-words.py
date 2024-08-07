class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        below_20 = [
            "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
            "Eighteen", "Nineteen"
        ]
        tens = [
            "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n: int) -> str:
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n - 1] + " "
            elif n < 100:
                return tens[n // 10 - 2] + " " + helper(n % 10)
            else:
                return below_20[n // 100 - 1] + " Hundred " + helper(n % 100)
        
        def convert(num: int) -> str:
            result = ""
            for i, v in enumerate(thousands):
                if num == 0:
                    break
                if num % 1000 != 0:
                    result = helper(num % 1000) + v + " " + result
                num //= 1000
            return result
        
        return convert(num).strip()

# Example usage:
sol = Solution()
print(sol.numberToWords(123))         # "One Hundred Twenty Three"
print(sol.numberToWords(12345))       # "Twelve Thousand Three Hundred Forty Five"
print(sol.numberToWords(1234567))     # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
