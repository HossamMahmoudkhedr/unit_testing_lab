class Calc:
    def factorial(n):
        fact = 1
        if not isinstance(n, int) or isinstance(n, bool) or n < 0:
            return None

        if n == 0:
            return fact
        else:
            for i in range(1, n+1):
                fact *= i
            return fact
