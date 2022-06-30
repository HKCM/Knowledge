import base64
import hashlib
import json
import hmac
from random import randint, random
from datetime import datetime, timedelta
from time import time

from flask import Flask, request, redirect, make_response

app = Flask(__name__)

redirect_uri = 'http://127.0.0.1:5000/client/passport'
users = {
    "ace": ["ace123"],
    "bill": ["bill123"],
    "candy": ["candy123"]
}

client_id = '123456'
users[client_id] = []
auth_code = {}
oauth_redirect_uri = []
TIMEOUT = 3600 * 2

def _get_signature(value):
    print(len(hmac.new(b'secret123456',value,digestmod=hashlib.sha1).digest()))
    return hmac.new(b'secret123456',value,digestmod=hashlib.sha1).digest()

def encode_token_bytes(data):
    return base64.urlsafe_b64encode(data)

def decode_token_bytes(data):
    return base64.urlsafe_b64decode(data)

def generate_token(data):
    """
    生成token
    :param data. dict type:
    :return:token <class 'bytes'>
    """
    data = data.copy()
    # 添加salt
    if "salt" not in data:
        data["salt"] = random()
    # 增加时效性
    if "expires" not in data:
        data["expires"] = time() + TIMEOUT
    # 转换为json
    payload = json.dumps(data).encode("utf8")
    # 生成签名
    sig = _get_signature(payload)
    return encode_token_bytes(payload + sig)

def verify_token(token):
    """
    验证token
    :param token:
    :return:
    """
    print(type(token))
    decode_token = decode_token_bytes(str(token))
    payload = decode_token[:-20]
    sig = decode_token[-20:]
    print("--------------payload",payload)
    print("sig",sig)
    expected_sig = _get_signature(payload)
    print("expected_sig",expected_sig)
    if sig != expected_sig:
        return {}
    data = json.loads(payload.decode("utf8"))
    if data.get("expires") >= time():
        return data
    return 0

    

def gen_auth_code(uri,user_id):
    code = randint(0,10000)
    auth_code[code] = [uri, user_id]
    return code

@app.route('/index', methods = ['POST','GET'])
def index():
    print(request.headers)
    return 'Hello'

@app.route('/login', methods = ['POST','GET'])
def login():
    """
    用户登录
    :return:
    """
    """
    print(request.headers['Authorization'])  # Basic ZXJpY3M6MTIzNDU2
    print(request.headers['Authorization'].split(' '))  # ['Basic', 'ZXJpY3M6MTIzNDU2']
    print(request.headers['Authorization'].split(' ')[-1])  # ZXJpY3M6MTIzNDU2
    print(base64.b64decode(request.headers['Authorization'].split(' ')[-1]))  # b'erics:123456'
    print(bytes.decode(base64.b64decode(request.headers['Authorization'].split(' ')[-1])))  # erics:123456
    print(str(base64.b64decode(request.headers['Authorization'].split(' ')[-1]), encoding='utf-8'))  # erics:123456
    """
    user_name,pw = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).decode().split(':')
    if users.get(user_name)[0] == pw:
        return generate_token(user_name)
    else:
        return 'error'


#################### 授权服务器的编写 ##########################
@app.route('/client/login', methods = ['POST','GET'])
def client_login():
    uri = 'http://localhost:5000/oauth?response_type=code&client_id={}&redirect_uri={}'.format(client_id,redirect_uri)
    return redirect(uri)

@app.route('/oauth', methods = ['POST','GET'])
def oauth():
    if request.method == "POST" and request.form['user']:
        u = request.form['user']
        p = request.form['pw']
        if users.get(u)[0] == p and oauth_redirect_uri:
            uri = oauth_redirect_uri[0] + '?code={}'.format(gen_auth_code(oauth_redirect_uri[0],u))
            expire_date = datetime.now() + timedelta(minutes=1)
            resp = make_response(redirect(uri))
            # 设置cookie,将用户名和密码写入cookie
            resp.set_cookie('login', '_'.join([u,p]),expires=expire_date)
            return resp
    if request.args.get('code'):
        auth_info = auth_code.get(int(request.args.get('code'))) 
        if auth_info[0] == request.args.get('redirect_uri'):
            return generate_token(dict(client_id=request.args.get('client_id'),userid=auth_info[1]))
    if request.args.get('redirect_uri'):
        oauth_redirect_uri.append(request.args.get('redirect_uri'))
        # 尝试读取cookie
        if request.cookies.get('login'):
            u,p = request.cookies.get('login').split('_')
            if users.get(u)[0] == p:
                uri = oauth_redirect_uri[0] + '?code={}'.format(gen_auth_code(oauth_redirect_uri[0],u))
                return redirect(uri)
    return '''
    <form action="" method="POST">
        <p><input type=text name=user></p>
        <p><input type=text name=pw></p>
        <p><input type=submit value=Login></p>
    </form>
    '''

@app.route('/client/passport',methods = ['POST','GET'])
def client_passport():
    code = request.args.get('code')
    uri = 'http://localhost:5000/oauth?grant_type=authorization_code&code={}&redirect_uri={}&client_id={}'.format(code,redirect_uri,client_id)
    return redirect(uri)


@app.route('/test', methods = ['POST','GET'])
def test():
    """
    用于请求数据测试
    :return:
    """
    token = request.args.get('token')
    res = verify_token(token)
    if res:
        return json.dumps(res)
    else:
        return 'error'

if __name__ == '__main__':
    app.run(debug=True)
