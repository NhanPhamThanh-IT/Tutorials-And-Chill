import math

# Import the math module, which provides access to mathematical functions.

print("--- Math Module Examples ---")

# --- Constants ---
print("\n--- Constants ---")
# The math module defines some useful mathematical constants.

# Pi (π): The ratio of a circle's circumference to its diameter.
print(f"Value of pi (math.pi): {math.pi}")

# Euler's number (e): The base of the natural logarithm.
print(f"Value of Euler's number (math.e): {math.e}")

# Infinity (inf): Represents positive infinity.
print(f"Positive infinity (math.inf): {math.inf}")
print(f"Negative infinity (-math.inf): {-math.inf}")

# Not a Number (nan): Represents an undefined or unrepresentable value.
print(f"Not a Number (math.nan): {math.nan}")


# --- Number-theoretic and Representation Functions ---
print("\n--- Number-theoretic and Representation Functions ---")

# math.ceil(x): Returns the ceiling of x, the smallest integer greater than or equal to x.
num_ceil = 4.2
print(f"Ceiling of {num_ceil} (math.ceil): {math.ceil(num_ceil)}") # Output: 5
num_ceil_neg = -4.8
print(f"Ceiling of {num_ceil_neg} (math.ceil): {math.ceil(num_ceil_neg)}") # Output: -4

# math.floor(x): Returns the floor of x, the largest integer less than or equal to x.
num_floor = 4.8
print(f"Floor of {num_floor} (math.floor): {math.floor(num_floor)}") # Output: 4
num_floor_neg = -4.2
print(f"Floor of {num_floor_neg} (math.floor): {math.floor(num_floor_neg)}") # Output: -5

# math.fabs(x): Returns the absolute value of x (as a float).
num_fabs = -10.5
print(f"Absolute value of {num_fabs} (math.fabs): {math.fabs(num_fabs)}") # Output: 10.5
# Note: The built-in abs() function can also compute absolute values and might return an int.
print(f"Absolute value using built-in abs(): {abs(-10)}") # Output: 10

# math.factorial(x): Returns the factorial of a non-negative integer x (x!).
# Factorial is n * (n-1) * (n-2) * ... * 1.
num_fact = 5
print(f"Factorial of {num_fact} (math.factorial): {math.factorial(num_fact)}") # Output: 120 (5*4*3*2*1)
# print(math.factorial(5.5)) # Raises ValueError: factorial() only accepts integral values
# print(math.factorial(-5)) # Raises ValueError: factorial() not defined for negative values

# math.gcd(a, b): Returns the greatest common divisor of two integers a and b. (Python 3.5+)
# The largest positive integer that divides both a and b without leaving a remainder.
num_gcd_a = 48
num_gcd_b = 18
print(f"Greatest Common Divisor of {num_gcd_a} and {num_gcd_b} (math.gcd): {math.gcd(num_gcd_a, num_gcd_b)}") # Output: 6

# math.trunc(x): Returns the truncated integer value of x (removes the fractional part).
num_trunc = 3.9
print(f"Truncated value of {num_trunc} (math.trunc): {math.trunc(num_trunc)}") # Output: 3
num_trunc_neg = -3.9
print(f"Truncated value of {num_trunc_neg} (math.trunc): {math.trunc(num_trunc_neg)}") # Output: -3
# Note: int() also truncates towards zero.
print(f"Truncated value using int(): {int(num_trunc)}") # Output: 3


# --- Power and Logarithmic Functions ---
print("\n--- Power and Logarithmic Functions ---")

# math.pow(x, y): Returns x raised to the power y (x^y). Result is always a float.
base = 2
exponent = 3
print(f"{base} raised to the power {exponent} (math.pow): {math.pow(base, exponent)}") # Output: 8.0
# Note: The ** operator can also be used for exponentiation.
print(f"{base} raised to the power {exponent} (using **): {base ** exponent}") # Output: 8 (might be int or float)

# math.sqrt(x): Returns the square root of x. x must be non-negative.
num_sqrt = 25
print(f"Square root of {num_sqrt} (math.sqrt): {math.sqrt(num_sqrt)}") # Output: 5.0
num_sqrt_float = 10
print(f"Square root of {num_sqrt_float} (math.sqrt): {math.sqrt(num_sqrt_float)}") # Output: 3.1622...
# print(math.sqrt(-4)) # Raises ValueError: math domain error

# math.exp(x): Returns e raised to the power x (e^x), where e is Euler's number.
num_exp = 2
print(f"e raised to the power {num_exp} (math.exp): {math.exp(num_exp)}") # Output: 7.389... (e^2)

# math.log(x[, base]): Returns the logarithm of x to the given base.
# If the base is not specified, it returns the natural logarithm (base e) of x.
num_log = 100
print(f"Natural logarithm (base e) of {num_log} (math.log): {math.log(num_log)}") # Output: 4.605...
# math.log(x, base) is equivalent to math.log(x) / math.log(base).
print(f"Logarithm base 10 of {num_log} (math.log): {math.log(num_log, 10)}") # Output: 2.0

# math.log10(x): Returns the base-10 logarithm of x. More accurate than math.log(x, 10).
print(f"Logarithm base 10 of {num_log} (math.log10): {math.log10(num_log)}") # Output: 2.0

# math.log2(x): Returns the base-2 logarithm of x. (Python 3.3+) More accurate than math.log(x, 2).
num_log2 = 8
print(f"Logarithm base 2 of {num_log2} (math.log2): {math.log2(num_log2)}") # Output: 3.0


# --- Trigonometric Functions ---
print("\n--- Trigonometric Functions ---")
# These functions operate on angles in radians.

angle_rad = math.pi / 4 # 45 degrees in radians

# math.sin(x): Returns the sine of x (x in radians).
print(f"Sine of {angle_rad:.4f} radians (math.sin): {math.sin(angle_rad):.4f}") # Output: 0.7071

# math.cos(x): Returns the cosine of x (x in radians).
print(f"Cosine of {angle_rad:.4f} radians (math.cos): {math.cos(angle_rad):.4f}") # Output: 0.7071

# math.tan(x): Returns the tangent of x (x in radians).
print(f"Tangent of {angle_rad:.4f} radians (math.tan): {math.tan(angle_rad):.4f}") # Output: 1.0000 (approx)

# Inverse trigonometric functions (return angles in radians)
sin_val = 0.5
# math.asin(x): Returns the arc sine (inverse sine) of x in radians.
print(f"Arc sine of {sin_val} (math.asin): {math.asin(sin_val):.4f} radians") # Output: 0.5236 (pi/6)

cos_val = 0.5
# math.acos(x): Returns the arc cosine (inverse cosine) of x in radians.
print(f"Arc cosine of {cos_val} (math.acos): {math.acos(cos_val):.4f} radians") # Output: 1.0472 (pi/3)

tan_val = 1.0
# math.atan(x): Returns the arc tangent (inverse tangent) of x in radians.
print(f"Arc tangent of {tan_val} (math.atan): {math.atan(tan_val):.4f} radians") # Output: 0.7854 (pi/4)

# math.atan2(y, x): Returns atan(y / x) in radians. The result is between -pi and pi.
# It considers the signs of both y and x to determine the correct quadrant.
y = 1
x = -1
print(f"Arc tangent of y={y}, x={x} (math.atan2): {math.atan2(y, x):.4f} radians") # Output: 2.3562 (3*pi/4)


# --- Angular Conversion ---
print("\n--- Angular Conversion ---")

# math.degrees(x): Converts angle x from radians to degrees.
angle_rad_convert = math.pi / 2 # 90 degrees
print(f"{angle_rad_convert:.4f} radians in degrees (math.degrees): {math.degrees(angle_rad_convert)}") # Output: 90.0

# math.radians(x): Converts angle x from degrees to radians.
angle_deg_convert = 180
print(f"{angle_deg_convert} degrees in radians (math.radians): {math.radians(angle_deg_convert):.4f}") # Output: 3.1416 (pi)


# --- Hyperbolic Functions ---
print("\n--- Hyperbolic Functions ---")
# Analogous to trigonometric functions but defined using the hyperbola rather than the circle.

val_hyp = 1
# math.sinh(x): Returns the hyperbolic sine of x.
print(f"Hyperbolic sine of {val_hyp} (math.sinh): {math.sinh(val_hyp):.4f}") # Output: 1.1752

# math.cosh(x): Returns the hyperbolic cosine of x.
print(f"Hyperbolic cosine of {val_hyp} (math.cosh): {math.cosh(val_hyp):.4f}") # Output: 1.5431

# math.tanh(x): Returns the hyperbolic tangent of x.
print(f"Hyperbolic tangent of {val_hyp} (math.tanh): {math.tanh(val_hyp):.4f}") # Output: 0.7616


# --- Special Functions ---
print("\n--- Special Functions ---")

# math.gamma(x): Returns the Gamma function at x.
# Related to the factorial function but defined for complex and real numbers.
# For positive integers n, gamma(n) = (n-1)!
num_gamma = 6
print(f"Gamma function at {num_gamma} (math.gamma): {math.gamma(num_gamma)}") # Output: 120.0 (same as 5!)

# math.lgamma(x): Returns the natural logarithm of the absolute value of the Gamma function at x.
# Often preferred over math.gamma() for large values to avoid overflow.
print(f"Natural log of Gamma at {num_gamma} (math.lgamma): {math.lgamma(num_gamma):.4f}") # Output: 4.7875 (log(120))

print("\n--- End of Math Module Examples ---")