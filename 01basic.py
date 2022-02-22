## 주교재 : 혼자 공부하는 파이썬

# 01-1 파이썬을 하기 전에 읽는 아주 간단한 설명
# 컴퓨터 프로그램(computer program) - 컴퓨터가 무엇을 해야 할지 미리 작성한 진행 계획
# 소스 코드(source code) - 프로그래밍 언어로 사람이 쉽게 읽고 이해할 수 있도록 만든 코드

# 01-2 파이썬을 배우기 위해 준비해야 할 것들
# 텍스트 에디터(text editor) - 파이썬 코드를 입력
# 파이썬 인터프리터 - 파이썬 코드를 실행

# 01-3 이 책에서 자주 나오는 파이썬 용어들
# 표현식 : 값을 만들어 내는 코드
#        - 키워드 : 언어가 처음 만들어질 때 정한 단어 (ex. import)

# 문장  : 표현식이 하나 이상 모인 것 (ex. print("Hello World"))

# 프로그램 : 문장이 모인 것
#         - 주석 : 프로그램에 영향을 주지 않는 코드 (ex. #예시)
#         - 식별자 : 사용자가 만들 수 있는 단어

# 표현식과 문장
# 표현식(expression) : 어떠한 값을 만들어 내는 간단한 코드
# 값? => 숫자, 수식, 문자열 등과 같은 것을 의미함.
# 273 / 10 + 20 + 30 * 10 / "Python Programming"

# 키워드(keyword)
# 키워드는 특별한 의미가 부여된 단어, 파이썬이 만들어질 때 이미 사용하겠다고 예약해 놓는 것.
# ex) False,break,else,if,not,while,None,class,except,....
# 파이썬은 대소문자를 구분함 => True는 키워드지만, true는 키워드가 아님
# 사용 되는 언어가 키워드인지 아닌지 꼭 확인해야 할 경우
import keyword
print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# 식별자(identifier)
#