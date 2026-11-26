# Newton-Raphson Method
# x(i+1) = x(i) - f(x(i)) / f'(x(i))


# غيري الدالة ومشتقاتها هنا حسب المسألة
def f(x):
    return x**3 - x - 2


def df(x):      # المشتقة الأولى
    return 3 * x**2 - 1


def d2f(x):     # المشتقة الثانية
    return 6 * x


def newton_raphson(x0, tolerance=0.000001, max_iterations=50):
    # شرط التقارب: |f(x) * f''(x) / f'(x)^2| < 1
    if df(x0) != 0:
        condition = abs(f(x0) * d2f(x0) / df(x0) ** 2)
        print(f"Convergence condition at x0 = {condition:.6f}")
        if condition < 1:
            print("Condition satisfied (< 1)\n")
        else:
            print("Warning: condition not satisfied, try another x0\n")

    x = x0
    for i in range(max_iterations):
        if df(x) == 0:
            print("f'(x) = 0, cannot divide by zero. Try another x0.")
            return None

        x_new = x - f(x) / df(x)    # القانون
        print(f"x{i + 1} = {x_new:.6f}")

        # نقف لما الفرق بين قيمتين ورا بعض يبقى صغير جدا
        if abs(x_new - x) < tolerance:
            print(f"\nRoot = {x_new:.6f}")
            return x_new

        x = x_new

    print("Did not converge. Try another x0.")
    return None


x0 = float(input("Enter x0: "))
newton_raphson(x0)
