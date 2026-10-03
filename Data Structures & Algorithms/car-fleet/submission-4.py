class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # pairs = [(p, s) for p, s in zip(position, speed)]
        # pairs.sort(reverse=True)
        pairs = sorted(zip(position, speed), reverse=True)

        fleets = 1
        prevTime = (target - pairs[0][0]) / pairs[0][1]
        for i in range(1, len(pairs)):
            currCar = pairs[i]
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets
