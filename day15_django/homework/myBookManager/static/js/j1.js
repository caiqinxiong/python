function getTime() {
    var dt = new Date();
    var s1 = dt.getFullYear() + "-" + (dt.getMonth() + 1) + "-" + dt.getDate() + " " + dt.getHours() + ":" + dt.getMinutes() + ":" + dt.getSeconds() + "\t评论详情:";
    return s1
}

// 0 将ul标签添加到div#box标签中
var oUl = document.createElement('ul');
var oBox = document.getElementById('box');
oBox.appendChild(oUl);

var oBtn = document.getElementById('btn');
var oMsg = document.getElementById('msg');
// 控制留言的总数量
var count = 0;
oBtn.onclick = function () {


    // 点击留言按钮事件操作
    // 1.创建li标签
    var oLi = document.createElement('li');
    //2.设置内容
    if (oMsg.value == '') {
        alert('评论内容不能为空！')
    } else {
        oLi.innerHTML = getTime() + oMsg.value + "<span class='close'>删除</span>";
        // 3.如果想在插入的第一个li获取的前面继续添加li标签
        //3.1获取li标签
        var olis = document.getElementsByTagName('li');
        //3.2 如果是第一次添加的li标签，则直接添加到ul的后面
        if (olis.length == 0) {
            oUl.appendChild(oLi);
            count++;

        } else {
            // 3.3 如果不是第一次添加的li标签，则插入到第一个li标签的前面
            oUl.insertBefore(oLi, olis[0]);
            count++;
        }
        // 4.添加完成之后 清空textarea的值
        oMsg.value = '';


        // 5.点击X的时候删除当前的一条数据
        //5.1先获取所有的X
        var oSpans = document.getElementsByTagName('span');

        // 5.2for循环 对所有的X添加点击事件
        for (var i = 0; i < oSpans.length; i++) {
            oSpans[i].onclick = function () {
                // 5.3 移除当前的li标签
                oUl.removeChild(this.parentNode);
                count--;
            }
        }
    }

};

function sum() {
    alert('一共有' + count + '条评论！');

}

setInterval(f, 200);

function f() {
    var content = document.getElementById('content');
    var color = parseInt(Math.ceil(Math.random() * 16777216), 16);
    content.style.color = '#' + color
}