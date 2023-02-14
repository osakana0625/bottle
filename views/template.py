# coding:utf-8
from bottle import run, route, template, get, request

# トップページ
@route("/")
def index():
    return template('index')

# フォーム入力結果ページ
@route("/kakoku",method="GET")
def kakoku():

    username = request.query.getunicode("name")
	
    return template('kakoku', username=username)
	

	



# プロセスの起動
if __name__ == "__main__":
    run(host='localhost', port=8084, reloader=True, debug=True)

