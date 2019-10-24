window.onload = function () {
    //需求：鼠标放到上面的li上，li本身变色(添加类)，对应的p也显示出来(添加类);
    //思路：1.点亮上面的盒子。   2.利用索引值显示下面的盒子。

    var tabli = document.getElementsByTagName('li');
    var tabContent = document.getElementsByTagName('table');
    for (var i = 0; i < tabli.length; i++) {
        // 绑定索引值（新增一个自定义属性：index属性）
        tabli[i].index = i;
        //鼠标移动到超链接时展示
        tabli[i].onmouseover = function () {
            // 1.点亮上面的盒子。   2.利用索引值显示下面的盒子。(排他思想)
            for (var j = 0; j < tabli.length; j++) {
                tabli[j].className = '';
                tabContent[j].className = '';
            }
            this.className = 'active';
            tabContent[this.index].className = 'active';//【重要代码】
        };

        //鼠标移出（包含下面的内容框）时取消
        tabContent[i].index = i;
        tabContent[i].onmouseout = function () {
            for (var j = 0; j < tabli.length; j++) {
                tabContent[j].className = '';
            }
            this.className = 'active';
            tabContent[this.index].className = '';//去除class格式
        }
    }
};