def solution(id_pw, db):
    _db = dict(db)
    if not id_pw[0] in list(_db.keys()):
        return 'fail'
    
    if _db[id_pw[0]] != id_pw[1]:
        return 'wrong pw'
    
    return 'login'