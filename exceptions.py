 #Exceptions
go_Wipe_Characteristics= ['Antibacterial', 'Food Safe', 'Gentle enough for infant', 'non-toxic', 'alcohol free', '100% biodegradable', 'cleaning utility']
go_Wipe_Characteristics.remove(1)
print(go_Wipe_Characteristics)
biggest_losers_last_day_percentage_drop= {'FTX Token': 7.5}, {'Amp': 3.2}, {'Quant': 2.8}, {'Uniswap': 2.8}
biggest_losers_last_day_percentage_drop['FTX Token']
x=-5
if x <0:
    raise Exception('x should be positive')
try:
    a=5/1
    b = a+4
except ZeroDivisionError as e:
        print(e)
except TypeError as e:
        print(e)
else:
        print('IT IS FINE')
class ValueTooHighError(Exception):
    pass
def test_value(x):
    if x > 100:
        raise ValueTooHighError('value too high')
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)