from flask_restful import fields

from apps.utils.constant import RESPONSE_SUCCESS_STATUS, RESPONSE_SUCCESS_MSG


class MainMoviesFields:
    banner_fields = {
        'bid': fields.Integer,
        'title': fields.String,
        'image': fields.String,
        'detail_url': fields.String,
    }
    movie_fields = {
        'id': fields.Integer,
        'show_name': fields.String,
        'show_name_en': fields.String,
        'director': fields.String,
        'leading_role': fields.String,
        'type': fields.String,
        'country': fields.String,
        'language': fields.String,
        'duration': fields.String,
        'screening_model': fields.String,
        'open_day': fields.String,
        'image': fields.String,
        'score': fields.String,
    }
    data_fields = {
        'banners': fields.List(fields.Nested(banner_fields)),
        'hot_count': fields.Integer,
        'ready_count': fields.Integer,
        'hot_movies': fields.List(fields.Nested(movie_fields)),
        'ready_movies': fields.List(fields.Nested(movie_fields)),
    }

    result_fields = {
        'status': fields.Integer,
        'msg': fields.String,
        # 'data': fields.List(fields.Nested(data_fields))
        'data': fields.Nested(data_fields)
    }


class MainAreaFields:
    area_fields = {
        'aid': fields.Integer,
        'parent_id': fields.Integer,
        'short_name': fields.String,
        'name': fields.String,
        'merger_name': fields.String,
        # 'level': fields.String,
        'zip_code': fields.String,
        'pinyin': fields.String,
        'first': fields.String,
        'is_hot': fields.String,
    }

    first_fields = {
        'first': fields.String,
        'areas': fields.Nested(area_fields)
    }

    result_fields = {
        'status': fields.Integer,
        'msg': fields.String,
        'data': fields.List(fields.Nested(first_fields))
    }


class MainRatingFields:
    data_fields = {
        'movie_id': fields.Integer,
        'score': fields.Float,
        'image': fields.String,
        'name': fields.String,
    }

    result_fields = {
        'status': fields.Integer(default=RESPONSE_SUCCESS_STATUS),
        'msg': fields.String(default=RESPONSE_SUCCESS_MSG),
        'data': fields.List(fields.Nested(data_fields))
    }


class MoviesFields:
    paginate_fields = {
        'pages': fields.Integer,
        'total': fields.Integer,
    }

    data_fields = {
        'pagination': fields.Nested(paginate_fields),
        'movies': fields.Nested(MainMoviesFields.movie_fields),
    }

    result_fields = {
        'status': fields.Integer,
        'msg': fields.String,
        'data': fields.Nested(data_fields)
    }


class CinemasFields:
    cinemas_fields = {
        'cid': fields.Integer(),
        'name': fields.String(),
        'address': fields.String(),
        'phone': fields.String(),
        'score': fields.Float(),

    }

    result_fields = {
        'status': fields.Integer(default=200),
        'msg': fields.String(default='success'),
        'data': fields.List(fields.Nested(cinemas_fields))
    }


class CinemaAreaFields:
    district_fields = {
        'name': fields.String,
        'aid': fields.Integer
    }

    result_fields = {
        'status': fields.Integer(default=200),
        'msg': fields.String(default='success'),
        'data': fields.List(fields.Nested(district_fields))
    }


class CinemaDetailFields:
    hall_fields = {
        'hid': fields.Integer,
        'name': fields.String,
        'screen_type': fields.Integer,
        'seat_num': fields.Integer,
    }
    hs_fields = {
        'hsid': fields.Integer,
        'start': fields.DateTime(dt_format='iso8601'),
        'end': fields.DateTime(dt_format='iso8601'),
        'origin_price': fields.Float,
        'current_price': fields.Float,
        'hall': fields.Nested(hall_fields),
    }
    data_fields = {
        'cinema': fields.Nested(CinemasFields.cinemas_fields),
        'movies': fields.List(fields.Nested(MainMoviesFields.movie_fields)),
        'movie': fields.Nested(MainMoviesFields.movie_fields),
        'hs_list': fields.List(fields.Nested(hs_fields)),
    }

    result_fields = {
        'status': fields.Integer(default=200),
        'msg': fields.String(default='success'),
        'data': fields.Nested(data_fields)
    }


class CinemaSeatsFields:
    movie_fields = {
        'id': fields.Integer,
        'image': fields.String,
        'screening_model': fields.String,
        'show_name': fields.String,
    }

    seat_fields = {
        'x': fields.Integer,
        'y': fields.Integer,
        'is_choose': fields.Boolean,
    }

    cinema_fields = {
        'cid': fields.Integer,
        'name': fields.String,
    }

    hall_fields = {
        'hid': fields.Integer,
        'name': fields.String,
        'cinema': fields.Nested(cinema_fields)
    }

    hs_fields = {
        'hsid': fields.Integer,
        'status': fields.Integer,
        'start': fields.DateTime,
    }
    data_fields = {
        'seats': fields.Nested(seat_fields),
        'movie': fields.Nested(movie_fields),
        'hall': fields.Nested(hall_fields),
        'hall_scheduling': fields.Nested(hs_fields),
    }

    result_fields = {
        'status': fields.Integer(default=200),
        'msg': fields.String(default='success'),
        'data': fields.Nested(data_fields)
    }


class OrderSuccessFields:
    result_fields = {
        'status': fields.Integer(default=200),
        'msg': fields.String(default='支付成功'),
        'data': fields.String,

    }
