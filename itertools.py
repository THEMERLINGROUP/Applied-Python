from itertools import product, combinations, permutations, combinations_with_replacement, accumulate, groupby, cycle, repeat
import operator
Songs=['Running up that Hill', 'Seeing Green', 'Desires']
Song_Artists=['Kate Bush', 'Lil Wayne', 'Drake']
prod = product(Songs, Song_Artists)
print(list(prod))
Verizon_Consumer_Products=['Galaxy Buds2', 'AirPods Pro', 'Apple iPhone12']
Verizon_Business_Products=['5G devices', 'BlueJeans by Verizon', 'Verizon Partners Solutions']
print(list(prod))
a=[1,2,3]
perm = permutations(a, 2)
print(list(perm))
Amazon_Electronics = ['Fire Stick', 'Amazon Smart Plug', 'Echo Dot', 'Roku', 'Wyze Cam Spotlight']
comb = combinations(Amazon_Electronics, 3)
print(list(comb))
comb_wr=combinations_with_replacement(Amazon_Electronics, 2)
print(list(comb_wr))
Zulay_Best_Sellers = ['Milk Frother Electric Handheld Foam Maker', 'Professional Heavy Duty Citrus Juicer', 'Quality Metal Lemon Lime Squeezer Manual Citrus Press Juicer']
acc = accumulate(Zulay_Best_Sellers)
print(Zulay_Best_Sellers)
print(list(acc))
#Numbers are fictional
sales=[250000, 300000, 500000]
acc=accumulate(sales, func=operator.mul)
print(sales)
print(list(sales))
def smaller_than_40(x):
    return x < 40

#In Seconds
World_Record_Swim_Times=[20.91,46.91,85.2, 204, 23, 240]
group_obj=groupby(World_Record_Swim_Times, key=lambda x:x<40)
for key, value in group_obj:
    print(key, list(value))
#USD prices
highest_gainers_crypto = [{'name': 'FTX Token', 'price':63.15 }, {'name':'Fantom', 'price':0.915686},
{'name':'IOTA', 'price':1.12}, {'name':'Sushi', 'price':13.48}, {'name':'Avalanche', 'price':43.77}] 
group_obj_2 = groupby(highest_gainers_crypto, key=lambda x: x['price'])
for key, value in group_obj_2:
    print(key, list(value))
super_bowl_scores=[{'Winner':'Kansas City', 'Loser':'San Francisco', 'score': 31-20}, {'Winner':'New England', 'Loser':'Los Angeles', 'score': 13-3}, {'Winner':'Philadelphia', 'Loser':'New England', 'score':41-33}, {'Winner':'New England', 'Loser':'Atlanta', 'score':34-28}]
group_sports_obj=groupby(super_bowl_scores, key=lambda x:x['Winner'])
for key, value in group_sports_obj:
    print(key, list(value))
a = [2,4,8,16,32,64,128,256]
for i in cycle(a):
    print(i)
b = [8,16,32,64,128]
for i in repeat[8,50]:
    print(i)
