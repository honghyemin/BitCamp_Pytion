# DemoFile.py
# 파일 객체를 리턴받기 (Write Text)
f = open("c:\\work\\demo.txt", "wt")
# newLine(줄바꿈)을 직접 코딩
f.write("한글을 출력\n")
f.write("abce\n1233\n")
f.close

# 파일을 읽기
f = open("c:\\work\\demo.txt", "rt")
# read()는 전체 라인을 읽어서 str로 리턴
print( f.read())
# 위치를 알려줌
print( f.tell())
# 리셋(처음으로 돌아감)
f.seek(0)
print( f.readline())
print( f.readline())
print( f.readline())
# 전체를 리스트로 받기
f.seek(0)
lst = f.readlines()
for item in lst:
    #print(item.replace("\n", ""))
    print(item, end="")

f.close()
print( f.closed )

# 기존 파일에 첨부를 하는 경우
print("=" * 15)
f = open("c:\\work\\demo.txt", "a+")
f.write("새로운 내용 추가4\n")
f.close

f = open("c:\\work\\demo.txt")
print( f.read( ) )
f.close()
