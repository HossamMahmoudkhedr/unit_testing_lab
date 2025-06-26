from user import User
import re

user = User()
def test_user_get_name():
    assert user.name() == user.usrName

def test_user_set_name():
    user.name('Ahmed')
    assert user.usrName == 'Ahmed'

def test_user_get_email():
    assert user.email() == user.usrEmail

def test_user_set_email():
    # Value to be set to email
    email = 'ahmed@gmail.com'

    # The email pattern
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

    # Check if email is valid
    isValidEmail = re.match(pattern, email)

    # Run test case to check if it's valid or not
    assert isValidEmail != None

    # Run test case to check if the email has been set to the targeted value
    user.email(email)
    assert user.usrEmail == email

