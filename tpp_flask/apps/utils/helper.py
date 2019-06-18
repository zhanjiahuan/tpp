import datetime
import random

from sqlalchemy import func

from apps.main.models import Rating


def get_score(movies):
    '''
    获取电影评分
    :param movies: 电影模型
    '''

    for movie in movies:
        ranting = Rating.query.filter(Rating.movie_id == movie.id) \
            .with_entities(func.round(func.avg(Rating.score), 1)) \
            .group_by(Rating.movie_id).all()
        if ranting:
            movie.score = ranting[0][0]


def product_code():
    data_code = datetime.datetime.now().strftime('%Y%m%d%H%I%S%f')
    random_code = random.randint(1000, 9999)
    return '{}{}'.format(data_code, str(random_code))


if __name__ == '__main__':
    print(product_code())
