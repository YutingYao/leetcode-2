"""
Valid Starting City:
Imagine you have a set of cities that are laid out in a circle, connected by a circular road that runs clockwise. 
Each city has a gas station that provides gallons of fuel, and each city is some distance away from the next city.
You have a car that can drive some number of miles per gallon of fuel, and your goal is to pick a starting city such that you can fill up your car with that city's fuel,
 drive to the next city, refill up your car with that city's fuel, drive to the next city,
  and so on and so forth until you return back to the starting city with 0 or more gallons of fuel left.
This city is called a valid starting city, and it's guaranteed that there will always be exactly one valid starting city.
For the actual problem, you'll be given an array of distances such that city i is distances[i] away from city i + 1.
Since the cities are connected via a circular road, the last city is connected to the first city.
In other words, the last distance in the distances array is equal to the distance from the last city to the first city.
You'll also be given an array of fuel available at each city, where fuel[i] is equal to the fuel available at city i.
The total amount of fuel available (from all cities combined) is exactly enough to travel to all cities.
Your fuel tank always starts out empty, and you're given a positive integer value for the number of miles that your car can travel per gallon of fuel (miles per gallon, or MPG).
You can assume that you will always be given at least two cities.
Write a function that returns the index of the valid starting city.

Sample Input
    distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10
Sample Output
    4

https://www.algoexpert.io/questions/Valid%20Starting%20City
"""


def validStartingCity(distances, fuel, mpg):
    start = 0
    end = 0
    miles_remaining = 0
    visited = 1

    while visited < len(distances):

        miles_if_move = miles_remaining - distances[end] + (fuel[end]*mpg)

        # is a valid move
        if miles_if_move >= 0:
            miles_remaining = miles_if_move
            visited += 1
            end = movePointerForward(distances,  end)

        # not a valid move -> move start forward
        else:
            if end == start:
                end += 1  # move to where start will be
                miles_remaining = 0
                visited = 1
            else:
                miles_remaining = miles_remaining + \
                    distances[start] - (fuel[start]*mpg)
                visited -= 1
            start += 1

    return start


def movePointerForward(array, pointer):
    if pointer + 1 < len(array):
        return pointer + 1
    return 0


"""
[0,1,2,3]
start = 0

# if we areach a point where we will have < 0 fuel when we move forward,
# we pause and start += 1 and remove the effects of the starting point:
# remove fuel added and add fuel spent
"""
