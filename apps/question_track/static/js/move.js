function getStyle(obj,name){
    if(obj.currentStyle){
        return obj.currentStyle[name];
    }
    else{
        return getComputedStyle(obj,false)[name];
    }
}
function startMove(obj,json,fn){
    var bStop=true;
    clearInterval(obj.timer);
    obj.timer=setInterval(function(){
        // json={'width':200,'height':200};
        for(var i in json){
            if(i=='opacity'){
                var cur=Math.round(parseFloat(getStyle(obj,i))*100);
            }else{
                var cur=parseInt(getStyle(obj,i));
            }
            var speed=(json[i]-cur)/6;
            speed=speed>0?Math.ceil(speed):Math.floor(speed);
            if(cur!=json[i]){
                bStop=false;
                if(i=='opacity'){
                    obj.style.filter='alpha(opacity:'+(cur+speed)+')';
                    obj.style.opacity=(cur+speed)/100;
                }else{
                    obj.style[i]=speed+cur+'px';
                }
            }
        }
        if(bStop){
            clearInterval(obj.timer);
            if(fn){fn()}
        }
    },30)
}