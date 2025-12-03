from flask import Flask, jsonify, request

class User:
    def __init__(self,username, nom , password , email, rol):
        self.username=username
        self.nom=nom
        self.password=password
        self.email=email
        self.rol=rol

    def __str__(self):
        return self.nom

#us1 = User(username="ama", nom="Rob Holfrod", password="12345", email="rob@gamil.com", rol="Tutor")
#print(us1)

users= [
    User(username="ama", nom="Rob Holfrod", password="12345", email="rob@gamil.com", rol="Tutor"),
    User(username="john", nom="john cannigan", password="12345", email="john@gamil.com", rol="Tutor"),
    User(username="maria", nom="maria sams", password="12345", email="maria@gamil.com", rol="Tutor")
]

class UserDao:
    def __init__(self):
        self.users=users

    def getUserByUsername(self,username):
        return "TO-DO"
'''
app = Flask(__name__)

@app.route('/user',methods=['GET'])
def user():

    resposta=""
    #Parametres
    username = request.args.get("username", default="")
    # Si els paràmetres OK
    if username!="":
    # Anar al DAO Server i cercar User per username
    # respondre amb dades Usuari si trobat
        resposta ="username" + username
    else :# Si els paràmetres No ok
    # Respondre error
        resposta="username No informat"
    return resposta

if __name__ == '__main__':
    app.run(debug=True)'''