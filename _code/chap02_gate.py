#chap02 논리 게이트

## AND 게이트

def AND(x1, x2):                  # 함수이름과 함수에 사용할 변수 명명
    w1, w2, b = 0.5, 0.5, -0.7    # 사용할 인수 지정
    tmp = x1*w1 + x2*w2 + b       # 함수에서 사용할 식
    if tmp <= 0:                  # 식이 0보다 같거나 작으면 0을 리턴
        return 0          
    elif tmp > 0:                 # if에 해당하지 않으면, 식이 0보다 크면 1을 리턴
        return 1
    
print(AND(0, 0)) # 0 을 출력
print(AND(0, 1)) # 0 을 출력
print(AND(1, 0)) # 0 을 출력
print(AND(1, 1)) # 1 을 출력

### if 조건문

if True :                          # True(o) true(x) 대소문자 주의
  print('True입니다')

#> True입니다

if False :
  print('False입니다')
  
#> 
#아무것도 출력되지 않음


### if else 조건문 : 두가지 반대조건이 있을 때 사용 가능
'''
if 조건 :
  print("조건이 참일 때 출력될 것")
else 조건 :
  print("조건이 거짓일 때 출력될 것")
'''

### elif 조건문 : 3개 이상의 조건이 있을 때 사용
'''
if 조건1 :
  print("조건1일 때 출력될 것")
elif 조건2 :
  print("조건2일 때 출력될 것")
elif 조건3 :
  print("조건3일 때 출력될 것")
else :
  print("위의 모든 조건에 해당하지 않을 때 출력될 것")
'''
