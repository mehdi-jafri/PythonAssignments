#demonstrate inheritance

class human():
    def __init__(self,names,ages):
        self.name=names
        self.age=ages

class student(human):
    def __init__(self,names,ages,id):
        self.name=names
        self.age= ages
        self.ids = id


s=student("hani",21,111)
print(s.name,s.age,s.ids)


#using super()

class human():
    def __init__(self,names,ages):
        self.name=names
        self.age=ages
    def display(self):
        print(self.name,self.age)

class student(human):
    def __init__(self,name,ages,ids,emails):
        super().__init__(name,ages)
        self.ids= ids
        self.email=emails

s2=student("haniya", 22, 90, "hani@gmail.com")
print(s2.name,s2.age,s2.ids,s2.email)


