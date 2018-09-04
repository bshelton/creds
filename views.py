import json
from flask import request, jsonify
from api import app, db
from model import Users, Account, System, Service
import gnupg
import datetime

gpg = gnupg.GPG(gnupghome='/home/brock/api/keytrust')

#unencrypted_string = 'Who are you and how did you get in my house?'
#encrypted_data = gpg.encrypt(unencrypted_string, 'brocks@brocks.com')
#newuser = Users('brock', str(encrypted_data))

'''
input_data = gpg.gen_key_input(key_type="RSA", key_length=2048, name_email=username+"@"+username+".com")
    key = gpg.gen_key(input_data)
'''

@app.route('/addcred/<uuid>', methods = ['POST'])
def create_cred(uuid):

    
    content = request.json

    sys_username = content['username']
    sys_password = content['password']
    service_id = content['service_id']
    encrypted_pass = encrypt_string(sys_password)

    acc = Account(datetime.datetime.now(), sys_username, str(encrypted_pass), service_id)
    db.session.add(acc)
    db.session.commit()

    print (content['username'])
    print (content['password'])
    print (encrypted_pass)
    print (content['service_id'])
    return jsonify({"username":content['username']})


def encrypt_string(msg):
    encrypted_msg = gpg.encrypt(msg, 'brocks@brocks.com')
    return encrypted_msg

@app.route('/get/user/<username>', methods=['GET'])
def get_user(username):
    user_id = Users.query.filter(Users.username == username).first()
    return str(user_id.username)


@app.route('/get/user/password/<username>', methods=['GET'])
def get_password(username):

    encrypted_str = Users.query.filter(Users.username == username).first()
    decrypted_data = gpg.decrypt(encrypted_str.password)
    return str(decrypted_data)