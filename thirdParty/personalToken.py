from config.uiniqu import SECRET_KEY
import jwt

def decode(t):
    return jwt.decode(t, SECRET_KEY, algorithms=["HS256"])