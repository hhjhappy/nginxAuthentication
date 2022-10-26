# -*- coding:utf-8 -*-

from flask import Flask, jsonify, request, make_response, g
from pathlib import Path
from redispublic import redisConnect
import logging,secrets,os

app = Flask(__name__)
redisconn = redisConnect()

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s:%(message)s",
    filename=os.path.join(BASE_DIR, "app.log"),
    filemode="a+",
)

@app.route('/auth',methods=["GET"])
def auth():
    '''
    nginx url动态认证
    '''
    token = redisconn.get('token')
    logging.info(str(token))
    if request.headers.get('Authorization') == token:
        logging.info(str(200))
        return '200',200
    else:
        logging.info(str(401))
        return '401',401
    

if __name__ == "__main__":
    app.run('127.0.0.1',port=8080,debug=True)