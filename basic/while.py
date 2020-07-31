#while
#True면 무한반복, False가 되면 while문을 나옴
#case1
cnt = 0
while True:
    print("마법을 쓰기 위해 %s번째 시도를 하였다" % cnt)

    if cnt == 10:
        print("%s 번째 시도 끝에 마법을 써서 빠져나간다" % cnt)
        break
    cnt += 1

#case2
cnt = 0
repeat_boolean = True
while repeat_boolean:
    print("%s 아직은 while문 도는 중" % cnt)

    cnt += 1

    if cnt ==10:
        repeat_boolean = False

#case3
stock_price = 1000
while stock_price != 100000:
    stock_price += 1000
    print("방금 %s원을 더해서 %s원이 되었다." % (1000, stock_price))