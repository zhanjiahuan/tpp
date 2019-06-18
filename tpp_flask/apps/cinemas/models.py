from apps.ext import db
from apps.main.models import Movie


class Cinema(db.Model):
    cid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True, unique=True)
    city = db.Column(db.String(64), nullable=False)
    district = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(16), nullable=False)
    score = db.Column(db.Float(3, 1))
    hall_num = db.Column(db.Integer, nullable=False)
    # 服务费
    service_money = db.Column(db.Numeric(3, 1))
    # 限购数量
    astrict = db.Column(db.Integer)
    # 电影院状态 True营业 False不营业
    flag = db.Column(db.Integer, default=1)
    is_delete = db.Column(db.Boolean, default=True)

    hs_list = db.relationship('HallScheduling', lazy='dynamic', backref='cinema')
    halls = db.relationship('Hall', lazy='dynamic', backref='cinema')


class Hall(db.Model):
    hid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 影厅的名字
    name = db.Column(db.String(100), nullable=False)
    # 1表示 2D 21 3D 3表示4D  4 表示  3D MAX
    screen_type = db.Column(db.Integer, nullable=False)
    # 影厅的座位
    seat_num = db.Column(db.Integer, nullable=False)
    # 影厅的状态 1 表示营业  2 表示打烊
    status = db.Column(db.Integer, default=1)
    # 是否删除
    is_delete = db.Column(db.Boolean, default=True)
    cid = db.Column(db.Integer, db.ForeignKey(Cinema.cid))
    hs_list = db.relationship('HallScheduling', lazy='dynamic', backref='hall')


class Seats(db.Model):
    sid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 1.普通  2.豪华 3 超豪华
    type = db.Column(db.Integer, nullable=False)
    # 座位的坐标
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    # True 正常  False 损毁
    status = db.Column(db.Boolean, default=True)
    # 是否可选
    is_choose = db.Column(db.Boolean, default=True)
    # 是否删除
    is_delete = db.Column(db.Boolean, default=True)
    #     外键设置
    cid = db.Column(db.Integer, db.ForeignKey(Cinema.cid))
    hid = db.Column(db.Integer, db.ForeignKey(Hall.hid))
    ss = db.relationship('SeatScheduling', uselist=False,backref='seat')


# 影厅拍片表
class HallScheduling(db.Model):
    hsid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 1未开始 2正在放映 3结束放映
    status = db.Column(db.Integer, default=1)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    origin_price = db.Column(db.Numeric(7, 2))
    current_price = db.Column(db.Numeric(7, 2))
    movie_id = db.Column(db.Integer, db.ForeignKey(Movie.id))
    cinema_id = db.Column(db.Integer, db.ForeignKey(Cinema.cid))
    hall_id = db.Column(db.Integer, db.ForeignKey(Hall.hid))
    is_delete = db.Column(db.Boolean, default=True)
    ss_list = db.relationship('SeatScheduling', lazy='dynamic', backref='hs')
    # hs_list = db.relationship('Movie', lazy='dynamic', backref='hs_list')


# 座位排期表
class SeatScheduling(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seat_id = db.Column(db.Integer, db.ForeignKey(Seats.sid))
    hall_id = db.Column(db.Integer, db.ForeignKey(Hall.hid))
    hs_id = db.Column(db.Integer, db.ForeignKey(HallScheduling.hsid))
    is_delete = db.Column(db.Boolean, default=False)
