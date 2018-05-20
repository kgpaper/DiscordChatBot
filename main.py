
#
# 투표개설페이지 알고리즘 (월요일까지 완성)
# 1. 투표개설페이지에 접속 (get)
# 2. 투표 개설 입력사항들을 입력
# 3. 투표개설 클릭 (post)
# 4. DB(임시 : sqlite3)에 랜덤주소 + 데이터 저장
# 5. 투표개설완료 페이지 출력 및 디스코드에 해당 투표페이지 전달
#
# 투표페이지 알고리즘 (화요일까지 완성)
# 1. 사용자가 투표페이지(get) 접속
# 2. DB 접속 후, 저장된 url이 있는가 확인
# 3. 없으면 404, 있으면 데이터를 불러와서 voteview.html 출력
# 4.


# db - vote table
# primary_number, manager, subject, description, content, anonymous

from flask import Flask, render_template, jsonify, request, redirect, session, url_for
import other, db_info
from flaskext.mysql import MySQL


application = Flask(__name__)

mysql = MySQL()
application.config['MYSQL_DATABASE_USER'] = db_info.db_user
application.config['MYSQL_DATABASE_PASSWORD'] = db_info.db_password
application.config['MYSQL_DATABASE_DB'] = db_info.db_name
application.config['MYSQL_DATABASE_HOST'] = db_info.db_host
mysql.init_app(application)
application.secret_key = '???'


@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@application.route("/createvote", methods=["POST","GET"])
def create_vote():
    if request.method == "POST":

        primary_vote_number = other.create_random_string()


        print(request.form)
    return render_template('votecreate.html')


@application.route('/vote/<url>')
def post(url):
    print(url)
    return render_template('voteview.html')


if __name__ == "__main__":
    application.run(host='0.0.0.0',debug=True)