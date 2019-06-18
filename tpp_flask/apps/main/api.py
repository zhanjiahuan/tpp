from flask_restful import Resource, reqparse
from sqlalchemy import func, desc

from apps.ext import cache
from apps.utils.field import MainMoviesFields, MainAreaFields, MainRatingFields
from apps.main.models import Area, Banner, Movie, Rating
from apps.utils.response_result import to_response_success, to_response_error

# 电影信息
from apps.utils.helper import get_score


class MainMoviesResource(Resource):
    def get(self):
        try:
            # 查询轮播表信息
            banners = Banner.query.filter(Banner.is_delete is False).order_by(Banner.order).all()
            hot_movies = Movie.query.filter(Movie.flag == 1).order_by(Movie.open_day).limit(5).offset(0).all()
            # hot_movies = Movies.query.filter(Movies.flag == 1).order_by(Movies.open_day).all()
            ready_movies = Movie.query.filter(Movie.flag == 2).order_by(Movie.open_day).limit(5).offset(0).all()
            # ready_movies = Movies.query.filter(Movies.flag == 2).order_by(Movies.open_day).all()
            hot_count = Movie.query.filter(Movie.flag == 1).count()
            ready_count = Movie.query.filter(Movie.flag == 2).count()

            get_score(hot_movies)
            get_score(ready_movies)

            data_fields = {
                'banners': banners,
                'hot_count': hot_count,
                'ready_count': ready_count,
                'hot_movies': hot_movies,
                'ready_movies': ready_movies,
            }

            return to_response_success(data=data_fields, fields=MainMoviesFields.result_fields)
        except Exception as e:
            return to_response_error()


# 地区信息

class MainAreaResource(Resource):
    @cache.cached(10 * 24 * 60)
    def get(self):
        try:
            first = Area.query.filter(Area.status == 1, Area.level == 2) \
                .with_entities(Area.first) \
                .group_by(Area.first) \
                .order_by(Area.first) \
                .all()
            initial = []
            for f in first:
                if f.first is not None:
                    areas = Area.query.filter(Area.status == 1, Area.level == 2, Area.first == f.first).all()
                    initial.append({'first': f.first, 'areas': areas})
            return to_response_success(data=initial, fields=MainAreaFields.result_fields)
        except Exception as e:
            return to_response_error()


# 热门电影排行
class HotRankingResource(Resource):
    def get(self):
        try:
            rantings = Rating.query.with_entities(
                Rating.movie_id, func.round(func.avg(Rating.score), 1).label('score'), Movie.show_name, Movie.image) \
                .join(Movie, Movie.id == Rating.movie_id) \
                .group_by(Rating.movie_id) \
                .order_by(desc('score')) \
                .limit(5).offset(0).all()
            data = [{'movie_id': ranting[0],
                     'score': ranting[1],
                     'name': ranting[2],
                     'image': ranting[3]} for ranting in rantings]
            return to_response_success(data=data, fields=MainRatingFields.result_fields)
        except Exception as e:
            return to_response_error()
