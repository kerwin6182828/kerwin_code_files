$(function () {

    // $("[name='portrait_show']").src('/media/portraits/');
    $('#submit_button').css('display','none');
    $('#portrait_form').css('display','none');
    $('#change_button').click(function () {
        change_userinfos();
    })
});

function userInfos_show() {

}

function change_userinfos() {
    $('#portrait_form').css('display','block');
    $('#submit_button').css('display','block');
    $('#change_button').css('display','none');
}