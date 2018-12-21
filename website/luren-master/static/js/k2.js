

dic = {
    url:"/show/",
    type:"get",
    data:"a_id=" + Number($("#a_id").val()) ,
    success:function(res){
        alert("???")
        $("#main-body").html(res)

    }
}


$(function(){
    $.ajax(dic)
})