#coding:utf-8
groupmates = [
    {
        "name": u"Александр",
        "group": "БСТ1702",
        "age": 19,
        "marks": [5, 4, 5, 4, 4]
    },
    {
        "name": u"Екатерина",
        "group": "БСТ1702",
        "age": 19,
        "marks": [5, 5, 5, 5, 5]
    },
    {
        "name": u"Радим",
        "group": "БСТ1702",
        "age": 16,
        "marks": [3, 3, 3, 3, 3]
    },
    {
        "name": u"Олеся",
        "group": "БСТ1702",
        "age": 19,
        "marks": [5, 4, 5, 5, 5]
    }
]

def print_students(students):
    print (u"Имя студента".ljust(15), u"Группа".ljust(8), \
        u"Возраст".ljust(8), \
        u"Оценки".ljust(20))
    for student in students:
        print (student["name"].ljust(15), \
            student["group"].ljust(8), \
            str(student["age"]).ljust(8), \
            str(student["marks"]).ljust(20))
    print ("\n")

print_students(groupmates)
ave = float(input("Введите среднюю оценку студента: "))
average = []
for student in groupmates:
    if float(sum(student["marks"])) / len(student["marks"]) >= ave:
        average.append(student)
print_students(average)
