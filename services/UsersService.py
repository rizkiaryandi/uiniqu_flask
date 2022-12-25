from flask import request, make_response, jsonify
from flask_restful import Resource
from models.UsersModel import Users
from config.uiniqu import SECRET_KEY
from thirdParty.personalToken import decode

# import lib
from config.uiniqu import db
import argon2
import jwt
import datetime

# Konfigurasi Hash
argon2Hasher = argon2.PasswordHasher(
    time_cost=3, # number of iterations
    memory_cost=64 * 1024, # 64mb
    parallelism=1, # how many parallel threads to use
    hash_len=32, # the size of the derived key
    salt_len=16 # the size of the random generated salt in bytes
)

class RegisterUser(Resource):
    def post (self):
        db.sync_db()
        dataUsername =  request.form.get('username')
        dataPassword = request.form.get('password')
        dataName = request.form.get('name')

        # cek apakah username & password ada?
        if dataUsername and dataPassword:
            # insert data
            try:
                userModel = Users(
                    username = dataUsername,
                    password = argon2Hasher.hash(dataPassword),
                    name = dataName
                )
                userModel.if_not_exists().save()
                return make_response(jsonify({"msg":"Berhasil membuat akun"}), 200)

            except Exception as e:
                return make_response(jsonify({"msg":"Username dengan username yang sama sudah terdaftar"}), 200)
        else:
            return make_response(jsonify({"msg":"Terjadi kesalahan, username/password harus diisi"}), 403)


class LoginUser(Resource):
    def post(self):
        dataUsername =  request.form.get('username')
        dataPassword = request.form.get('password')
        if dataUsername and dataPassword:
            try:
                token = ""
                user = Users.objects.get(username = dataUsername)
                if(argon2.PasswordHasher().verify(user.password, dataPassword)):
                    token = jwt.encode({
                        'uuid': str(user.uuid),
                        'username': user.username,
                        'name': user.name,
                        'photo_url': user.photo_url,
                        'created_at': str(user.created_at),
                        'updated_at': str(user.updated_at),
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(days = 30)
                    }, SECRET_KEY, algorithm="HS256")

                    return make_response(jsonify({
                        "data":{
                            'username': user.username,
                            'name': user.name,
                            'photo_url': user.photo_url,
                            'created_at': str(user.created_at),
                            'updated_at': str(user.updated_at),
                            'token': token
                        },
                    }), 200)
                else:
                    return make_response(jsonify({"msg":"Kata sandi salah"}), 200)

            except Exception as e:
                print(e)
                return make_response(jsonify({"msg":"Username atau kata sandi salah"}), 200)

        else:
            return make_response(jsonify({"msg":"Terjadi kesalahan, username/password harus diisi"}), 403)


class User(Resource):
    def get(self):

        user = Users.objects.get(username='rizkiaryandi')

        return make_response(jsonify(dict(user)), 200)


    def put(self):
        try:
            user = decode(request.headers['Authorization'])
            Users.objects(username=user['username']).update(name = request.form.get('name'))
            return make_response(jsonify({"msg":"Berhasil mengupdate data"}), 200)
        except Exception as e:
            return make_response(jsonify({"msg":"Terjadi kesalahan"}), 403)