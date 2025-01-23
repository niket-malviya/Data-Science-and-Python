import matplotlib.pyplot as plt
import numpy as np

class FunctionPlotter:
    def __init__(self, function, x_range=(-10, 10), step=0.1):
        self.function = function
        self.x_range = x_range
        self.step = step
        self.x_values = np.arange(self.x_range[0], self.x_range[1], self.step)
        self.y_values = None

    def calculate(self):
        """Calculate y-values for the function."""
        self.y_values = [self.function(x) for x in self.x_values]

    def save_graph(self, filename="function_plot.png"):
        """Generate and save the graph."""
        if self.y_values is None:
            raise ValueError("Calculate values before plotting.")
        plt.figure(figsize=(10, 6))
        plt.plot(self.x_values, self.y_values, label=f'{self.function.__name__}(x)', color='blue')
        plt.title(f"Graph of {self.function.__name__}")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
        plt.axvline(0, color='black', linewidth=0.5, linestyle="--")
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.savefig(filename)
        print(f"Graph saved as {filename}")

    def show_graph(self):
        """Display the graph."""
        plt.show()

# Advanced Decorator to Log Function Calls
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Execution of {func.__name__} complete.")
        return result
    return wrapper

# Decorate and Define Function
@log_execution
def quadratic_function(x):
    return x**2 - 4*x + 3

# Main Execution
if __name__ == "__main__":
    plotter = FunctionPlotter(quadratic_function, x_range=(-10, 10), step=0.5)
    plotter.calculate()
    plotter.save_graph("quadratic_function_plot.png")
    plotter.show_graph()

