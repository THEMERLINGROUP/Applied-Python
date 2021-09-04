#lambda arguments: expression 
#map(func, seq)
from functools import reduce
add1 = lambda x: x+1
print(add1(5))
#Using mult function with lambda
sales_volume = lambda inventory_sales_volume,by_year: inventory_sales_volume*by_year 
print(sales_volume(878477775,12))
inventory_turnover_ratio = lambda COGS,average_inventory: COGS/average_inventory
print(inventory_turnover_ratio(200000,50000))
cryptocurrencies= [('Bitcoin',50603.40), ('Bitcoin Cash ABC', 263.85), ('Solana', 141.50)]
cryptocurrencies_sorted= sorted(cryptocurrencies, key=lambda x:x[1])
print(cryptocurrencies)
print(cryptocurrencies_sorted)
home_run_leaders = [('Shohei Ohtani', 42), ('Vladimir Guerrero', 39), ('Salvador Perez', 38), ('Fernando Tatis Jr.', 36), ('Marcus Semien', 33)]
home_run_leaders_sorted = sorted(home_run_leaders, key=lambda x: x[0] + x[1])
print(home_run_leaders)
print(home_run_leaders_sorted)
a = [1,2,3,4,5]
b=map(lambda x: x*2, a)
print(list(b))
a=[2,5,89,55,666,88,72]
b=filter(lambda x: x%2==0, a)
print(list(b))
a=[12,66,62,39,54]
product_a = reduce(lambda x,y: x*y, a)
print(product_a)

