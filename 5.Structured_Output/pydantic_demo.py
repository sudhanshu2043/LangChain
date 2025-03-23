from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name:str="Sudhanshu"
    age:Optional[int]=None
    email: EmailStr
    cgpa:float=Field(gt=0,lt=10,default=5)

new_student={'age':'32','email': 'abc@gmail.com','cgpa':5}

student=Student(**new_student)

print(student)
# explicit convert into dict
student_dict=dict(student)
print(student_dict['name'])

# explicit convert itno json
student_json=student.model_dump_json()
print(student_json)