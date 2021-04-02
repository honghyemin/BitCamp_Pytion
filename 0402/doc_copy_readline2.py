# 정규 표현식 모듈
import re 

# 원본파일과 복사본 만들기
# 원본 로그 파일을 읽기(유니코드 방식으로 읽기 : utf-8)
f=open('c:\\work\\PV3.txt','rt', encoding='utf-8')
# 복사본 쓰기(에러......)
g=open('c:\\work\\PV3_copy.txt','wt', encoding='utf-8')

#많은 라인의 파일이면 (로그파일은 굉장히 큼 : ex)100MB~1GB) 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
while (line != ''): #빈줄을 찾다가 없으면 계속 반복    # 파일의 EOF(End Of File)까지
    if (re.search("error", line)): # 날짜 있는 것만 찾음.
        g.write(line + "\n")
    line = f.readline()

f.close() 
g.close()








