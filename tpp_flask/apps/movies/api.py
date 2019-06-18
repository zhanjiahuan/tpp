from flask_restful import Resource, reqparse

from apps.main.models import Movie
from apps.movies.models import Goods
from apps.utils.field import MoviesFields
from apps.utils.response_result import to_response_success, to_response_error
from apps.utils.helper import get_score


class MoviesResource(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument('page', type=int, default=1)
        self.parse.add_argument('size', type=int, default=9)
        # 1 表示正在热映   2 表示即将上映
        self.parse.add_argument('flag', type=int, default=1)

    def get(self):
        try:
            goods = Goods.query.all()
            args = self.parse.parse_args()
            page = args.get('page')
            size = args.get('size')
            flag = 1 if args.get('flag') == 1 else 2
            pagination = Movie.query.filter(Movie.flag == flag).paginate(page=page, per_page=size, error_out=False)
            get_score(pagination.items)
            data_fields = {
                'pagination': pagination,
                'movies': pagination.items,
            }
            return to_response_success(data=data_fields, fields=MoviesFields.result_fields)
        except Exception as e:
            return to_response_error()