function UserManage() {

}

UserManage.prototype.run = function () {
  var self = this;
  self.listenUserAdd();
};

UserManage.prototype.listenUserAdd = function(){
  var self = this;
  var userAddBtn = $('#user-add-btn');
  userAddBtn.click(function () {
      layer.open({
          type:2,
          title:'新增分类',
          skin:'layui-layer-rim',
          area: ['600px', '400px'], //宽高
          btn: ['确定', '取消'],
          content: "../../templates/user_add.html",
          yes:function (index,layero) {
              var body = layer.getChildFrame('body',index);//建立父子联系
             var forms = body.find('form');
             forms.submit();  //上传可以成功,但无法取回服务器的数据

              // csrfajax.post({
              //     'url':'/account/user/',
              //     'data':forms.serialize(),
              //     'enctype':"multipart/form-data",
              //     'success':function (result) {
              //         layer.close(index);
              //         layer.msg('ok',{icon:1,time:1000});
              //         window.location.reload();
              //      }
              // })
          },
           btn2:function (index, layero) {
                layer.close(index);
            }
      })
  });

};


$(function () {
    var userManage = new UserManage();
    userManage.run();
});