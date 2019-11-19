// 给删除按钮绑定事件,普通点击事件
// $('.del').click(function () {
//     // 删除当前行
//     $(this).parent().parent().remove()
// });

// 给删除按钮绑定事件,事件委托
$('table').on('click', '.del', function () {
    // 删除当前行
    $(this).parent().parent().remove()
});

// 给添加按钮绑定事件
$('#add').click(function () {
    // 添加表头数据
    $('.modal-title').text('添加员工信息');
    // 清空输入框
    $('#name, #age, #department').val('');
});

// 给修改按钮绑定点击事件,事件委托
$('tbody').on('click', '.edit', function () {
    // 1.弹出模态框
    $('#myModal').modal('show');
    // 2.添加表头数据
    $('.modal-title').text('修改员工信息');
    // 3.获取原数据信息
    var $currentTr = $(this).parent().parent();
    var name = $currentTr.children().eq(0).text();
    var age = $currentTr.children().eq(1).text();
    var department = $currentTr.children().eq(2).text();
    console.log(name, age, department);
    // 4.把获取到的数据填入模态框
    $('#name').val(name);
    $('#age').val(age);
    $('#department').val(department);
    // 5.给模态框中的提交按钮绑定一个data,给了一个键值对，键为key， 值为$currentTr
    $('#save').data('key', $currentTr);
});

// 给保存按钮绑定数据
$('#save').click(function () {
    // 1.获取用户输入的值
    var name = $('#name').val();
    var age = $('#age').val();
    var department = $('#department').val();
    console.log(name,age,department);
    // 2.判断是添加操作还是编辑操作，通过key获取值
    var $currentTr = $(this).data('key');
    // 3.判断有没有值，是编辑操作还是添加操作
    if($currentTr){
        // 如果有值，那就是编辑模式
        $currentTr.children().eq(0).text(name);
        $currentTr.children().eq(1).text(age);
        $currentTr.children().eq(2).text(department);
        // 清空保存按钮上面的data，那个键值对，key和$currentTr
        $('#save').removeData('key');
    }else{
        // 如果没有值，那就是添加模式
        // 创建一个tr标签，把数据塞进去
        var trEle = document.createElement('tr');
        $(trEle).append('<td>'+name+'</td>');
        $(trEle).append('<td>'+age+'</td>');
        $(trEle).append('<td>'+department+'</td>');
        $(trEle).append('<td>\n' +
            '<button type="button" class="btn btn-info btn-sm edit">编辑</button>\n' +
            '<button type="button" class="btn btn-danger btn-sm del">删除</button>\n' +
            '</td>');
        // 把上面的tr追加到表格的tbody后面
        $('tbody').append(trEle);
    }
    // 4.隐藏模态框
    $('#myModal').modal('hide');
});
