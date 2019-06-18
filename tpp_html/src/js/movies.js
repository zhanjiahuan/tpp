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


