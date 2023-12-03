# Method 1: Leibniz’s Formula
# This equation can be implementd in any programming language.
# Accuracy of value of pie depends on number of terms present in the equation which means high number of iterations produce better result.

# leibniz-formula {\displaystyle 1-{\frac {1}{3}}+{\frac {1}{5}}-{\frac {1}{7}}+{\frac {1}{9}}-\cdots ={\frac {\pi }{4}},}

# Implementation of Leibniz’s Formula:
# We will create 2 variables sum, d (denominator)
# Initialise sum = 0
# Initialise d = 1
# Create a for loop
# Loop i from 0 to 1000000 ( bigger number = more precsion )
# Check if i is even then sum=sum+4/d, else sum=sum-4/d
# Increment d by 2 every at every iteration
# Print sum

# Time Complexity:
# O(N * logN * loglogN), where
# N = number of iterations
# Division of two numbers of order O(N) takes O(logN loglogN) time.

# Code:
#Initialize denominator
d = 1
#Initialize sum
sum = 0
for i in range(0,1000000): # 6 zeroes for 16 digits 10 zeroes for 
    #even index add to sum
    if i % 2 == 0:
        sum += 4/d
    else:
    #odd index subtract from sum
        sum -= 4/d
#increment denominator by 2 
    d += 2

print("Value of Pi is : ",sum)