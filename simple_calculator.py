def arithmetic_ops(op):
    num1 = int(input("input 1st number:"))
    num2 = int(input("input 2nd number:"))
    return num1, num2, op(num1, num2)

# +와 -는 함수로 정의한다

def add(a,b):
    return a + b
def sub(a, b):
    return a - b

while True:
    op = input("input operation:")
    if op == "end":
        break   # "반복을 종료"
    elif op == "+":
        num1, num2, ret = arithmetic_ops(add) # 정의된 함수 사용
    elif op == "*":
        num1, num2, ret = arithmetic_ops(lambda a,b:a*b) # 익명함수(lambda) 사용
   
    # [fill this area] 위의 코드를 참고하여 -, /, %에 대한 내용 구현
    
    elif op == '-':
        num1, num2, ret = arithmetic_ops(sub)
    elif op == '/':
        num1, num2, ret = arithmetic_ops(lambda a,b:a/b)
    elif op == '%':
        num1, num2, ret = arithmetic_ops(lambda a, b:a%b)

    else:
        print("Invalid operation")
        continue # Invalid operation이므로 연산결과를 출력하지 않고 "넘어간다".
    print(f"{num1}{op}{num2} = {ret}")  # 연산 결과를 출력

print("Exit program")
