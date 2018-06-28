//处理登录请求
function Signin() {
    this.submitBtn = $(".login-btn input[type=button]");
}

Signin.prototype.run = function () {
    var self = this;
    self.listenSignIn();
};

Signin.prototype.listenSignIn = function () {
    var self = this;
    self.submitBtn.click(function () {
        var username = $("input[name='username']").val();
        var password = $("input[name='password']").val();
        var remember = $("input:checkbox:checked").val();
        console.log(username, password, remember);
        if(!username){
            layer.tips('请输入用户名',"input[name=username]");
        }else if(!password){
            layer.tips('请输入密码',"input[name=password]");
        }else{
        myajax.post({
            'url': '/account/signin/',
            'data': {
                'username': username,
                'password': password,
                'remember': remember
            },
            'success': function (result) {
                console.log(result['code']);
                if (result['code'] == 200) {
                    console.log(result);
                    window.location.assign('http://127.0.0.1:8000');
                } else {
                    var messageObj = result['message'];
                    if (typeof messageObj == 'string') {
                        layer.msg(messageObj);
                    } else {
                        var messages = [];
                        $.each(messageObj, function (k, v) {
                            messages.push(v[0]);
                        });
                        layer.msg(messages[0]);
                    }
                }
            },
            'error': function (error) {
                console.log(error);
            }

        })
      }
    })
};


function Signup() {

}

$(function () {
    var signobj = new Signin();
    signobj.run();
});