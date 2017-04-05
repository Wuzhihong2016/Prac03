"""
import random
print(random.randint(5, 20))        # line 1
print(random.randrange(3, 10, 2))   # line 2
print(random.uniform(2.5, 5.5))     # line 3
"""
#●	What did you see on line 1?
#What was the smallest number you could have seen, what was the largest?
#●	What did you see on line 2?
#What was the smallest number you could have seen, what was the largest?
#Could line 2 have produced a 4?
#●	What did you see on line 3?
#What was the smallest number you could have seen, what was the largest?
import random
MAX_INCREASE = 0.10  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
i = 0
price = INITIAL_PRICE
print("Starting price is ${:,.2f}".format(price))
while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)
    i += 1

    price *= (1 + price_change)
    print("On day {} price is :${:,.2f}".format(i, price))
