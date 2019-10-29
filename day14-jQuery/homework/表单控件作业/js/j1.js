function add() {
    var name = $("#name").val();
    var hobby = $("#hobby").val();
    if (name == "") {
        alert('姓名不能为空！')
    } else {
        $('table:first').append('<tr><td><input type="checkbox"></td><td>' + name + '</td><td>' + hobby + '</td>');
        $('div').css("display", 'none');
        $("#name").val("");
        $("#hobby").val("");
    }
};
$('#add').click(
    function () {
        $('div').css("display", 'block')
    }
);
$('#btn').click(function () {
    add()
});
$('#del').click(
    function () {
        if ($('input:checked').length < 1) {
            alert('请先选择！！')
        } else {
            $('input:checked').parent().parent().remove()
        }
    }
);
$('#change').click(
    function () {
        if ($('input:checked').length > 1) {
            alert('不支持批量修改！')
        } else if ($('input:checked').length < 1) {
            alert('请先选择！！')
        } else {
            var d_name = $('input:checked').parent().next().text();
            var d_hobby = $('input:checked').parent().next().next().text();
            $('#name').val(d_name);
            $('#hobby').val(d_hobby);
            $('input:checked').parent().parent().remove();
            $('div').css("display", 'block');
        }
    }
);
// 点击全选按钮 选中所有的checkbox
// DOM绑定事件方法
// $("#all")[0].onclick = function(){}
// jQuery绑定事件方法
$("#all").click(function () {
    $(":checkbox").prop('checked', true);
});
// 取消
$("#cancel").on("click", function () {
    $(":checkbox").prop('checked', false);
});
// 反选
$("#reverse").click(function () {
    // 1. 找到所有选中的checkbox取消选中
    // $("input:checked").prop('checked', false);
    // // 2. 找到没有选中的checkbox选中
    // $("input:not(:checked)").prop('checked', true);
    //你会发现上面这么写，不行，为什么呢？因为你做了第一步操作之后，再做第二步操作的时候，所有标签就已经全部取消选中了，所以第二步就把所有标签选中了

    // 方法1. for循环所有的checkbox,挨个判断原来选中就取消选中，原来没选中就选中
    var $checkbox = $(":checkbox");
    for (var i = 0; i < $checkbox.length; i++) {
        // 获取原来的选中与否的状态
        var status = $($checkbox[i]).prop('checked');
        $($checkbox[i]).prop('checked', !status);
    }
    // 方法2. 先用变量把标签原来的状态保存下来
    //     var $unchecked =  $("input:not(:checked)");
    //     var $checked = $("input:checked");
    //
    //     $unchecked.prop('checked', true);
    //     $checked.prop('checked', false);
})
