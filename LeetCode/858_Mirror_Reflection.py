# class Solution:
#     def mirrorReflection(self, p: int, q: int) -> int:
#         x, y = 0, 0
#         dx, dy = p, q

#         while True:
#             if dy == 0:
#                 return 0

#             # Time to reach a vertical wall
#             tx = (p - x) / dx if dx > 0 else (0 - x) / dx

#             # Time to reach a horizontal wall
#             ty = (p - y) / dy if dy > 0 else (0 - y) / dy

#             t = min(tx, ty)

#             x += dx * t
#             y += dy * t

#             if x == 0 or x == p:
#                 if y == p:
#                     return 2 if x == p else 1
#                 if y == 0:
#                     return 0

#                 dx = -dx

#             if y == 0 or y == p:
#                 dy = -dy







# Brute force:
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        x, y = 0, 0
        dx, dy = p, q

        while True:
            if dy == 0:
                return 0

            # Time to reach a vertical wall
            tx = (p - x) / dx if dx > 0 else (0 - x) / dx

            # Time to reach a horizontal wall
            ty = (p - y) / dy if dy > 0 else (0 - y) / dy

            t = min(tx, ty)

            x += dx * t
            y += dy * t

            if x == 0 or x == p:
                if y == p:
                    return 2 if x == p else 1
                if y == 0:
                    return 0

                dx = -dx

            if y == 0 or y == p:
                dy = -dy






# Optimal:
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p //= 2
            q //= 2

        if p % 2 == 0:
            return 2

        if q % 2 == 0:
            return 0

        return 1
