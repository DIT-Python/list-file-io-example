## 파일 : 한 과목에 대한 자료는 하나의 파일에 저장
## 디렉토리 : 파일을 묶어 놓은 공간
## 파일경로 : 파일이 실제 위치한 디렉토리 명을 계층적 구조로 나열 (파일을 찾아가는 경로)

## 파일에 저장함으로서 장기간 보관하거나 이후 재사용 및 공유 기능
## 예) 100명에게 설문조사 후 평균을 계산하고, 표준편차를 계산하기 위해 데이터를 일일이 입력
## 파일로 저장한 후 파이썬을 통해 순식간에 데이터를 읽어들여 데이터를 분석하고 그 결과를 파일로 저장한다.

## 파일열기
## 파일변수 = open(파일경로, 모드)
## 파일변수에는 메모리 상의 파일위치, 다음에 읽어야 하는 위치 등이 들어있다.


## r(ead) : 읽기모드
f = open("C:\\python\\newfile.txt","r")		## 해당경로에 파일이 없으면 에러

## read() : 파일의 내용 전체를 한꺼번에 읽음
f = open("c:\\python\\food.txt","r")
data = f.read()
print(data)

## readline() : 호출할 때마다 파일의 내용을 줄 단위로 읽음
## 10줄일 경우 전체를 읽기 위해서 10번을 실행해야 함
f = open("c:\\python\\food.txt","r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)

## readlines() : 파일의 모든 내용을 읽어 줄 단위로 리스트 항목을 만들어 줌
f = open("c:\\python\\food.txt","r")
list = f.readlines()
print(list)		## ["떡볶이\n","피자\n"]


## w(rite) : 쓰기모드 
## 기존 내용 모두 삭제되고 처음부터 기록
## 해당 경로에 파일이 없으면 파일 생성
f = open("newfile.txt","w")		## 현재 실행되고 있는 디렉토리에 생성

f = open("c:\\python\\food.txt","w")
f.write("떡볶이\n")		## \n : 개행문자
f.write("피자\n")

## a(ppend) : 파일의 마지막에 내용을 추가 (이어쓰기)
## 기존 파일에 내용을 추가할 때는 반드시 a 모드로 열어야 함
## 해당 경로에 파일이 없으면 파일 생성
f = open("newfile.txt","a")		## 현재 실행되고 있는 디렉토리에 생성

f = open("c:\\python\\food.txt","a")
f.write("파스타\n")


## 사용이 끝난 파일은 닫아야 함
f = open("newfile.txt","w")
f.close()	## 파일을 닫기 전까지는 디스크에 저장되지 않음