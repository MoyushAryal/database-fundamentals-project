import sys
import sqlite3

sys.path.insert(0,r"C:\everything\Internship\Task\Task-4\Python_Data_Toolkit\finalToolkit")

from Logic.dataset import Dataset

dataset = Dataset("messy_people.csv")
dataset.clean()


connection = sqlite3.connect("people.db")

cursor = connection.cursor()

for i in dataset.stream():
    each_person = i.id,i.name,i.age,i.city,i.score
    cursor.execute("""
        INSERT  INTO people (id,name,age,city,score)
        VALUES (?,?,?,?,?)
        """,each_person)
connection.commit()
