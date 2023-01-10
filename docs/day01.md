# Python Basic Day01
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



