
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

def rysuj_wielomian(wejscie):
    """
    Parses input string using eval() and plots the function.
    Input format: "expression, start end"
    """
    # Split input into the formula and the range
    formula, bounds = wejscie.split(',')
    start, end = map(float, bounds.split())

    # Generate x values
    x_val = np.linspace(start, end, 400)
    
    # Calculate y values using eval()
    # Note: we provide a dict to eval so it knows 'x' and 'np' functions
    y_val = [eval(formula, {"x": x, "sin": np.sin, "cos": np.cos, "exp": np.exp}) for x in x_val]
    y_val = np.array(y_val)

    # Plotting
    plt.figure()
    plt.plot(x_val, y_val, label=f"eval: {formula}")
    plt.title("Function Plot (eval)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()

    # Return values at the boundaries
    return y_val[0], y_val[-1]

def rysuj_wielomian_sympy(wejscie):
    """
    Parses input string using SymPy and lambdify() for numerical plotting.
    """
    # Split input into the formula and the range
    formula_str, bounds = wejscie.split(',')
    start, end = map(float, bounds.split())

    # Define the symbol and convert string to SymPy expression
    x = symbols('x')
    expr = sympify(formula_str)
    
    # Convert SymPy expression to a fast numerical function (numpy-based)
    f_numerical = lambdify(x, expr, "numpy")

    x_val_sympy = np.linspace(start, end, 400)
    y_val_sympy = f_numerical(x_val_sympy)

    plt.figure()
    plt.plot(x_val_sympy, y_val_sympy, color='red', label=f"SymPy: {formula_str}")
    plt.title("Function Plot (SymPy)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()

    return y_val_sympy[0], y_val_sympy[-1]

if __name__ == '__main__':
    input1 = "x**3 - 3*x**2 + 3*x - 1, -2 2"
    result_eval = rysuj_wielomian(input1)
    print("Result (eval):", result_eval)
    
    input2 = "x**4 - 5*x**2 + 3*sin(x), -10 10"  
    result_sympy = rysuj_wielomian_sympy(input2)
    print("Result (SymPy):", result_sympy)
    
    plt.show()
