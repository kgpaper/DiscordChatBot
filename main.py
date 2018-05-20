
#
# 투표개설페이지 알고리즘
# 1. 투표개설페이지에 접속 (get)
# 2. 투표 개설 입력사항들을 입력
# 3. 투표개설 클릭 (post)
# 4. DB(임시 : sqlite3)에 랜덤주소 + 데이터 저장
# 5. 투표개설완료 페이지 출력 및 디스코드에 해당 투표페이지 전달
#
# 투표페이지 알고리즘
# 1. 사용자가 투표페이지(get) 접속
# 2. DB접속 후, 저장된 url이 있는가 확인
# 3. 없으면 404, 있으면 데이터를 불러와서 voteview.html 출력
#

from flask import Flask, render_template, jsonify, request, redirect, session, url_for

application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@application.route("/createvote", methods=["POST","GET"])
def create_vote():
    if request.method == "POST":

        print(request.form)


    return render_template('votecreate.html')


@application.route('/vote/<url>')
def post(url):
    print(url)
    return render_template('voteview.html')


if __name__ == "__main__":
    application.run(host='0.0.0.0',debug=True)