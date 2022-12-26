from flask import request, make_response, jsonify
from flask_restful import Resource
from models.RoteModel import Rote
from thirdParty.personalToken import decode
from config.uiniqu import db

class RoteService(Resource):
    def get(self):
        try:
            if(request.form.get('user_uid')):
                rote = Rote.objects.filter(user_uid=request.form.get('user_uid')).allow_filtering()
                result = [dict(foo) for foo in rote]
            else:
                rote = Rote.all()
                result = [dict(foo) for foo in rote]

            return make_response(jsonify({"data":result}), 200)

        except Exception as e:
            return make_response(jsonify({"msg":"Terjadi kesalahan saat mengambil data"}),403)


    def post(self):
        # db.sync_db()
        try:
            user = decode(request.headers['Authorization'])
            if(request.form.get("history")):
                
                if(Rote.objects(user_uid=user['uuid']).count() != '0'):
                    Rote.objects(user_uid=user['uuid']).delete()

                roteModel = Rote(
                    user_uid = user['uuid'],
                    history = request.form.get("history"),
                )

                roteModel.save()
                return make_response(jsonify({"msg":"Berhasil menyimpan data"}), 200)
            else:
                return make_response(jsonify({"msg":"Form kosong"}), 402)


        except Exception as e:
            print(e)
            return make_response(jsonify({"msg":"Terjadi kesalahan saat menyimpan data"}),403)


    def delete(self):
        try:
            user = decode(request.headers['Authorization'])
            Rote.objects(user_uid=user['uuid']).delete()
            return make_response(jsonify({"msg":"Berhasil menghapus data"}), 200)

        except Exception as e:
            return make_response(jsonify({"msg":"Terjadi kesalahan"}), 403)


        




