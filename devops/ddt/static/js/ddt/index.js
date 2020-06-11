function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function logout() {
    $.ajax({
        url: "/api/v1.0/sessions",
        type: "delete",
        headers: {
            "X-CSRFToken": getCookie("csrf_token")
        },
        dataType: "json",
        success: function (resp) {
            if ("0" == resp.errno) {
                location.href = "/login.html";
            }
        }
    });
}

$(document).ready(function(){
    // 检查用户的登录状态
    $.get("/api/v1.0/sessions", function(resp) {
        if ("0" == resp.errno) {
            $(".user-info").html(resp.data.username);
            // $(".top-bar>.user-info").show();
        } else {
            console.log("ss");
            location.href = "/login.html";
        }
    }, "json");
})


