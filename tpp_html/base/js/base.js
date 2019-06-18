const BASE_URL = 'http://127.0.0.1:5000/api/v1';
const MAIN_MOVIES_URL = BASE_URL + '/main/movies/';
const MOVIES_URL = BASE_URL + '/movies/';
const MAIN_AREA_URL = BASE_URL + '/main/area/';

const IMG_HEAD = 'https://img.alicdn.com/bao/uploaded/';
const PAGE_SIZE = 9;

function get_success(result) {
    return (result && result.status === 200)
}