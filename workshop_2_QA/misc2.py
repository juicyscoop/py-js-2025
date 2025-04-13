class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #self._full_name = f"{self.name} {self.age}"

    def check_username(self):
        self.dalsi_metoda()
        if self.name.isalpha():
            return True
        return False
    
    def dalsi_metoda(self):
        pass

    @staticmethod
    def hello():
        print('Hello')
    
    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        age = int(age)
        return cls(name, age)
        # return User("John", 30)

    @property # getter
    def full_name(self):
        return f"{self.name} {self.age}"
    
    @full_name.setter
    def full_name(self, value):
        self.name, self.age = value.split(' ')
    
    @full_name.deleter
    def full_name(self):
        self.name = None
        self.age = None


user1 = User('John', 30)
user1.full_name = 'John,20'
del user1.full_name
print(user1.full_name)


user2 = User.from_string('John,30')






user1.hello()

User.hello()


print(user1)
print(type(user1))

user_ref = User

print(user_ref)
print(type(user_ref))


