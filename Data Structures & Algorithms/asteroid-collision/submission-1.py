class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # collide when current moves left (< 0) and stack top moves right (> 0)
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()  # stack top destroyed; current keeps moving left
                elif diff > 0:
                    a = 0  # current destroyed; stack top survives
                else:
                    a = 0  # both destroyed if equal size
                    stack.pop()

            # save current asteroid if it survived or had no collision
            if a != 0:
                stack.append(a)

        return stack

