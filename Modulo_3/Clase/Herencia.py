from ClaseUser_3 import User

class WebUser(User):
    def __init__(self, name, email, phoneNumber, password, isAdmin):
        super().__init__(name, email, phoneNumber, password)
        self.isAdmin = isAdmin
        self.urlBasePage = None

wu1 = WebUser('Abraham','abraham@hotmail.com','2222222222','Admin123',True)
print(wu1.isAdmin)
print(wu1.urlBasePage)
wu1.urlBasePage = 'https://www.cursoPython.com'
print(wu1.urlBasePage)
print(wu1.name)
print(wu1.email)
print(wu1.phoneNumber)
print(wu1.password)