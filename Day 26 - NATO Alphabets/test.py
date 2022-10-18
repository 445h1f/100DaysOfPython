# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor','Freddie']

# from random import randint


# students_score = {student:randint(1, 100) for student in names}
# print(students_score)
# passed_students = {student:score for (student, score) in students_score.items() if score >= 60}
# print(passed_students)


import pandas

student_dict = {
    'student' : ['Alex', 'Beth', 'Caroline'],
    'score' : [87, 64, 45]
}

student_data_frame = pandas.DataFrame(student_dict)

# print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    if row.student == 'Beth':
        print(row.score)