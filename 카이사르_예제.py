## 카이사르 암호화 예제
## 두 사람이 서로 알파벳 이동 칸 수를 합의하고 
## 각 알파벳을 그 칸 수만큼 이동하여 암호화한다

## 1. 알파벳 리스트 정의
alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

## 2. 암호화 함수
def encrypt_and_decrypt(text,shift):
	ciphertext = ""
	for ch in text:		## 문자 하나하나에 대하여
		if ch in alph:	## 알파벳인 경우만 암호화한다.
			i = (alph.index(ch)+shift)%26	## 리스트의 전체 순서번호가 넘어갈 경우 순환시킴
			ciphertext += alph[i]
		else:
			ciphertext += ch
	return ciphertext
	
## 3. 이동 칸 수를 입력받아 암호화된 문자열을 파일에 저장한다.
shift = int(input("input a shift.."))	## 이동칸수 입력

sentence = input("input a sentence>").lower()
cipher = encrypt_and_decrypt(sentence,shift)

f = open("D:\\caesar_cipher.txt","w")
f.write(cipher)
f.close()