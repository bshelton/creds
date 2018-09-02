import json
from api import app, db
from model import Users
import gnupg

gpg = gnupg.GPG(gnupghome='/home/brock/api/keytrust')

#unencrypted_string = 'Who are you and how did you get in my house?'
#encrypted_data = gpg.encrypt(unencrypted_string, 'brocks@brocks.com')
#newuser = Users('brock', str(encrypted_data))



@app.route('/createkey/<username>')
def create_key(username):
    input_data = gpg.gen_key_input(key_type="RSA", key_length=2048, name_email=username+"@"+username+".com")
    key = gpg.gen_key(input_data)
    return str(key)

@app.route('/get/user/<username>', methods=['GET'])
def get_user(username):
    user_id = Users.query.filter(Users.username == username).first()
    return str(user_id.id)


@app.route('/get/user/password/<username>', methods=['GET'])
def get_password(username):

    encrypted_str = Users.query.filter(Users.username == username).first()
    decrypted_data = gpg.decrypt(encrypted_str.password)
    return str(decrypted_data)
