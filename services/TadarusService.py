from flask import request, make_response, jsonify
from flask_restful import Resource
from models.TadarusModel import Tadarus
from thirdParty.personalToken import decode
from config.uiniqu import db

class TadarusService(Resource):
    def get(self):
        try:
            user = decode(request.headers['Authorization'])
            tadarus = Tadarus.objects.filter(user_uid=user['uuid']).allow_filtering()
            result = [dict(foo) for foo in tadarus]

            return make_response(jsonify({"data":result}), 200)

        except Exception as e:
            return make_response(jsonify({"msg":"Terjadi kesalahan saat mengambil data"}),403)


    def post(self):
        db.sync_db()
        try:
            if(request.form.get("surah_name") and request.form.get("surah_number") and request.form.get("ayah_number")):
                user = decode(request.headers['Authorization'])
                # print(user['uuid'])

                tadarusModel = Tadarus(
                    user_uid = user['uuid'],
                    surah_name = request.form.get("surah_name"),
                    surah_number = request.form.get("surah_number"),
                    ayah_number = request.form.get("ayah_number")
                )

                tadarusModel.save()
                return make_response(jsonify({"msg":"Berhasil menyimpan tadarus"}), 200)
            else:
                return make_response(jsonify({"msg":"Form kosong"}), 402)


        except Exception as e:
            return make_response(jsonify({"msg":"Terjadi kesalahan saat menyimpan tadarus"}),403)


    def delete(self):
        try:
            user = decode(request.headers['Authorization'])
            uuid = request.form.get("uuid")
            Tadarus.objects(uuid=uuid, user_uid=user['uuid']).delete()
            return make_response(jsonify({"msg":"Berhasil menghapus data"}), 200)
        except Exception as e:
            return make_response(jsonify({"msg":"Terjadi kesalahan"}), 403)


        




