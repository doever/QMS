function UserManage() {

}

UserManage.prototype.run = function () {
  var self = this;
  self.listenUserAdd();
  self.listenUserEdit();
  self.listenDelete();
};


UserManage.prototype.listenUserAdd = function(){
  var self = this;
  var userAddBtn = $('#user-add-btn');
  userAddBtn.click(function () {
      layer.open({
          type:2,
          title:'新增用户',
          skin:'layui-layer-rim',
          area: ['600px', '450px'], //宽高
          btn: ['确定', '取消'],
          content: "../../templates/user_add.html",
          yes:function (index,layero) {
              var body = layer.getChildFrame('body',index);//建立父子联系
              var forms = body.find('form');
              csrfajax.post({
                  'url':'/account/user/',
                  'data':forms.serialize(),
                  'success':function (result) {
                      if(result['code']===200){
                          layer.close(index);
                          layer.msg('success',{icon:1,time:1000});
                          window.location.reload();
                      }else{
                          console.log(result['message']);
                          layer.msg('error:'+result['message'],{icon:2,time:1000});
                      }
                   },
                  'error':function (error) {
                      layer.msg("服务器内部错误",{icon:2,time:1000});
                  }
              })
          },
           btn2:function (index, layero) {
                layer.close(index);
            }
      })
  });

};

//用户修改逻辑
UserManage.prototype.listenUserEdit = function(){
    var editBtn = $(".user-edit");
    editBtn.on('click',function () {
        var currentBtn = $(this);
        var userId = currentBtn.parent().parent().attr('data-pk');
        layer.open({
            type:2,
            title:'用户编辑',
            skin:'layui-layer-rim',
            area: ['600px', '450px'], //宽高
            btn: ['确定', '取消'],
            content: "/account/user_edit/"+userId,
            yes:function (index,layero) {
              var body = layer.getChildFrame('body',index);//建立父子联系
              var forms = body.find('form');
              csrfajax.put({
                  'url':'/account/user/',
                  'data':forms.serialize(),
                  'success':function (result) {
                      if(result['code']===200){
                      layer.close(index);
                      layer.msg('ok',{icon:1,time:1000});
                      window.location.reload();
                      }else{
                          layer.msg('error:'+result['message'],{icon:2,time:1000});
                      }
                   }
              })
          },
           btn2:function (index, layero) {
                layer.close(index);
            }
        })
    })
};


UserManage.prototype.listenDelete = function(){
    var userDeleteBtn =  $(".user-delete");
    userDeleteBtn.on('click',function () {
        var currentBtn = $(this);
        var userId = currentBtn.parent().parent().attr('data-pk');
        var userName = currentBtn.parent().siblings().eq(0).text();
        layer.confirm('禁用用户'+userName+'?',function (index) {
            csrfajax.delete({
                'url':'/account/user/',
                'data':{'user_id':userId},
                'success':function (result) {
                    if(result['code']===200){
                        layer.msg('ok',{icon:1,time:1000});
                        layer.closeAll();
                        window.location.reload();
                    }else{
                        layer.msg(result['message'],{icon:2,time:1000});
                        layer.closeAll();
                    }
                }
            })
        })
    })
};

$(function () {
    var userManage = new UserManage();
    userManage.run();
});