def apply_dicount(price,discount):
    if not isinstance(price,(int, float)):
        return "The price should be a number"
    elif not isinstance(discount,(int,float)):
        return "The discount should be a number"
    elif price <= 0:
        return "The price should be greater then zero"
    elif discount<0 or discount>100:
        return "the discount should be between 0 and 100"
    else:
        final_price=price-(price*discount/100)
        return final_price

print(apply_dicount(200,10))