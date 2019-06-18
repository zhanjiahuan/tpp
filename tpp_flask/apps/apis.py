from flask_restful import Api

from apps.cinemas.api import CinemasResource, CinemasDistrictResource, CinemaDetailResource, \
    CinemaSeatsResource, UpdateHallSchedulingResource
from apps.main.api import MainMoviesResource, MainAreaResource, HotRankingResource
from apps.movies.api import MoviesResource
from apps.order.api import OrderResource

api = Api(prefix='/api/v1')


def init_api(app):
    api.init_app(app)


api.add_resource(MainMoviesResource, '/main/movies/')
api.add_resource(MainAreaResource, '/main/area/')
api.add_resource(HotRankingResource, '/main/ranking/')
api.add_resource(MoviesResource, '/movies/')
api.add_resource(CinemasResource, '/cinemas/')
api.add_resource(CinemasDistrictResource, '/cinemas/district/')
api.add_resource(UpdateHallSchedulingResource, '/cinemas/update/')
api.add_resource(CinemaDetailResource, '/cinemas/detail/')
api.add_resource(CinemaSeatsResource, '/cinemas/seats/')
api.add_resource(OrderResource, '/order/')
