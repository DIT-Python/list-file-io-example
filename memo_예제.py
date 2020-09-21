## 메모장 프로그램 예제

## 사용자 입력을 파일에 기록하는 함수
def write_your_memo(mode):
	f = open("D:\\memo.txt",mode)
	memo =input("input your memo> ")+"\r\n"
	f.write(memo)
	f.close

## 파일열기 선택
mode = input("w: New memo note, a: Append your memo? ")

## 열기 모드에 따른 동작
if mode == "w" or mode == "a":
	write_your_memo(mode)
	if mode == "w":
		print("Wrote your memo to a new note")
	else:
		print("Appended your memo...")
else:
	print("Wrong command!")