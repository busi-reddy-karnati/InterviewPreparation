class Solution:
    def numberToWords(self, num: int) -> str:
        def process_tens(num): #exclusively for 10's 10-19
            tens = {
                0:"Ten",
                1:"Eleven",
                2:"Twelve",
                3:"Thirteen",
                4:"Fourteen",
                5:"Fifteen",
                6:"Sixteen",
                7:"Seventeen",
                8:"Eighteen",
                9:"Nineteen"
            }
            return tens[num]
        def process_num(num): # This is for decoding a 3 digit number
            tens_map = {2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety"}
            ones_map = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
            hundreds = num // 100
            num = num % 100
            tens = num // 10
            num = num % 10
            ones = num
            li = []
            if tens == 1:
                li.append(process_tens(ones))
            else:
                if ones > 0:
                    li.append(ones_map[ones])
                if tens > 1:
                    li.append(tens_map[tens])
            if hundreds > 0:
                li.append("Hundred")
                li.append(ones_map[hundreds])
            # li.reverse()
            return li
        if num == 0:
            return "Zero"
        ones = num % 1000
        num = num // 1000
        hundreds = num % 1000
        num = num // 1000
        millions = num % 1000
        num = num // 1000
        billions = num % 1000
        ans = []
        # print(ans)
        if ones > 0:
            for i in process_num(ones):
                ans.append(i)
        if hundreds > 0:
            ans.append("Thousand")
            for i in process_num(hundreds):
                ans.append(i)
            # ans.append(i for i in process_num(hundreds))
        if millions > 0:
            ans.append("Million")
            for i in process_num(millions):
                ans.append(i)
            # ans.append(i for i in process_num(millions))
        if billions > 0:
            ans.append("Billion")
            for i in process_num(billions):
                ans.append(i)
            # ans.append(i for i in process_num(billions))
        ans.reverse()
        # print(ans)
        return " ".join(ans)