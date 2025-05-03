import math

array = [1.35,1.37,1.41,1.47,1.54,1.63,1.74,1.86,2.00,2.12,2.17,2.22,2.27,2.41,2.54,2.71,2.82,3.14,5.05,7.02,8.61,9.83,10.05,10.29,10.48,10.64,10.74,10.83,10.90,11.07,11.17,11.23,11.30,11.32,11.35,11.37,11.40,11.41,11.43,11.44,11.45,11.47,11.48,11.49,11.50,11.51,11.52,11.53,11.54,11.55,11.55,11.56,11.57,11.58,11.58,11.59,11.60,11.61,11.63,11.64,11.64,11.64,11.65,11.65,11.65,11.66]

def calculate_standard_deviation(numbers):

    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    # Calculate the mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate the squared differences from the mean
    squared_diffs = [(x - mean) ** 2 for x in numbers]
    
    # Calculate the variance
    variance = sum(squared_diffs) / len(numbers)
    
    # Calculate the standard deviation
    std_deviation = math.sqrt(variance)
    
    return std_deviation

# Example usage
print("Standard Deviation:", calculate_standard_deviation(array))