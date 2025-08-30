import math
from statistics import mean
import colorama

colorama.init()


class LeastSquares:
    def __init__(self, x, y, rounding=2, with_errors=False):
        if len(x) != len(y):
            raise ValueError("X and Y must have the same length.")
        if len(x) < 2:
            raise ValueError("At least 2 points are required.")

        self.x = x
        self.y = y
        self.n = len(x)
        self.rounding = rounding
        self.with_errors = with_errors

        # Основні величини
        self.x2 = [xi**2 for xi in x]
        self.y2 = [yi**2 for yi in y]
        self.xy = [xi * yi for xi, yi in zip(x, y)]

        self.S_X2 = mean(self.x2) - mean(x) ** 2
        self.S_Y2 = mean(self.y2) - mean(y) ** 2
        self.R_XY = mean(self.xy) - mean(x) * mean(y)

        if self.S_X2 == 0:
            raise ZeroDivisionError("All X values are the same → regression cannot be computed.")

        # Коефіцієнти
        self.alpha = self.R_XY / self.S_X2
        self.beta = mean(y) - self.alpha * mean(x)

    def table(self):
        """Повертає таблицю x, y, x^2, y^2, xy."""
        header = f"{'x':>8} {'y':>8} {'x^2':>8} {'y^2':>8} {'xy':>8}"
        rows = [f"{xi:8.3f} {yi:8.3f} {xi2:8.3f} {yi2:8.3f} {xy:8.3f}"
                for xi, yi, xi2, yi2, xy in zip(self.x, self.y, self.x2, self.y2, self.xy)]
        return header + "\n" + "\n".join(rows)

    def formula(self):
        """Повертає формулу у вигляді рядка."""
        a = round(self.alpha, self.rounding)
        b = round(self.beta, self.rounding)
        return f"Y = {a} * X + {b}"

    def errors(self):
        """Обчислює похибки та кореляцію (якщо потрібно)."""
        if not self.with_errors:
            return None
        if self.n < 3:
            raise ValueError("At least 3 points required to compute errors.")

        delta_a = round(2 * math.sqrt((self.S_Y2 / self.S_X2 - self.alpha ** 2) / (self.n - 2)), self.rounding)
        delta_b = round(delta_a * math.sqrt(self.S_X2 + mean(self.x) ** 2), self.rounding)

        epsilon_a = round(abs(delta_a / self.alpha) * 100, self.rounding) if self.alpha else 100
        epsilon_b = round(abs(delta_b / self.beta) * 100, self.rounding) if self.beta else 0

        r_cov = round(self.R_XY / math.sqrt(self.S_Y2 * self.S_X2), self.rounding) if self.S_Y2 else 0

        return {
            "delta_a": delta_a,
            "delta_b": delta_b,
            "epsilon_a": epsilon_a,
            "epsilon_b": epsilon_b,
            "r": r_cov,
        }

    def __str__(self):
        result = colorama.Fore.CYAN + "Table of values:\n" + colorama.Fore.RESET
        result += self.table() + "\n\n"

        result += colorama.Fore.BLUE + "Formula: " + colorama.Fore.RESET + "\n"
        result += colorama.Style.BRIGHT + self.formula() + "\n" + colorama.Style.RESET_ALL
        if self.with_errors:
            errs = self.errors()
            result += (f"Absolute errors: A = {errs['delta_a']}, B = {errs['delta_b']}\n"
                       f"Relative errors: A = {errs['epsilon_a']}%, B = {errs['epsilon_b']}%\n"
                       f"Correlation coefficient: r = {errs['r']}\n")
        return result


def get_floats(prompt):
    """Зчитування чисел з input."""
    try:
        values = input(colorama.Fore.GREEN + prompt + ": \n" + colorama.Fore.RESET).strip()
        numbers = list(map(float, values.split()))
        if not numbers:
            raise ValueError
        return numbers
    except ValueError:
        print(colorama.Fore.RED + "Invalid input! Use numbers separated by spaces." + colorama.Fore.RESET)
        return None


def main():
    print(colorama.Style.BRIGHT + "\n  --- # STARTING PROGRAM # --- " + colorama.Style.RESET_ALL)
    print(colorama.Fore.BLACK + colorama.Back.WHITE +
          "\nThis program finds linear dependency between X and Y using the Least Squares Method\n" +
          colorama.Back.RESET + colorama.Fore.RESET)

    x = get_floats("Input values of X-s with spaces")
    if not x: return
    y = get_floats("Input values of Y-s with spaces")
    if not y: return

    try:
        rounding = int(input("Number of decimal places: "))
        if rounding < 0:
            raise ValueError
    except ValueError:
        print(colorama.Fore.RED + "Invalid rounding value." + colorama.Fore.RESET)
        return

    with_errors = input("Enter 1 for errors & correlation coefficient: ").strip() == "1"

    try:
        model = LeastSquares(x, y, rounding, with_errors)
        print(model)
    except Exception as e:
        print(colorama.Fore.RED + f"Error: {e}" + colorama.Fore.RESET)

    print(colorama.Fore.YELLOW + "Hope this was helpful." + colorama.Fore.RESET)
    print(colorama.Style.BRIGHT + colorama.Fore.RED + "\n --- # ENDING PROGRAM # --- " + colorama.Style.RESET_ALL)


if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
