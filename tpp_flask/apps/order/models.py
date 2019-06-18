import datetime

from apps.cinemas.models import Cinema, HallScheduling, SeatScheduling, Seats
from apps.ext import db
from apps.main.models import Movie


class Order(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # 订单号
    no = db.Column(db.String(50), unique=True, nullable=False, index=True)
    # 关联电影
    movie_id = db.Column(db.Integer, db.ForeignKey(Movie.id))
    # 影院
    cinema_id = db.Column(db.Integer, db.ForeignKey(Cinema.cid))
    # 影厅
    hs_id = db.Column(db.Integer, db.ForeignKey(HallScheduling.hsid))
    # 座位
    ss_id = db.Column(db.Integer, db.ForeignKey(SeatScheduling.id))
    seat_id = db.Column(db.Integer, db.ForeignKey(Seats.sid))
    # 所购票数量
    number = db.Column(db.Integer, nullable=False)
    # 取票码
    ticket_code = db.Column(db.String(100))
    # 总金额
    total = db.Column(db.Numeric(7, 2))
    # 创建的时间
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    # 支付时间
    pay_date = db.Column(db.DateTime)
    # 状态 1: 未支付 2: 已支付 3: 支付已使用 4: 支付未使用
    status = db.Column(db.SmallInteger)
    # 支付有效期
    out_time = db.Column(db.DateTime, default=datetime.datetime.now() + datetime.timedelta(minutes=15))
    is_delete = db.Column(db.Boolean, default=True)
