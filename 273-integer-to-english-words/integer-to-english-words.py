class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        lookup = {
            1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine",
            10:"Ten",
            11:"Eleven",
            12:"Twelve",
            13:"Thirteen",
            14:"Fourteen",
            15:"Fifteen",
            16:"Sixteen",
            17:"Seventeen",
            18:"Eighteen",
            19:"Nineteen",
            20:"Twenty",
            30:"Thirty",
            40:"Forty",
            50:"Fifty",
            60:"Sixty",
            70:"Seventy",
            80:"Eighty",
            90:"Ninety"
        }
        digits = [(1000000000,"Billion"),(1000000,"Million"),(1000,"Thousand")]
        def convert(val):
            l = []
            if val>=100:
                v = val//100
                l.append(lookup[v])
                l.append("Hundred")
                val%=100
            if val>=20:
                v = (val//10)*10
                l.append(lookup[v])
                val%=10
            if val>0:
                l.append(lookup[val])
            return l
        ans = []
        for val,label in digits:
            if num>=val:
                v = num//val
                num%=val
                ans.extend(convert(v))
                ans.append(label)
        if num>0:
            ans.extend(convert(num))
        return ' '.join(ans)