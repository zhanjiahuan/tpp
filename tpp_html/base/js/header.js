$(function () {
    let city_codes = location.search.split('=');
    let city_code = '';
    if (city_codes[0] === '?city' && city_codes[1] !== undefined) {
        city_code = city_codes[1];
        load_city(city_code);
    }
    init_area();
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