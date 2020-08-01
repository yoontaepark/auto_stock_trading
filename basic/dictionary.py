# dictionary: 자리 순서가 없고 키와 값(value)의 페어만 있음
# {"key": value, "key": value} 꼴로 표현한다

# a_dict = {"종목명": "섬광글라스", "등락율(%)": 0.0, "고가대비(%)": -0.97, "보유수량": 0,
#           "현재가": 41050, "(최우선)매도호가": 41050}
# print(a_dict)
#
# # 키만 출력
# print(a_dict.keys())
#
# # 값만 출력
# print("키: %s, 값: %s" % ('등락율(%)', a_dict.get('등락율(%)')))
# # or
# print("키: %s, 값: %s" % ('등락율(%)', a_dict['등락율(%)']))
#
# #반복문으로도 출력가능
# for key in a_dict.keys():
#     print(key)
#     print(a_dict[key])

## 추가
b_dict = {"종목명": "섬광글라스", "등락율(%)": 0.0, "고가대비(%)": -0.97, "보유수량": 0,
          "현재가": 41050, "(최우선)매도호가": 41050}

# items function: enumerate랑 비슷
for key, value in b_dict.items():
    print("키: %s, 값: %s" % (key, value))

# update: 키가 있으면 해당 키에 대응하는 값을 변경시킴, 없는 경우 키:값을 신규로 추가해줌
b_dict.update({'종목명': '키움증권'})
b_dict.update({'보유수량': 5, '현재가': 5000})
b_dict.update({'신규키': 123456789})

print(b_dict)

#update2
b_dict['종목명'] = '한화증권'
b_dict['신규키2'] = 987654321

print(b_dict)

#실제로 프로그래밍에 사용하게될 예제
c_dict = {'023943': {'종목명': '삼광글라스', '등락률(%)': 0.0,'고가대비(%)': -0.97, '보유수량': 0, '현재가': 41050, '(최우선)매도호가': 41050}}
print(c_dict['023943']['종목명'])
print(c_dict.get('023943').get('고가대비(%)'))

print(c_dict.keys())
print(c_dict['023943'].keys())






