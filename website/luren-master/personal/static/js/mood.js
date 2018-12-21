/**
 * Created by tarena on 18-9-13.
 */
function loadmood(){
    $.get('/mood_info/',function(data){
        var html="";
        //循环遍历data,得到图片以及对应的文章JSON
        $.each(data,function(i,obj){
            html+="<div class='cd-timeline-block'>";
            var typeObj = JSON.parse(obj.type);
              html+="<div class='cd-timeline-img cd-picture'>";
                html+="<img src='/"+typeObj.picture+"'>";
              html+="</div>";
                //将obj.arcticles转换成JSON数组
                var goodsArr = JSON.parse(obj.arcticles);
                $.each(goodsArr,function(i,arcticles){
                  //arcticles表示的是每一篇文章
                  //文章标题
                html+="<div class='cd-timeline-content'>";
                  html+="<h4 class='title'>";
                      html+= arcticles.fields.titile;
                  html+="</h4>";
                    //加载文章
                      html+="<p>"+arcticles.fields.content+"</p>";
                      html+="<a href='www.wfyvv.com' class='f-r'><input class='btn btn-success size-S' type='button' value='更多'></a>";
                      //加载作者，文章发表时间，阅读量，评论量
                      html+="<span>"+arcticles.fields.authors+"</span>";
                      html+="<span class='cd-date'>"+arcticles.fields.datatime+"</span>";
                html+="</div>";
               html+="</div>";
                });
            html+="</div>";
        });

        $(".index_arc").html(html);
    },'json');
}

$(function () {
    loadmood()
});