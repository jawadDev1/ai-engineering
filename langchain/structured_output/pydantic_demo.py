from pydantic import BaseModel, EmailStr , Field
from typing import Optional

class Student(BaseModel):
    # name: str
    name: str = "Roronoa Zoro" # default value
    age: Optional[int] = None  # in optional must set the default to None or something
    email: EmailStr
    cgpa: float = Field(gt=0, lt=4, description="cgpa of a student")

new_student = {
    # "name" : 123 # gives error 
    "name" : "Monkey D. Luffy",
    "email": "aebc@gmail.com",
    "cgpa": 2
}

student = Student(**new_student) # pydantic Object

print(student)

student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()