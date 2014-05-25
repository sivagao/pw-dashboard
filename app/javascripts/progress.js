/*global $, _*/

/*
 * @Author: hanjiyun
 * @Date:   2014-05-20 13:09:33
 * @Last Modified by:   hanjiyun
 * @Last Modified time: 2014-05-26 02:14:57
 */


$(function () {

    var limitNum = 5;
    var isFirst = true;
    var textTimer;
    var apiURL = 'http://192.168.100.47:4000/tasks/';
    var taskTpl = _.template($('#task-list-tpl').html());
    var taskList = $('#progress-cont');

    getNewData();
    setInterval(getNewData, 5000);

    function textAnimate() {
        var idx = 0;
        var _spanLen = $('.rw-sentence span').hide().length;
        textTimer = setInterval(function () {
            $('.rw-sentence span:visible').fadeOut('fast');
            $('.rw-sentence span').eq(idx % _spanLen).fadeIn({
                delay: 200,
                duration: 600
            });
            idx += 1;
        }, 3500);
    }

    function getNewData() {
        $.ajax({
            type: 'GET',
            dataType: 'json',
            url: apiURL,
            success: function (res) {
                res.size = res.data.length;
                if (res.size === 0 && isFirst) {
                    $('#no-data').show();
                    textAnimate();
                    isFirst = false;
                    return;
                }

                if (res.size === 0 && !isFirst) {
                    return;
                }

                res.data = _.last(_.shuffle(res.data), limitNum);
                window.clearInterval(textTimer);
                taskList.html(renderTaskList(res));
            },
            error: function (error) {
                taskList.append('<div class="error-message">出错了 (>_<) </div>');
            }
        });
    }

    function renderTaskList(res) {

        for (var i = 0, len = res.data.length; i < len; i++) {
            res.data[i].assignee = res.data[i].assignee.split(',');
            res.data[i].assignee_avatars = res.data[i].assignee_avatars.split(',');

            res.data[i].members = [];

            for (var n = 0, length = res.data[i].assignee.length; n < length; n++) {
                res.data[i].members[n] = {
                    'name': res.data[i].assignee[n],
                    'avatar': res.data[i].assignee_avatars[n],
                };
            }
        }

        return (taskTpl({
            num: limitNum,
            total: res.total,
            finished: res.size,
            tasks: res.data
        }));
    }
});