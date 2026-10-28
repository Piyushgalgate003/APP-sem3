import pandas as pd
names = []
attendance = []
for i in range(10):
    name = input(f"Enter name of student {i + 1}: ")
    percent = float(input(f"Enter attendance percentage of {name}: "))
    names.append(name)
    attendance.append(percent)
att = pd.Series(attendance, index=names, name="Attendance %")
print("\nAttendance Series:")
print(att)
student = input("\nEnter a student name to look up: ")
print(f"Attendance of {student}:", att.loc[student])
print("Attendance of the first student:", att.iloc[0])
print("Attendance of first three students:")
print(att.iloc[0:3])
print("\nStudents with attendance above 75%:")
print(att[att > 75])
print("\nMean attendance:", att.mean())
print("Median attendance:", att.median())
print("\nMinimum attendance:", att.min(), "->", att.idxmin())
print("Maximum attendance:", att.max(), "->", att.idxmax())