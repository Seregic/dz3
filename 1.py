def average_grade(*b):
    average = round(sum(b)/len(b),1)
    print("Средний балл:" , average)
    return average
def grade_message(a):
    if a >= 4.5 :
     print("Отлично")
    elif a >= 3.5 :
     print("Хорошо")
    else :
     print("Нужно повторить материал")

w = map(int,input("Введите числа: ").split())
grade_message(average_grade(*w))
