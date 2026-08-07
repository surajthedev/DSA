# You are given a string num which represents a positive integer, and an integer t.

# A number is called zero-free if none of its digits are 0.

# Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible by t. If no such number exists, return "-1".

 

# Example 1:

# Input: num = "1234", t = 256

# Output: "1488"

# Explanation:

# The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

# Example 2:

# Input: num = "12355", t = 50

# Output: "12355"

# Explanation:

# 12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.

# Example 3:

# Input: num = "11111", t = 26

# Output: "-1"

# Explanation:

# No number greater than 11111 has the product of its digits divisible by 26.

 

# Constraints:

# 2 <= num.length <= 2 * 105
# num consists only of digits in the range ['0', '9'].
# num does not contain leading zeros.
# 1 <= t <= 1014




# Solution:
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        FACTORS = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        # --------------------------------------------------
        # Factorize t = 2^a * 3^b * 5^c * 7^d
        # --------------------------------------------------

        target = [0, 0, 0, 0]
        primes = [2, 3, 5, 7]

        for i, p in enumerate(primes):
            while t % p == 0:
                target[i] += 1
                t //= p

        # Agar 2,3,5,7 ke alawa koi prime factor hai
        if t != 1:
            return "-1"

        A, B, C, D = target

        # --------------------------------------------------
        # DP for factors of 2 and 3
        # dp[a][b] = minimum digits required
        # to get at least 2^a * 3^b
        # --------------------------------------------------

        INF = 10**9

        dp = [[INF] * (B + 1) for _ in range(A + 1)]
        dp[0][0] = 0

        digits_23 = [2, 3, 4, 6, 8, 9]

        for a in range(A + 1):
            for b in range(B + 1):

                if a == 0 and b == 0:
                    continue

                for digit in digits_23:
                    x, y, _, _ = FACTORS[digit]

                    pa = max(0, a - x)
                    pb = max(0, b - y)

                    dp[a][b] = min(
                        dp[a][b],
                        dp[pa][pb] + 1
                    )

        def min_digits_needed(req):
            """
            req = remaining factors of 2,3,5,7
            """
            a, b, c, d = req
            return dp[a][b] + c + d

        def subtract(req, digit):
            f = FACTORS[digit]

            return (
                max(0, req[0] - f[0]),
                max(0, req[1] - f[1]),
                max(0, req[2] - f[2]),
                max(0, req[3] - f[3]),
            )

        # --------------------------------------------------
        # Build smallest suffix of EXACT length
        # --------------------------------------------------

        def build_suffix(length, req):

            ans = []

            for pos in range(length):

                remaining = length - pos - 1

                for digit in range(1, 10):

                    new_req = subtract(req, digit)

                    if min_digits_needed(new_req) <= remaining:
                        ans.append(str(digit))
                        req = new_req
                        break

            return ''.join(ans)

        # --------------------------------------------------
        # Check whether num itself is valid
        # --------------------------------------------------

        if '0' not in num:

            have = [0, 0, 0, 0]

            for ch in num:
                f = FACTORS[int(ch)]

                for j in range(4):
                    have[j] += f[j]

            if all(have[j] >= target[j] for j in range(4)):
                return num

        n = len(num)

        # --------------------------------------------------
        # Prefix factor counts
        # --------------------------------------------------

        total = [0, 0, 0, 0]

        for ch in num:
            f = FACTORS[int(ch)]

            for j in range(4):
                total[j] += f[j]

        # Factors coming from positions AFTER i
        after = [0, 0, 0, 0]

        # --------------------------------------------------
        # Same length answer
        # --------------------------------------------------

        for i in range(n - 1, -1, -1):

            # Agar num[i] se pehle zero hai,
            # then this position cannot be changed while
            # keeping prefix zero-free.
            if '0' not in num[:i]:

                current_digit = int(num[i])
                current_f = FACTORS[current_digit]

                # Factors contributed by prefix [0 ... i-1]
                prefix = [
                    total[j] - current_f[j] - after[j]
                    for j in range(4)
                ]

                # Current digit ko smallest possible
                # larger digit se replace karo.
                for digit in range(current_digit + 1, 10):

                    f = FACTORS[digit]

                    req = (
                        max(0, target[0] - prefix[0] - f[0]),
                        max(0, target[1] - prefix[1] - f[1]),
                        max(0, target[2] - prefix[2] - f[2]),
                        max(0, target[3] - prefix[3] - f[3]),
                    )

                    suffix_len = n - i - 1

                    if min_digits_needed(req) <= suffix_len:

                        suffix = build_suffix(
                            suffix_len,
                            req
                        )

                        return (
                            num[:i]
                            + str(digit)
                            + suffix
                        )

            # num[i] ko "after" mein add karo
            f = FACTORS[int(num[i])]

            for j in range(4):
                after[j] += f[j]

        # --------------------------------------------------
        # Need a longer number
        # --------------------------------------------------

        minimum_length = min_digits_needed(tuple(target))

        length = max(n + 1, minimum_length)

        return build_suffix(length, tuple(target))