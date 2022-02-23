# 여러줄 주석처리 : 작은 따옴표 3개 or 큰 따움표 3개
"""
02-1. 자료형과 문자열
자료 : 프로그램이 처리할 수 있는 모든 것
프로그램 : 자료를 처리 하는 역할

#자료형(data type) : 문자열(string), 숫자(number), 불(boolean)
String : "Hallo", "Hello World"
Number : 52, 103.32
Boolean : True, False

#자료형 확인하기 : type() 함수 이용
ex)
>>>print(type("Hallo"))
<class 'str'> -> 문자열
>>>print(type(273))
<class 'int'> -> 정수

#문자열 만들기
따옴표로 둘러싸여 입력된 모든 것
ex)
"Hello"
'String'
'안녕하세요'
"Hello Python Programming"

***문자열 내부에 따옴표 넣기
왜 문자열 형성을 위해 큰따옴표, 작은따옴표로 만드는 두가지 방법을 지원하는가?
ex)
"안녕하세요"라고 말했습니다.
#>>>print(""안녕하세요"라고 말했습니다")
<SyntaxError : invalid syntax>

따라서,
>>>print('"안녕하세요"라고 말했습니다')

#이스케이프 문자를 사용해 문자열 만들기
 역슬래시(\) 기호와 함께 조합해서 사용
 \와 함께 큰따옴표,작은따옴표를 사용하면 이를 '문자열을 만드는 기호'가 아니라 '단순한 따옴표'로 인식함
  \" : 큰따옴표
  \' : 작은따옴표
ex)
>>>print("\"안녕하세요\"라고 말했습니다.")
>>>print('\'배가 고픕니다\'라고 생각했습니다')


"""
