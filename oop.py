class student :
    def __init__(self, name , age , grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    
    def introduce(self):
        print(f"Hii, I'm {self.name}")    
        
    def assign_grade(self):
     print(f"My grade is {self.grade}")
    
    # Object instance        
student_1 = student('fathia', 22, 'A')
student_1.introduce()
student_1.assign_grade()

class female(student):
    def introduce(self):
        print(f" I am a girl and my name is {self.name}")
        
class male(student):
    def introduce(self):
        print(f" I am a boy and my name is {self.name}")
        
# object instance
students = [
   female('fathia', 22, 'A'),
   male ('ahmed', 23, 'B'),
   student('sara', 21, 'C')]

for student in students:
    student.introduce()
    student.assign_grade()
    
    
    
    ## polymorphism challenge
class Animal:
        def speak(self):
            print("Animal speaks")
            
class Dog(Animal):
        def speak(self):
            print("Dog barks")
            
class Cat(Animal):
        def speak(self):
            print("Cat meows")
            
def noise(creature) :
     creature.speak()

    # Object instances
dog = Dog()
cat = Cat()
    
noise(dog) 
noise(cat)  