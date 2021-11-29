function get_time(){
    $.ajax({
        url: '/time',
        type: 'get',
        success: function(data){
            $('#tim').html(data)
        },error:function(){
            $('#tim').html('Fail to link server!')
        }
    })
}
function add2(){
    $.ajax({
        url:'/sum',
        data: {'d1':$('#i1').val(), 'd2':$('#i2').val(), 'd3':$('#i3').val()
        },success: function(data){
            $('#sum_res').eq(0).text('输入框数字之和为 '+data.d)
        }
    })
}
setInterval(get_time,5000)
// setInterval(get_c1,2000)