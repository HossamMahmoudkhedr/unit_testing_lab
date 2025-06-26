class User:
    def __init__(self):
        self.usrName = ""
        self.usrEmail = ""

    def name(self, name=""):
        if name == "":
            return self.usrName
        else:
            self.usrName = name

    def email(self, email=""):
        if email == "":
            return self.usrEmail
        else:
            self.usrEmail = email
