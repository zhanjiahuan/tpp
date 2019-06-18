$(function () {
    $('.foot').load('../base/html/footer.html');
    let city_codes = location.search;
    let city_code = '';
    if (city_codes.length > 0) {
        city_codes = city_codes.split('=');
        for (let i = 0; i < city_codes.length; i++) {
            if (city_codes[i] === '?city') {
                city_code = city_codes[i + 1];
                load_city(city_code);
            }
        }
    } else {
        $('#city_name').text('北京');
    }

    init_area();
    init_movies();
    area_event();
});

function area_event() {
    $('.cityWrap').mouseover(function () {
        $(this).addClass('cityWrap_hover');
    });
    $('.cityWrap').mouseout(function () {
        $(this).removeClass('cityWrap_hover');
    });

}

function load_city(code) {
    if (code.length <= 6) {
        // alert(code);
        $.get(MAIN_AREA_URL, function (result) {
            if (get_success(result)) {
                for (let areas of result.data) {
                    for (let area of areas.areas) {
                        if (code === area.zip_code) {
                            $('#city_name').text(area.short_name);
                            break
                        }
                    }
                }
            }
        })
    }
}

function init_area() {
    let $city_ul = $('<ul>');

    $.get(MAIN_AREA_URL, function (result) {
        if (get_success(result)) {
            for (let areas of result.data) {
                let $city_li = $('<li>');
                $('.M-cityList')
                    .append(
                        $city_ul
                            .append(
                                $city_li
                                    .append(
                                        $('<label>').text(areas.first)
                                    )
                            )
                    );
                for (let area of areas.areas) {
                    $city_li
                        .append(
                            $('<a>').text(area.short_name).attr('href', '?city=' + area.zip_code)
                        );
                }
            }
        }

    })
}

function init_movies() {
    let $hot_div = $('#hot');
    let $ready_div = $('#ready');
    $.get(MAIN_MOVIES_URL, function (result) {
        if (get_success(result)) {
            $('#main_movies')
                .append(
                    $('<a>').addClass('tab-control-item current').attr('id', 'hot_movies')
                        .text('正在热映(' + result.data.hot_count + ')')
                )
                .append(
                    $('<a>').addClass('tab-control-item').attr('id', 'ready_movies')
                        .text('即将上映(' + result.data.ready_count + ')')
                )
                .append(
                    $('<a>').addClass('more').attr('href', 'movies.html?flag=1')
                        .text('查看全部 >')
                );
            load_movie($hot_div, result.data.hot_movies);
            load_movie($ready_div, result.data.ready_movies);

            $('#hot_movies').on('click', function () {
                $(this).addClass('current');
                $('#ready_movies').removeClass('current');
                $hot_div.show();
                $ready_div.hide();
            });

            $('#ready_movies').on('click', function () {
                $(this).addClass('current');
                $('#hot_movies').removeClass('current');
                $hot_div.hide();
                $ready_div.show();
            });

            // $('.more').on('click',function () {
            //     window.location.href="movies.html?flag=2";
            // });
        }
    });


}

function load_movie($div, movies) {
    for (let movie of movies) {
        let model = '';
        if (movie.screening_model === '3D') {
            model = 't-201'
        } else if (movie.score === null) {
            model = 't-103'
        }
        let movie_card = '';
        let movie_card_text = '';
        if ($div.attr('id') === 'hot') {
            movie_card = 'movie-card-buy';
            movie_card_text = '选座购票';
        } else {
            movie_card = 'movie-card-soon';
            movie_card_text = '上映时间' + movie.open_day;
        }
        $div
            .append(
                $('<div>').addClass('movie-card-wrap')
                    .append(
                        $('<a>').addClass('movie-card')
                            .append(
                                $('<div>').addClass('movie-card-tag')
                                    .append(
                                        $('<i>').addClass(model)
                                    )
                            )
                            .append(
                                $('<div>').addClass('movie-card-poster')
                                    .append(
                                        $('<img width="160" height="224">')
                                            .attr('src', IMG_HEAD + movie.image)
                                    )
                            )
                            .append(
                                $('<div>').addClass('movie-card-name')
                                    .append(
                                        $('<span>').addClass('bt-l').text(movie.show_name)
                                    )
                                    .append(
                                        $('<span>').addClass('bt-r').text(movie.score)
                                    )
                            )
                            .append(
                                $('<div>').addClass('movie-card-info')
                                    .append(
                                        $('<div>').addClass('movie-card-mask')
                                    )
                                    .append(
                                        $('<div>').addClass('movie-card-list')
                                            .append(
                                                $('<span>').text('导演：' + movie.director)
                                            )
                                            .append(
                                                $('<span>').text('主演：' + movie.leading_role)
                                            )
                                            .append(
                                                $('<span>').text('类型：' + movie.type)
                                            )
                                            .append(
                                                $('<span>').text('地区：' + movie.country)
                                            )
                                            .append(
                                                $('<span>').text('语言：' + movie.language)
                                            )
                                            .append(
                                                $('<span>').text('片长：' + movie.duration + '分钟')
                                            )
                                    )
                            )
                    )
                    .append(
                        $('<a>').addClass(movie_card).text(movie_card_text)
                    )
            )
    }
}