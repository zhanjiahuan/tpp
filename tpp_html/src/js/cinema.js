let sort = 1;
$(function () {
    let city_code = location.search.split('=')[1];
    if (city_code !== undefined) {
        load_city(city_code);
    }

    init_area();
    area_event();

    // alert(city_name);
    // load_area_data();
    // load_cinema_data();

    $('#sorce_id').click(function () {
        if (sort === 1) {
            load_cinema_data(-1, sort);
            sort = 2;
        } else {
            load_cinema_data(-1, sort);
            sort = 1;
        }

    })
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
            // todo 根据城市名字显示不同影院信息
            $('#city_name').text('深圳');
            let city_name = $('#city_name').text();
            $('.nav_name').text(city_name);
            load_area_data(city_name);
            load_cinema_data();
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
                            $('<a>').text(area.short_name)
                                .attr('href', 'JavaScript:void(0);')
                                // .attr('href', '?city=' + area.zip_code)
                                .click(function () {
                                    $('#city_name').text(area.short_name);
                                    $('.nav_name').text(area.short_name);
                                    load_area_data(area.short_name);
                                    // load_cinema_data(area.aid);
                                })
                        );
                }
            }
        }

    })
}

let area_url = 'http://127.0.0.1:5000/api/v1/cinemas/district/';

//加载城市区县信息
function load_area_data(city_name) {
    let select_div = $('.select-tags');
    let data = {'city': city_name};
    $.get(area_url, data, function (result) {
        if (result && result.status === 200) {
            select_div.append(
                $('<a>').text('全部区域')
                    .attr('href', '')
                    .addClass('current all_area')
                // .click(function () {
                //     $(this).addClass('current');
                //     $('.select_div').find('<a>').removeClass('current');
                // })
            );
            for (let area of result.data) {
                select_div.append(
                    $('<a>').text(area.name)
                        .data('aid', area.aid)
                        .attr('href', 'JavaScript:void(0);')
                        .click(function () {
                            // $(this).addClass('current');
                            // $('.all_area').removeClass('current');
                            // $('.select_div').find('<a>').removeClass('current');
                            load_cinema_data($(this).data('aid'))
                        })
                )
            }
        }
    })
}

//加载影院相关的数据
let cinema_url = 'http://127.0.0.1:5000/api/v1/cinemas/';

function load_cinema_data(dist, sort) {
    let data = {'city': '1988', 'district': dist, 'sort': sort};
    console.log(data);
    $.get(cinema_url, data, function (result) {
        let content = '';
        if (result && result.status === 200) {
            for (let cinema of result.data) {
                content += '<li>\n' +
                    '                <div class="detail-right">\n' +
                    '                    <div class="right-score">评分：<strong> ' + cinema.score +
                    ' </strong></div>\n' +
                    '                    <div class="right-fav "></div>\n' +
                    '                    <div class="right-buy "><a href="">选座</a></div>\n' +
                    '                </div>\n' +
                    '                <a href="" class="detail-left pictures">\n' +
                    '                    <span><img src="' + 'https://gw.alicdn.com/tfscom/i4/TB1XihcjnqWBKNjSZFAXXanSpXa_.jpg' +
                    '" alt=""/></span>\n' +
                    '                </a>\n' +
                    '                <div class="detail-middle">\n' +
                    '                    <div class="middle-hd">\n' +
                    '                        <h4>\n' +
                    '                            <a href="">' + cinema.name +
                    '</a>\n' +
                    '                        </h4>\n' +
                    '                    </div>\n' +
                    '                    <div class=middle-p>\n' +
                    '                        <div class="middle-p-list"><i>地址：</i><span class="limit-address"></span><a\n' +
                    '                                class="J_miniMap"\n' +
                    '                                href=""\n' +
                    '                                data-points="116.449826,39.919551">[地图]</a></div>\n' +
                    '                        <div class="middle-p-list"><i>电话：</i>' + cinema.phone + '</div>\n' +
                    '                        <div class="middle-p-list"><i>更多：</i><a class="middle-more">影院服务</a><a\n' +
                    '                                class="middle-more"\n' +
                    '                                href="">交通信息</a>\n' +
                    '                        </div>\n' +
                    '                    </div>\n' +
                    '                </div>\n' +
                    '            </li>';

            }
            $('.sortbar-detail').html(content)
        }

    })
}