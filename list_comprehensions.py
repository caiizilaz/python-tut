prices = [5, 10, 50, 100]

dbl_prices = [price * 2 for price in prices]

print(dbl_prices)

nums = [1, 2, 3, 4, 5, 6]
sqr_even_nums = []

for num in nums:
    if(num**2) % 2 == 0:
        sqr_even_nums.append(num**2)
print(sqr_even_nums)

sqr_even_nums = [num**2 for num in nums if (num**2) % 2 == 0]

print(sqr_even_nums)