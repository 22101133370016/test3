from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Ally",
        "age": 45,
        "year": "yr7"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class Updatestudent(BaseModel):
    name: Optional[str]=None
    age: Optional[int]=None
    year:Optional[str]=None

@app.get("/")
def laam():
    return {"name": "First data"}

@app.get("/get-student/{student_id}")
def get_student_by_id(student_id: int = Path(..., description="Enter the ID you want")):
    return students.get(student_id, {"Data": "Not found"})

@app.get("/get-by-name/{student_id}")
def get_student_by_name(student_id: int, name: Optional[str]= None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Message": "Student already exists"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: Updatestudent):
    if student_id not in students:
        return {"error": "student not found"}
    
    if student.name != None:
        students[student_id].name= student.name
    if student.age !=None:
        students[student_id].age= student.age
    if student.year !=None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Message:" "Student already not exist"}
    del students[student_id]
    return{"Message:" "student deleted successfully"}