function out(){
    var elements_city = document.getElementById("city");
    var f = elements_city.value

    var elements_temp = document.getElementsByName("temp_yn");


    var a = kakikomi(elements_temp);

    var elements_wind = document.getElementsByName("wind_yn");

    var b = kakikomi(elements_wind);

    var elements_d_wind = document.getElementsByName("wind_d_yn");

    var c = kakikomi(elements_d_wind);

    var elements_clouds = document.getElementsByName("clouds");

    var d = kakikomi(elements_clouds);

    var elements_times = document.getElementById("times");
    var e = elements_times.value;

    var res = document.getElementById("result");

    var hinagata = "<div class='alert alert-warning' role='alert'><p id = 'text'>import requests<br>txt = requests.post('http://127.0.0.1:8000/weather/"
    res.innerHTML = hinagata + f + "'" + ", data = {'temp_yn':" + "'" + a + "'" + ", 'wind_yn':" + "'" + b + "'" + ", 'wind_d_yn':" + "'" + c + "'" + ", 'clouds':" + "'" + d + "'" + ", 'times':" + "'" + e + "'})<br>print(txt.json())</p>" + "<input type='button' onclick = 'copy(this)' class='btn btn-outline-secondary' data-bs-toggle='button' value='コピーする'></div>";
}

function out2(){
    var elements_city = document.getElementById("city2");
    var f = elements_city.value

    var elements_temp = document.getElementsByName("temp_yn2");


    var a = kakikomi(elements_temp);

    var elements_wind = document.getElementsByName("wind_yn2");

    var b = kakikomi(elements_wind);

    var elements_d_wind = document.getElementsByName("wind_d_yn2");

    var c = kakikomi(elements_d_wind);

    var elements_clouds = document.getElementsByName("clouds2");

    var d = kakikomi(elements_clouds);

    var elements_times = document.getElementById("times2");
    var e = elements_times.value;

    var res = document.getElementById("result");

    var hinagata = "<div class='alert alert-warning' role='alert'><p id = 'text'>import requests<br>txt = requests.post('http://127.0.0.1:8000/weather2/"
    res.innerHTML = hinagata + f + "'" + ", data = {'temp_yn2':" + "'" + a + "'" + ", 'wind_yn2':" + "'" + b + "'" + ", 'wind_d_yn2':" + "'" + c + "'" + ", 'clouds2':" + "'" + d + "'" + ", 'times2':" + "'" + e + "'})<br>print(txt.json())</p>" + "<input type='button' onclick = 'copy(this)' class='btn btn-outline-secondary' data-bs-toggle='button' value='コピーする'></div>";
}


function kakikomi(a){
    for ( var result="", i=a.length; i--; ) {
        if ( a[i].checked ) {
            var result = a[i].value ;
            break ;
        }
    }
    return result;
}

function copy(a){
    var text = document.getElementById("text");
    copy_do(text);
    a.value = "コピーしました";
}


function copy_do(text){
    var range = document.createRange();
    range.selectNodeContents(text);
    var selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    // 選択したものをコピーする.
    document.execCommand('copy');
    // コピー内容の選択を解除する.
    selection.removeAllRanges();
}