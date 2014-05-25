/*global $, _*/

/*
 * @Author: hanjiyun
 * @Date:   2014-05-20 13:09:33
 * @Last Modified by:   hanjiyun
 * @Last Modified time: 2014-05-25 14:57:05
 */


$(function () {

    var limitNum = 5;
    var dataSize;
    var apiURL = 'http://192.168.100.47:4000/tasks/';
    var taskTpl = _.template($('#task-list-tpl').html());
    var taskList = $('#progress-cont');
    var noData = $('#no-data');

    getNewData();

    if (dataSize > 0) {
        setInterval(getNewData, 5000);
    }

    function getNewData() {
        $.ajax({
            type: 'GET',
            dataType: 'json',
            url: apiURL,
            success: function (res) {
                dataSize = res.size = res.data.length;
                res.data = _.last(_.shuffle(res.data), limitNum);
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