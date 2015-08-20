$(function(){

    root = 'http://127.0.0.1:8000/bugsdjango/';

   $("input[name='btn-login']").click(checkLogin);

    $("input").keydown(function(){
        $(".message").html("");
    });
});

function checkLogin(){

    var frm = $("#form-login").serialize();

    $(".message").html("Checking...");
alert(root + 'is-valid-user');
    $.ajax({
        url: root + 'is-valid-user',
        type: 'post',
        data: frm,
        success: function(data){
alert(data);
            if(data.indexOf('invalid')>-1)
                $(".message").html('Invalid email or password');
            else
                ;//window.location.replace(root + 'user-section');
        }
    });
}