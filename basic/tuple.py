#tuple: 배열의 일종인데, 연산은 빠르나 수정이 안되는 단점이 있음, 걍 type 중 하나라고 보면 됨
#() 이런식으로

#case1
a_tuple = ("키움증권", "대신증권", "네이버증권")


count = 0
for value in a_tuple:
    print("%s 데이터, %s count" % (value, count))
    count += 1

#enumerate는 출력은 이쁘게 되는데 연산속도가 저하될 수 있음. 따라서, 동 프로젝트에서는 잘 안쓸 예정
for index, value in enumerate(a_tuple):
    print(index, value)

#case2
kiwoon_count = 0
for value in a_tuple:
    if value == "대신증권":
        kiwoon_count += 1

print("키움증권 매수량 : %s" % kiwoon_count)