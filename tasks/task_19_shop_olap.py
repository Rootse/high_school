def ShopOLAP(n: int, items: list[str]) -> list[str]:
    sales_dict = {}
    for record in items:
        name, sold = record.split()
        sold = int(sold)

        if name in sales_dict:
            sales_dict[name] += sold
        else:
            sales_dict[name] = sold

    output = []
    for name, sold in sorted(sales_dict.items(), key=lambda x: (-x[1], x[0])):
        output.append(f"{name} {sold}")

    return output
