#import uiniqu
from config.uiniqu import app, api

#import service
from services.UsersService import User, RegisterUser,LoginUser 
from services.TadarusService import TadarusService
from services.AgenciesService import AgenciesService
from services.RoteService import RoteService


# routes
api.add_resource(User, '/api/v1/user', methods=["GET", "PUT"])
api.add_resource(RegisterUser, "/api/v1/register", methods=["POST"])
api.add_resource(LoginUser, "/api/v1/login", methods=["POST", "PUT"])
api.add_resource(TadarusService, "/api/v1/tadarus", methods=["GET", "POST","DELETE"])
api.add_resource(AgenciesService, "/api/v1/agency", methods=["GET", "POST","PUT","DELETE"])
api.add_resource(RoteService, "/api/v1/rote", methods=["GET", "POST","DELETE"])



# jalankan aplikasi app.py
if __name__ == "__main__":
    app.run(debug=True)








# routing autentikasi: register

        

# # routing autentikasi: login
# class LoginUser(Resource):
#     def post(self):
#         dataUsername =  request.form.get('username')
#         dataPassword = request.form.get('password')

#         # query matching kecocokan data
#         query = UserModel.get()