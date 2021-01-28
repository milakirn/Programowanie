db = {
    "Gandalf" : '123',
    "admin" : 'admin',
    "Geralt" : '123',
    "Ciri" : '321',
    "Johnny" : '123',
    "V" : '321'
}
while True:
    login = input("Login: ")
    password = input("Password: ")
    if password == db.get(login):
        if 'admin' != db.get(login):
            print("Logged in as a user ")
            break
        else:
            print("Logged in as an admin ")
            break
    else:
        print("incorrect password or login")