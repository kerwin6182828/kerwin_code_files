/**
 * Created by tarena on 18-9-13.
 */
/**
 * 功能：加载所有的图片以及对应的文章
 * */
function loadArticle(){
    $.get('/personal/load_articles/',function(data){
        var html="";
        //循环遍历data,得到图片以及对应的文章JSON
        $.each(data,function(i,obj){
            var article = obj;
            html+="<li class='index_arc_item'>";
              html+="<a href='#' class='pic'>";
                html+="<img class='lazyload' src="+article.fields.a_cover+">";
              html+="</a>";
                //将obj.arcticles转换成JSON数组
                  //arcticles表示的是每一篇文章
                  //文章标题
                    html+="<h4 class='title'>";
                    html+="<span style='display: none'>"+article.pk+"</span>";
                    html+="<a href='article_detail.html' id=''>";
                    html+= article.fields.a_title;
                    html+="</a>";
                    html+="</h4>";
                    //加载文章
                    html+="<div class='desc'>"+article.fields.a_content+"</div>";
                      //加载作者，文章发表时间，阅读量，评论量
                    　html+="<div class='date_hits'>";
                        html+="<span>发表日期</span>";
                        html+="<span>"+article.fields.a_time+"</span>";
                        html+="<span>";
                           html+="<a href='#' id='read_detail_acticle' onclick='readAll()'>阅读全文>></a>";

                    html+="</span>";
                    html+="<p class='hits'>";
                    html+="<i class='read_count' title='点击量'>阅读("+article.fields.a_read_count+")</i>";
                    html+="</p>";
                    html+="<p class='commonts'>";
                    html+="<i class='cy_cmt_count' title='评论量'>评论("+article.fields.a_comment_count+")</i>";
                    html+="</p>";
                      html+="</div>";

            html+="</li>";
        });

        $(".index_arc").html(html);
    },'json');
}
//加载博主的个人信息
// function loadAuthor() {
//     $.get('/personal/',function (data) {
//         var html="";
//         //获取作者的详细信息
//             html+="<ul class='index_recd'>";
//               html+="<li class='index_recd_item'>";
//                 html+="<img src="+obj.author_picture+">";
//               html+="</li>";
//
//               html+="<li class='index_recd_item'>";
//                 html+="<姓名："+obj.author_name;
//               html+="</li>";
//
//               html+="<li class='index_recd_item'>";
//                 html+="<职业："+obj.author_work;
//               html+="</li>";
//
//               html+="<li class='index_recd_item'>";
//                 html+="<邮箱："+obj.author_email;
//               html+="</li>";
//
//               html+="<li class='index_recd_item'>";
//                 html+="<定位:"+obj.author_address;
//               html+="</li>";
//             html+="</ul>";
//         },'json');
// }
//
// //阅读全文的跳转
// function readAll() {
//     var article_id = this.next().html();
//     $.get('/get_article/',article_id,function (data) {
//         var article = JSON.parse(data);
//         $(".index_arc").html(article['content']);
//     },'json');
// }

//热门推荐

function load_about() {
    $.get('/personal/load_about/',function (data) {
        if(data.status == 1){
            $("[name='uid']").val(data.id);
            $("[name='uphone']").val(data.uphone);
            $("[name='utime']").val(data.time);
            $("[name='uname']").val(data.uname);
            $("[name='uemail']").val(data.uemail);
            $("[name='ugender']").val(data.ugender);
            $("[name='uage']").val(data.uage);
            $("[name='uaddress']").val(data.uaddress);
            $("[name='portrait_show']").attr('src',data.uportrait);
            $("[name='uprofire']").val(data.uprofire);
        }else{
            $("[name='uid']").val(data.id);
            $("[name='uphone']").remove();
            $("[name='utime']").val(data.time);
            $("[name='uname']").val(data.uname);
            $("[name='uemail']").remove();
            $("[name='ugender']").val(data.ugender);
            $("[name='uage']").val(data.uage);
            $("[name='uaddress']").remove();
            $("[name='portrait_show']").attr('src',data.uportrait);
            $("[name='uprofire']").val(data.uprofire);
            $('#change_button').remove();
            $('#submit_button').remove();
            if(data.isActive==0){
                $('#spec_infos').html('该用户已注销');
            }

        }
    },'json')
}

$('#change_button').click(function () {
    $('#portrait_form').css('display','block');
    $('#submit_button').css('display','block');
    $('#drop_button').css('display','block');
    $('#change_button').css('display','none');
    $('.changeable').css({'background':'white',
                            'font-size':'16px',});
    $('.changeable').removeAttr('readonly');
});

$('#drop_button').click(function () {
    $('#portrait_form').css('display','none');
    $('#submit_button').css('display','none');
    $('#drop_button').css('display','none');
    $('#change_button').css('display','block');
    $('.changeable').css({'background':'gainsboro',
                            'font-size':'16px',});
    $('.changeable').setAttr('readonly');
});


$(function () {
    $('#submit_button').css('display','none');
    $('#portrait_form').css('display','none');
    $('#drop_button').css('display','none');

    loadArticle();
    load_about();
    // loadAuthor();
    // $.post('/personal/index/',function (data) {
    //     $.each(data,function (i, obj) {
    //        console.log(obj)
    //     });
    // },'json')
});

