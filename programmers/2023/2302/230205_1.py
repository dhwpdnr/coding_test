def solution(id_pw, db):
    for i in db:
        user_id = i[0]
        pw = i[1]
        if user_id == id_pw[0]:
            if pw == id_pw[1]:
                return 'login'
            else:
                return 'wrong pw'
    return 'fail'

    # 프로그래머스 연습문제 로그인 성공?
