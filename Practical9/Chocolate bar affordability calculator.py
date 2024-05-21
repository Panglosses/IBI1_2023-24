def chocolate_bar_affordability(total_money, price_per_bar):
    bars_bought = int(total_money) // int(price_per_bar)
    
    change_left = int(total_money) % int(price_per_bar)
    
    return bars_bought, change_left


total_money = input("total_money= "+"")  
price_per_bar = input("price_per_bar= "+"")

bars_bought, change_left = chocolate_bar_affordability(total_money, price_per_bar)

print(f"You can buy {bars_bought} chocolate bars and you will have {change_left} left over.")