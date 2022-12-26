from flask import request, make_response, jsonify
from flask_restful import Resource
from models.Agencies import Agencies
from thirdParty.personalToken import decode
from config.uiniqu import db

import datetime

class AgenciesService(Resource):
    def get(self):
        try:
            agencies = Agencies.all()
            result = [dict(foo) for foo in agencies]

            return make_response(jsonify({"data":result}), 200)

        except Exception as e:
            return make_response(jsonify({"msg":"Terjadi kesalahan saat mengambil data"}),403)


    def post(self):
        db.sync_db()
        try:
            user = decode(request.headers['Authorization'])
            if(request.form.get("agency_name") and request.form.get("agency_detail") and user['role']):

                agencyModel = Agencies(
                    agency_name = request.form.get("agency_name"),
                    agency_detail = request.form.get("agency_detail"),
                    created_by = user['uuid']
                )

                agencyModel.save()
                return make_response(jsonify({"msg":"Berhasil menyimpan data"}), 200)
            else:
                return make_response(jsonify({"msg":"Form kosong"}), 402)


        except Exception as e:
            return make_response(jsonify({"msg":"Terjadi kesalahan saat menyimpan data"}),403)


    def put(self):
        try:
            user = decode(request.headers['Authorization'])
            if(user['role']):
                Agencies.objects(uuid=request.form.get('uuid')).update(
                    agency_name = request.form.get('agency_name'), 
                    agency_detail = request.form.get('agency_detail'),
                    updated_at = datetime.datetime.now()
                )
                return make_response(jsonify({"msg":"Berhasil mengupdate data"}), 200)

        except Exception as e:
            return make_response(jsonify({"msg":"Terjadi kesalahan"}), 403)



    def delete(self):
        try:
            user = decode(request.headers['Authorization'])
            if(user['role']):
                Agencies.objects(uuid=request.form.get('uuid')).delete()
                return make_response(jsonify({"msg":"Berhasil menghapus data"}), 200)

        except Exception as e:
            return make_response(jsonify({"msg":"Terjadi kesalahan"}), 403)


        




