/**
 * Created by tarena on 18-9-13.
 */
/**
 * 功能：加载所有的图片以及对应的文章
 * */
function loadArticle(){
    $.get('/article_info/',function(data){
        var html="";
        //循环遍历data,得到图片以及对应的文章JSON
        $.each(data,function(i,obj){
            html+="<li class='index_arc_item'>";
            var typeObj = JSON.parse(obj.type);
              html+="<a href='#' class='pic'>";
                html+="<img class='lazyload' src='/"+typeObj.picture+"'>";
              html+="</a>";
                //将obj.arcticles转换成JSON数组
                var goodsArr = JSON.parse(obj.arcticles);
                $.each(goodsArr,function(i,arcticles){
                  //arcticles表示的是每一篇文章
                  //文章标题
                  html+="<h4 class='title'>";
                    html+="<a href='article_detail.html' id=''>";
                      html+= arcticles.fields.titile;
                    html+="</a>";
                  html+="</h4>";
                    //加载文章
                      html+="<div class='desc'>"+arcticles.fields.content+"</div>";
                      //加载作者，文章发表时间，阅读量，评论量
                    　html+="<div class='date_hits'>";
                        html+="<span>"+arcticles.fields.authors+"</span>";
                        html+="<span>"+arcticles.fields.datatime+"</span>";
                        html+="<span>";
                           html+="<a href='#' id='read_detail_acticle' onclick='readAll()'>阅读全文>></a>";
                           html+="<span>"+arcticles.fields.id+"</span>";
                    html+="</span>";
                    html+="<p class='hits'>";
                    html+="<i class='read_count' title='点击量'>阅读("+arcticles.fields.read_count+")</i>";
                    html+="</p>";
                    html+="<p class='commonts'>";
                    html+="<i class='cy_cmt_count' title='评论量'>评论("+arcticles.fields.coment_count+")</i>";
                    html+="</p>";
                      html+="</div>";
                });
            html+="</li>";
        });

        $(".index_arc").html(html);
    },'json');
}
//加载博主的个人信息
function loadAuthor() {
    $.get('/author_info/',function (data) {
        var html="";
        //获取作者的详细信息
            html+="<ul class='index_recd'>";
              html+="<li class='index_recd_item'>";
                html+="<img src="+obj.author_picture+">";
              html+="</li>";

              html+="<li class='index_recd_item'>";
                html+="<姓名："+obj.author_name;
              html+="</li>";

              html+="<li class='index_recd_item'>";
                html+="<职业："+obj.author_work;
              html+="</li>";

              html+="<li class='index_recd_item'>";
                html+="<邮箱："+obj.author_email;
              html+="</li>";

              html+="<li class='index_recd_item'>";
                html+="<定位:"+obj.author_address;
              html+="</li>";
            html+="</ul>";
        },'json');
}

//阅读全文的跳转
function readAll() {
    var article_id = this.next().html();
    $.get('/get_article/',article_id,function (data) {
        var article = JSON.parse(data);
        $(".index_arc").html(article['content']);
    },'json');
}

//热门推荐
$(function () {
    loadArticle();
    loadAuthor();
});

