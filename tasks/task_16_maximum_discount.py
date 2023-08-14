def MaximumDiscount(n: int, price: list[int]) -> int:
    sorted_prices = sorted(price, reverse=True)

    total_discount = 0
    while len(sorted_prices) >= 3:
        total_discount += sorted_prices[2]
        sorted_prices = sorted_prices[3:]

    return total_discount
