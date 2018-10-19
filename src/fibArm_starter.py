#!/usr/bin/env python3
"""myMorseGenerator_solution.py: Program to use generator functions to put text into morse code."""

__author__      = "ADD YOUR NAME!!!"
__date__        = "18 Oct 2018"



def fibsList(n):
# stavely's chapter 7
    result = [ ]
    a=1
    b=1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
# end of FibList()



def fibByArm(m, gRatio_flt):
# The function to compute the fibonacci sequence based on the golden ratio
# m is a previous term, and gRatio_flt is the Golden Ratio (Phi)
    print("")
#   TODO: calculate some value and return it

#end of fibByArm()


def main():
    print("  Welcome to the Fibonacci Sequence calculator using the Golden Ratio which has been prepared from measurments of your arm. ")

# get user input (As floats) for both measurements
#    sf_flt = input(" Length of shoulder tip of longest finger : ")
#    ef_flt = input(" Length of elbow to tip of longest finger : ")

#   TODO: add code to work with these measurments

    print(" The Real Fibonacci Sequence:")
    print(fibsList(10))
#end of main()



# this is used for the math.ciel() function that rounds up values to nearest integer
import math
if __name__ == "__main__":
	main()
