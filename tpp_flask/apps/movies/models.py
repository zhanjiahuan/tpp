import datetime

from apps.ext import db


class Goods(db.Model):
    __tablename__ = "goods"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    good_id = db.Column(db.String(32), unique=True)

    cid = db.Column(db.Integer)
    # shop_id = db.Column(db.Integer, db.ForeignKey(GcProperty.id))

    # 外键
    # cid = db.Column(db.Integer)
    # shop_id = db.Column(db.Integer)
    # brand_id = db.Column(db.Integer)
    ################
    good_name = db.Column(db.String(255), nullable=False)
    show_img = db.Column(db.String(255))
    good_desc = db.Column(db.String(255))
    good_price = db.Column(db.Numeric(11, 2))

    # stocks = db.Column(db.Integer)
    # good_tips = db.Column(db.String(255))
    # is_hot = db.Column(db.Integer)
    # is_new = db.Column(db.Integer)
    # is_recom = db.Column(db.Integer)
    # is_sale = db.Column(db.Integer)
    # good_status = db.Column(db.Integer)
    # sale_volume = db.Column(db.Integer)
    # sale_time = db.Column(db.DateTime, default=datetime.datetime.now())
    # # 0:删除 1:有效
    # is_delete = db.Column(db.Boolean, default=1)
    # # 创建时间
    # create_time = db.Column(db.DateTime, default=datetime.datetime.now())