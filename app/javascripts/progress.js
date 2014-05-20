/*global $, _*/

/* 
* @Author: hanjiyun
* @Date:   2014-05-20 13:09:33
* @Last Modified by:   hanjiyun
* @Last Modified time: 2014-05-20 18:36:32
*/


$(function () {

    var num = 5;
    var taskTpl = _.template($('#task-list-tpl').html());
    var taskList = $('#progress-cont');

    getNewData();

    function getNewData() {
        $.ajax({
            type: 'GET',
            dataType: 'json',
            url: 'http://192.168.108.178:9000/tasks/',
            success: function (res) {
                // console.log(res);
                if (res.data.length <=  num) {
                    // console.log('小于或等于5');
                    res.size = res.data.length;
                    taskList.html(initTaskList(res));
                } else {
                    // console.log('大于5');
                    var size = res.data.length;
                    res.data = _.last(res.data, 5);
                    res.size = size;
                    // console.log('res.data', res);
                    taskList.html(initTaskList(res));
                }


                // setTimeout(function () {
                //     getNewData();
                // }, 5000);
            },
            error: function (error) {
                taskList.append('<div class="error-message">出错了 (>_<) </div>');
            }
        });
    }

    function initTaskList(res) {

        for (var i = 0, len = res.data.length; i < len; i++) {
            res.data[i].assignee = res.data[i].assignee.split(',');
            res.data[i].assignee_avatars = res.data[i].assignee_avatars.split(',');

            res.data[i].members = [];

            for (var n = 0, length = res.data[i].assignee.length; n < length; n++) {
                res.data[i].members[n] = {
                    'name' : res.data[i].assignee[n],
                    'avatar' : res.data[i].assignee_avatars[n],
                };
            }
        }

        // console.log('new res', res);

        return (taskTpl({num: num, total: res.total, finished: res.size, tasks: res.data}));
    }
});