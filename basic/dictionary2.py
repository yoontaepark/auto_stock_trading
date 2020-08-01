#dictionary 활용

a_dict = {'키움증권': 5000, '카카오': 3000, '네이버': 2000, '애플': 1000000}
my_account = 1110000

for data in a_dict.keys():
    if data =='키움증권':
        my_account -= a_dict[data] * 5
    elif data =='카카오':
        my_account -= a_dict[data] * 2
    elif data =='네이버':
        my_account -= a_dict[data] * 5

print("남은 금액 %s" % my_account)

#while(추가예제)
b_dict = {'키움증권': 5000, '카카오': 3000, '네이버': 2000, '애플': 1000000}
ee_bool = True

while ee_bool:
    b_dict['키움증권'] += 1000

    if b_dict['키움증권'] == 10000:
        b_dict.update({'키움증권':0})
        break;

print(b_dict)