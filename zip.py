kor = ["사과","바나나","오렌지"]
eng = ["apple","banana","orange"]

print(tuple(zip(kor,eng)))

mixed = {('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')}

print(list(zip(*mixed)))