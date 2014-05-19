/*global $*/

/* 
* @Author: hanjiyun
* @Date:   2014-05-19 13:16:35
* @Last Modified by:   hanjiyun
* @Last Modified time: 2014-05-19 14:44:11
*/

$(function () {
    console.log(1);

    var ufoList = $('.ufo');
    var testNum;

    function getNewData() {
        $.ajax({
            type : 'GET',
            dataType: 'json',
            url:  'http://192.168.108.178:9000/teams/',
            success: function (data) {
                // console.log(data);

                // $('.steps').fadeIn();

                for (var index = 0, len = data.results.length; index < len; index++) {
                    var select = index + 1;
                    // console.log($('.ufo-' + select));
                    $('.ufo-' + select).parents('.steps').eq(0).addClass('step-' + data.results[index].progress);
                }

                setTimeout(function () {
                    getNewData();
                    console.log('重新请求');
                }, 1000);
            }
        });
    }

    getNewData();
});

