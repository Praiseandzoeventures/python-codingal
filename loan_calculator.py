import argparse
from math import isclose


def monthly_payment(principal: float, annual_rate_percent: float, years: int) -> float:
    """Return monthly payment for an amortizing loan.

    principal: loan amount
    annual_rate_percent: annual interest rate in percent (e.g. 5 for 5%)
    years: loan term in years
    """
    if years <= 0:
        raise ValueError("years must be > 0")
    n = years * 12
    r = annual_rate_percent / 100.0 / 12.0
    if isclose(r, 0.0):
        return principal / n
    return principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)


def total_payment(monthly: float, years: int) -> float:
    return monthly * years * 12


def total_interest(total_pay: float, principal: float) -> float:
    return total_pay - principal


def simple_interest(principal: float, annual_rate_percent: float, years: int) -> float:
    return principal * (annual_rate_percent / 100.0) * years


def format_money(x: float) -> str:
    return f"{x:,.2f}"


def run_example():
    principal = 10000.0
    rate = 5.0
    years = 3
    monthly = monthly_payment(principal, rate, years)
    tot = total_payment(monthly, years)
    interest = total_interest(tot, principal)
    print("Example loan:")
    print(f" Principal: {format_money(principal)}")
    print(f" Annual rate: {rate}%")
    print(f" Term: {years} years")
    print(f" Monthly payment: {format_money(monthly)}")
    print(f" Total payment: {format_money(tot)}")
    print(f" Total interest: {format_money(interest)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple loan math calculator")
    parser.add_argument("--principal", type=float, help="Loan principal amount")
    parser.add_argument("--rate", type=float, help="Annual interest rate (percent)")
    parser.add_argument("--years", type=int, help="Loan term in years")
    args = parser.parse_args()

    if args.principal is None or args.rate is None or args.years is None:
        run_example()
    else:
        p = args.principal
        r = args.rate
        y = args.years
        m = monthly_payment(p, r, y)
        tot = total_payment(m, y)
        intr = total_interest(tot, p)
        sim_intr = simple_interest(p, r, y)
        print(f"Principal: {format_money(p)}")
        print(f"Rate: {r}%")
        print(f"Term: {y} years")
        print(f"Monthly payment: {format_money(m)}")
        print(f"Total payment: {format_money(tot)}")
        print(f"Total interest (amortized): {format_money(intr)}")
        print(f"Total interest (simple interest): {format_money(sim_intr)}")
