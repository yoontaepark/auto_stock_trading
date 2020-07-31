#if문

stock_name = "대신증권"

if stock_name == "키움증권":
    print("키움증권이 맞네요")
elif stock_name != "카카오증권":
    print("카카오증권은 아니네요")
else:
    print("위의 조건값들 중 일치하는게 없네요")
#else는 안써도 if문이 출력되기는 함
# (주석넣는 단축키: ctrl + /)

#<, <=, >, >=,  =< 나 => 는 안됨(순서 유의)
stock_price = 3000
if stock_price < 2000:
    print("2000보다 작네요")
elif stock_price <= 3000:
    print("3000보다 작거나 같네요")

stock_rate = 2.5
if stock_rate > 2.5:
    print("2.5보다 크네요")
elif stock_rate >= 2.5:
    print("2.5 이상이네요")


#and는 걸린 조건문들을 모두 만족해야 됨, or는 걸린 조건문 중에 하나만 만족해도 됨
#in: 리스트 중에 하나
stock_name2 = "삼성전자"
if stock_name2 in ["lG", "APPLE", "MS", "삼성전자"]:
    print("삼성전자가 존재한다")

#섞어보기, 수식 도중 줄바꿈하면 \가 자동으로 붙거나 수기로 붙여줘야 함
stock_name3 = "삼성전자"
if stock_name3 in ["lG", "APPLE", "MS", "삼성전자"]\
        and (stock_name3 == "홈즈" or "삼성전자")\
        and stock_name3 != "가디언":
    print("리스트에 포함되어 있으면서, 회사이름은 홈즈이거나 삼성전자이고, 가디언과는 같지 않다")

