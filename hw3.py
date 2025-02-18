# 1. Oski Stole Your Power - Find a different way (by writing a function) that can compute x raised to the power of y
def computePower(x, y):
    n = 1
    for i in range (y):
        n *= x
    return n
x = 2
y = 3
print(computePower(x,y))

# 2. What Should I Wear? - Write a function that takes in a list as input and returns a tuple with the min and max as two values.
def temperatureRange(readings):
    return min(readings), max(readings)
readings = [15, 14, 17, 20, 23, 28, 20]
print(temperatureRange(readings)) 

# 3. Check if its the Weekend - Write a function that takes a day of the week and returns True if its a weekend and False if otherwise.
def isWeekend(day):
    return day == 6 or day == 7
print(isWeekend(6))

# 4. Fuel Efficiency Calculator - Write a function that takes the distance traveled (in miles) and the amount of fuel consumed (in gallons) as input and returns the fuel efficiency.
def fuel_efficiency(distance, fuel):
    return round(distance / fuel, 2)
distance = 70 # miles 
fuel = 21.5 # gallons
print(fuel_efficiency(distance, fuel))


# 5. Secret Code - Write a function that takes an integer as input and moves its last digit to the front of the number.
def decodeNumbers(n):
    # n % 10 will give last digit and n//10 will give first 4 digits
    ones = n % 10 
    n = n // 10 
    length = len(str(n))
    return ones * (10 ** length) + n
n = 12345
print(decodeNumbers(n))

# 6.1. For Loops - Write two functions to manually find the minimum and maximum values in a list of numbers with for loops.
def find_min_with_for_loop(nums):
    min_value = nums[0] 
    for i in nums:
        if i < min_value:
            min_value = i 
    return min_value

def find_max_with_for_loops(nums):
    max_value = nums[0]
    for i in nums:
        if i > max_value:
            max_value = i 
    return max_value

nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_for_loop(nums))
print(find_max_with_for_loops(nums))

# 6.2. While Loops - Write two functions to manually find the minimum and maximum values in a list of numbers with while loops.
def find_min_with_while_loop(nums):
    min_value = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] < min_value:
            min_value = nums[i]
        i += 1
    return min_value 

def find_max_with_while_loops(nums):
    max_value = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] > max_value:
            max_value = nums[i]
        i += 1
    return max_value

nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_while_loop(nums))
print(find_max_with_while_loops(nums))


# 7. Counting Vowels - Write a function that takes a string as an input and returns the number of vowels in the string and the number of consonants in the string as tuple.
def vowel_and_consonant_count(text):
    bank = "aeiouAEIOU"
    vowels = 0
    consonants = 0

    for char in text:
        if char.isalpha():
            if char in bank:
                vowels += 1
            else:
                consonants += 1
    return (vowels, consonants)

text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text))

# 8. Calculate Digital Root - Write a function that takes an integer as an input and returns the sum of its digits.
def digital_root(num):
    sum = 0 
    while num > 0:
        sum += num % 10 
        num //= 10 
    return sum
num = 2468
print(digital_root(num))