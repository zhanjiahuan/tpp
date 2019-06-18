from flask_restful import Resource, reqparse
from sqlalchemy.testing import in_

from apps.cinemas.models import HallScheduling, Seats
from apps.ext import db
from apps.order.models import Order
from apps.utils.field import OrderSuccessFields
from apps.utils.helper import product_code
from apps.utils.response_result import to_response_error, to_response_success


class OrderResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('uid', type=int, required=True)
        self.parser.add_argument('movie_id', type=int, required=True)
        self.parser.add_argument('hs_id', type=int, required=True)
        self.parser.add_argument('seat_ids', type=int, required=True, action='append')
        self.parser.add_argument('ss_id', type=int, default=1)

    def post(self):
        args = self.parser.parse_args()
        uid = args.get('uid')
        movie_id = args.get('movie_id')
        hs_id = args.get('hs_id')
        seat_ids = args.get('seat_ids')
        ss_id = args.get('ss_id')

        try:
            # db.session.begin()
            # 查询座位是否可选
            seats = Seats.query.filter(Seats.sid.in_(seat_ids)).all()
            if is_choose(seats):
                # 锁定座位
                for seat in seats:
                    seat.is_choose = False
                db.session.add_all(seats)

                # 生成订单号
                no = product_code()
                # 查询票价
                hs = HallScheduling.query.get(hs_id)
                # 计算总金额
                total = hs.current_price * 2
                # 生成订单
                order = Order(no=no, number=2, total=total, status=1,
                              movie_id=movie_id,
                              hs_id=hs_id,
                              cinema_id=1,
                              ss_id=1,
                              seat_id=1)

                # 提交订单
                db.session.add(order)
                db.session.commit()
                return to_response_success(data=no, fields=OrderSuccessFields.result_fields)
            else:
                return to_response_error(status='-1', msg='座位已经被选了')
        except:
            db.session.rollback()
            return '失败'


def is_choose(seats):
    for seat in seats:
        if seat.is_choose:
            continue
        else:
            return False
    return True
