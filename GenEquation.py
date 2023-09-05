import numpy as np
import matplotlib.pyplot as plt
# Function to generate a polynomial curve given a set of points

class AppliedMath:
    def __init__(self):
        self.coefficents = []
    def getCoefficents(self):
        return self.coefficents
    def generate_curve_from_points(self, points, degree=None):
        """
        Generate a polynomial curve based on a set of points and print the coefficients.
        
        Parameters:
            points (list of tuples): List of (x, y) coordinates.
            degree (int): Degree of the polynomial. If None, degree is set to number of points - 1.
                The higher the degree teh greater acurracy of the graph
            
        Returns:
            list: List of polynomial coefficients
        """
        # Extract x and y coordinates from the points
        x_coords = [point[0] for point in points]
        y_coords = [point[1] for point in points]
        
        # If degree is not specified, set it to number of points - 1
        if degree is None:
            degree = len(points) - 1
        
        # Fit a polynomial of given degree to the points
        coefficients = np.polyfit(x_coords, y_coords, degree)
        
        # Print the coefficients
        print(f"The coefficients for the polynomial curve are: {coefficients.tolist()}")
        
        self.coefficents = coefficients.tolist()


curve1 = AppliedMath()
example_points = [(0, 0), (3, 5), (6, 10), (9, 7), (10, 3)]  # Start, intermediate and end points
coefficients = curve1.generate_curve_from_points(example_points, 4)
print(curve1.getCoefficents())

