$(function () {
    $('.foot').load('../base/html/footer.html');
    let url_args = location.search.split('&');
    // let city_code = '';
    let mid;
    if (url_args.length > 0) {
        for (let arg of url_args) {
            let city_codes = arg.split('=');
            for (let i = 0; i < city_codes.length; i++) {
                if (city_codes[i] === '?city') {
                    // let city_code = city_codes[i + 1];
                    load_city(city_codes[i + 1]);
                } else if (city_codes[i] === 'mid') {
                    mid = city_codes[i + 1];
                    init_movie(mid);
                }
            }
        }
    }
    init_area(mid);
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

function init_area(mid) {
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
                            $('<a>').text(area.short_name).attr('href', '?city=' + area.zip_code + '&mid=' + mid)
                        );
                }
            }
        }

    })
}

function init_movie(mid) {
    $.get(MAIN_MOVIES_URL, function (result) {

        if (get_success(result)) {
            let movies = [].concat(result.data.hot_movies, result.data.ready_movies);
            for (let movie of movies) {
                if (parseInt(mid) === movie.id){
                    $('#movie_content')
                        .append(
                            $('<h3>').addClass('cont-title').text(movie.show_name)
                                .append(
                                    $('<i>').text(' （'+ movie.show_name_en +'） ')
                                )
                                .append(
                                    $('<em>').addClass('score').text(movie.score)
                                )
                        )
                        .append(
                            $('<div>').addClass('cont-pic')
                                .append(
                                    $('<img width="230" height="300">').attr('src', IMG_HEAD + movie.image)
                                )
                        )
                        .append(
                            $('<ul>').addClass('cont-info')
                                .append(
                                    $('<li>').text('导演：' + movie.director)
                                )
                                .append(
                                    $('<li>').text('主演：' + movie.leading_role)
                                )
                                .append(
                                    $('<li>').text('类型：' + movie.type)
                                )
                                .append(
                                    $('<li>').text('制片国家/地区：' + movie.country)
                                )
                                .append(
                                    $('<li>').text('片长：' + movie.duration + '分钟')
                                )
                                .append(
                                    // todo 数据库没有介绍
                                    $('<li class="J_shrink shrink">').text('剧情介绍：' + '暂无介绍...')
                                )
                        )
                        .append(
                            $('<div>').addClass('cont-time').text('上映时间' + movie.open_day)
                        );
                }

            }

        }
    });

}