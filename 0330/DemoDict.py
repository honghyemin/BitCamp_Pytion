# DemeDict.py
d = dict(a=1, b=2, c=3)
print( type(d) )
print ( d )

color = { "apple":"red", "kiwi":"green"}
print( len(color))
print( color["apple"] )

# 두번째 예제
device = {"아이폰":5, "아이패드":10}
#입력
device["맥프레"] =15
print( len(device) )
print( device["아이폰"])

#수정
device["아이폰"] = 6
#삭제
del device["아이패드"]
print( device )
#반복구문
for item in device.items() :
    print(item)

for k,v in device.items():
    print(k,v)


#전화번호 예제
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print( type(phone) )
print( phone["kim"] )
# print( phone[0] ) -> [0]번째 인덱스라는 것이 없으므로 실행 오류
# 참조를 복사해서 대입한다.
p = phone
for item in p.items() : 
    print(item)

print( "moon" in phone)
# 주소 출력
print( id(phone), id(p))