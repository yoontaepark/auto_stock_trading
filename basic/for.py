#for
#for문에서 i를 쓰면, 배열을 반복한다라는 의미

# for i in [1,2,3,4,5]:
#     print(i)

#range는 a이상 b미만의 값을 쭉 나타냄
#break는 해당 조건을 종료하고 나가는 부분
for i in range(0,10):
    print("%s 일째 복역 중 입니다." % (i+1))

    if i ==5:
        print("사면되었습니다")
        break;

#len은 변수의 총 횟수를 추출해줌
print("%s번 다 복역해서 자유가 되었습니다." % len(range(0,6)))

#count가 0에서 시작해서, 0~9번(총 10번) 1씩 더해라 이니 count가 10이 됨
count = 0
for i in range(0,10):
    count += 1
print(count)

#enumerate: 순서와 값을 모두 출력해줌
for i, value in enumerate(['키움', '삼성', '카카오']):
    print("%s 순번과 %s 값" % (i, value))