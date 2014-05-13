### Summary
Wandoulabs Polish Week dashboard which is located office front's Tv

### Screencast
![Road](./screencast/designv1-road.png)
![Tasks](./screencast/designv1-task.png)

### Data Layer

#### task相关：
主要的字段包括如下：

- taskName - string
- Assignee - list [(string) -> peopleName] 会通过此调用who.wandoulabs的数据取得头像
- Status - list[被提出，开始做，提交验证，验证通过]

使用包括：

- get /status=done 的所有task用来轮播
- done number / total number , 获得当前完成的状态
- 后台来导入polish week tasks 列表
- 后台来比较task is done


#### team相关：

- teamName - string which identifys the virtual team
- processStatus - 进度 在road上前进几步(共20步)

使用包括：

- 取得所有teamName list 并绘制到road上，并且realtime with it
- 在后台手动改变processStatus值

