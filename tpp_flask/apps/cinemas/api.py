from flask_restful import Resource, reqparse

from apps.cinemas.models import Cinema, HallScheduling
from apps.main.models import Area
from apps.utils.field import CinemasFields, CinemaAreaFields, CinemaDetailFields, CinemaSeatsFields
from apps.utils.response_result import to_response_error, to_response_success


class CinemasResource(Resource):
    def __init__(self):
        # 影院区域信息 需要通过city来获取当前城市所有影院数据
        # city是通过点击头部地区列表获取
        self.parser = reqparse.RequestParser()
        # 城市和区域是通过id查询
        # 选择的城市
        self.parser.add_argument('city', type=str, default='2')
        # 当前城市的区域 根据区域标签显示
        self.parser.add_argument('district', type=str)
        # 排序要求
        self.parser.add_argument('sort', type=int)
        # 搜索影院名称的关键字
        self.parser.add_argument('keyword', type=str)

    def get(self):
        try:
            args = self.parser.parse_args()
            # 获取城市参数
            city = args.get('city')
            # 获取区域参数
            district = args.get('district')
            # 获取排序参数(综合排序,按评分排序)
            sort = args.get('sort')
            # 获取当前城市的影院数据
            query = Cinema.query.filter(Cinema.city == city)
            if district:
                # 判断是否有选中区域
                query = query.filter(Cinema.district == district)
            # 影院评分排序
            if sort == 1:
                # 降序
                query = query.order_by(Cinema.score.desc())
            elif sort == 2:
                # 升序
                query.order_by(Cinema.score.asc())

            cinemas = query.all()
            return to_response_success(data=cinemas, fields=CinemasFields.result_fields)
        except Exception as e:
            print(e)
            return to_response_error()


class CinemasDistrictResource(Resource):
    # 当前城市的所有区域
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('city', type=str, default='北京')

    def get(self):
        try:
            city = self.parser.parse_args().get('city')
            city = Area.query.filter(Area.short_name == city, Area.level == 2).first()
            districts = Area.query.filter(Area.parent_id == city.aid, Area.level == 3).all()
            return to_response_success(districts, fields=CinemaAreaFields.result_fields)
        except:
            return to_response_error()


# todo 添加影院排片(未完成)
class UpdateHallSchedulingResource(Resource):
    #
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass


"""
查看影院详情

1 影院的信息
2 影院排片信息
"""


# 影院详情
class CinemaDetailResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('cid', type=int, required=True)

    def get(self):
        cid = self.parser.parse_args().get('cid')
        hs_list = HallScheduling.query.filter(HallScheduling.cinema_id == cid).all()
        # for hs in hs_list:
        #     print(hs.cinema.name, '\n', hs.movie.show_name, '\n', hs.hall.name)
        movies = []
        for hs in hs_list:
            if hs.movie not in movies:
                movies.append(hs.movie)
        data = {
            'cinema': hs_list[0].cinema,
            'movies': movies,
            'movie': hs_list[0].movie,
            'hs_list': hs_list
        }
        return to_response_success(data=data, fields=CinemaDetailFields.result_fields)
        # cinema = Cinema.query.get(cid)
        # for hs in cinema.hs_list:
        #     print(cinema.name, '\n', hs.movie.show_name, '\n', hs.hall.name)


# 影院座椅
class CinemaSeatsResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('hs_id', type=int, required=True)

    def get(self):

        try:
            hs_id = self.parser.parse_args().get('hs_id')
            hs = HallScheduling.query.get(hs_id)
            seats = [seat.seat for seat in hs.ss_list]

            data_fields = {
                'seats': seats,
                'movie': hs.movie,
                'hall': hs.hall,
                'hall_scheduling': hs,
            }
            return to_response_success(data=data_fields, fields=CinemaSeatsFields.result_fields)
        except Exception as e:
            print(e)
            return to_response_error()

    def post(self):
        pass

    def put(self):
        pass
