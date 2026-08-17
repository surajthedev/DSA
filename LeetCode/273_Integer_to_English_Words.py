# Convert a non-negative integer num to its English words representation.

 

# Example 1:

# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:

# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:

# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

# Constraints:

# 0 <= num <= 231 - 1






# Brute force:
class Solution:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        ones = [
            "", "One", "Two", "Three", "Four",
            "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty",
            "Ninety"
        ]

        def helper(n):
            if n < 20:
                return ones[n]

            if n < 100:
                return tens[n // 10] + (
                    " " + ones[n % 10] if n % 10 else ""
                )

            return (
                ones[n // 100]
                + " Hundred"
                + (" " + helper(n % 100) if n % 100 else "")
            )

        result = []

        if num >= 1_000_000:
            result.append(helper(num // 1_000_000))
            result.append("Million")
            num %= 1_000_000

        if num >= 1_000:
            result.append(helper(num // 1_000))
            result.append("Thousand")
            num %= 1_000

        if num > 0:
            result.append(helper(num))

        return " ".join(result)







# Optimal:
class Solution:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        below_20 = [
            "", "One", "Two", "Three", "Four",
            "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty",
            "Ninety"
        ]

        def convert(n):
            """
            Convert a number from 1 to 999
            into English words.
            """

            if n < 20:
                return below_20[n]

            if n < 100:
                return tens[n // 10] + (
                    " " + below_20[n % 10]
                    if n % 10
                    else ""
                )

            return (
                below_20[n // 100]
                + " Hundred"
                + (
                    " " + convert(n % 100)
                    if n % 100
                    else ""
                )
            )

        scales = [
            "",
            "Thousand",
            "Million",
            "Billion"
        ]

        result = []
        scale_index = 0

        while num > 0:
            chunk = num % 1000

            if chunk != 0:
                words = convert(chunk)

                if scales[scale_index]:
                    words += " " + scales[scale_index]

                result.append(words)

            num //= 1000
            scale_index += 1

        # Chunks were processed from right to left
        return " ".join(reversed(result))