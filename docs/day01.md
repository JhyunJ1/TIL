# Python Basic Week 01

## 이규화 멘토님
### 신한투자증권 ict 영역
- web : 주로 java vue.js node.js
- openAPI : 주로 java
- 인프라 : 경험 우선
- 데이터 분석
- 모바일/mts
- hts
- core 금융
- 대외연계 인터페이스

### 사용 테스트 종류
- 단위 테스트
- 인수 테스트
- 벤치마크 테스트
- 부하 / 스트레스 테스트 : 성능 임계치 확인
- 자동화 테스트 : CI/CD


## Python 기초 문법
### Let's Code PYTHONIC
#### Important Python Enhance Proposal
Layout
- 들여쓰기 : 공백 4칸
- 한 줄은 79자(120)
- 클래스 정의와 최상위 함수는 두 줄을 띄움
- 클래스 내 메소드는 한 줄을 띄움

Variables
- _variable : 내부적으로 사용되는 변수
- print_ : 파이썬 키워드와 충돌 방지

#### Floating Point
- 컴퓨터는 실수를 이진 부동소수점을 활용
- 0, 1
```python
0.1 + 0.2 != 0.3
round(0,1 + 0.2, 1) == round(0.3, 1)
```

#### inputwith Evaluation
```python
memo = eval(input("Say anyting > "))
print(memo, type(memo))
```

#### Git
기본bash layout
- $ : 사용자의 입력 받을 준비
- ~ : 사용자가 root 권한 없이 사용할 수 있는 가장 최상위 위치 (=user 폴더)
- git push origin main
- /*Trailing comma*/
```python
menus = [
	'tteokbokki',
	'pizza',
	'Cream Soup',
]
```

### List Tuple Dictionary Set
#### List, Tuple
- List : 순서 존재
- Tuple : 무순서 ,묶음
```
Tuple
: 함수에서 여러 개의 값을 반환할 때 주로 사용
: 값들을 교환해야 할 때 주로 사용
```

#### Hash Table
> 일정한 탐색 속도
- .format을 이용하여 dict 편하게 출력하기
```python
contact = {
    'name': 'John Doe',
    'Locale': 'CA, USA',
}
print("Hello, {name}. You are from{Locale}".format(**contact))
```

#### Set
> 원소는 유일해야 한다는 집합의 속성으로 중복 제거 할 때 유용


#### Pseudo Code
omputational Thinking
컴퓨팅적 사고 방식을 위한 연습

문제 정의
잠에 들기 전 /*더 글로리 시즌 2*/가 나왔다. 어디서, 어떻게 드라마를 볼까?

문제 추상화
- 드라마가 보고 싶은가?
     Yes -> 드라마를 시청한다.
     No -> 잠에 든다.

- 잠들기 전 시간이 충분히 남았는가?
    Yes -> 드라마를 시청한다.
    No -> 잠에 든다.

- 핸드폰 배떠리가 45프로 이상인가?
    Yes -> 핸드폰으로 드라마를 시청한다.
    No -> 노트북으로 드라마를 시청한다.

- 부모님이 주무시는가?
    Yes -> 방에서 조용히 혼자 드라마를 시청한다.
    No -> 부엌에서 야식을 먹으며 드라마를 시청한다.

솔루션
![ct](https://user-images.githubusercontent.com/93964101/211465308-1a2a37d1-3661-4a04-b7ea-1d0378445339.png)


#### VAT
- Korea: 10%
- Japan: 8%
- USA : 주마다 다름
- UK : 20%
제품 가격과 나라에 따라 다른 부가가치세를 계산해 그 가격을 보여주도록!

/*Pseudo Code*/
```
1. vat 변수를 생성하여 사용자에게 입력받는다.
2. korea는 제품 가격 : vat * 1.1 부가가치세 : vat * 0.1를 출력한다.
3. Japan는 제품 가격 : vat * 1.08 부가가치세 : vat * 0.08를 출력한다.
4. USA는 제품 가격 : 지역에 따라 다름 부가가치세 : 지역에 따라 다름을 출력한다.
5. UK는 제품 가격 : vat * 1.2 부가가치세 : vat * 0.2를 출력한다.
```







