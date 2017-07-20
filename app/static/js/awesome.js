////////////////////////////this is the section of the modal implementation ////////////////////


var modal_init = function() {

    var modalWrapper = document.getElementById("modal_wrapper");
    var modalWindow  = document.getElementById("modal_window");

    var openModal = function(e)
    {
      modalWrapper.className = "overlay";
      var overflow = modalWindow.offsetHeight - document.documentElement.clientHeight;
      if(overflow > 0) {
        modalWindow.style.maxHeight = (parseInt(window.getComputedStyle(modalWindow).height) - overflow) + "px";
      }
      modalWindow.style.marginTop = (-modalWindow.offsetHeight)/2 + "px";
      modalWindow.style.marginLeft = (-modalWindow.offsetWidth)/2 + "px";
      e.preventDefault ? e.preventDefault() : e.returnValue = false;
    };

    var closeModal = function(e)
    {
      modalWrapper.className = "";
      e.preventDefault ? e.preventDefault() : e.returnValue = false;
    };

    var clickHandler = function(e) {
      if(!e.target) e.target = e.srcElement;
      if(e.target.tagName == "DIV") {
        if(e.target.id != "modal_window") closeModal(e);
      }
    };

    var keyHandler = function(e) {
      if(e.keyCode == 27) closeModal(e);
    };

    if(document.addEventListener) {
      document.getElementById("modal_open").addEventListener("click", openModal, false);
      document.getElementById("modal_close").addEventListener("click", closeModal, false);
      document.addEventListener("click", clickHandler, false);
      document.addEventListener("keydown", keyHandler, false);
    } else {
      document.getElementById("modal_open").attachEvent("onclick", openModal);
      document.getElementById("modal_close").attachEvent("onclick", closeModal);
      document.attachEvent("onclick", clickHandler);
      document.attachEvent("onkeydown", keyHandler);
    }
};
  
if(document.addEventListener) {
       document.addEventListener("DOMContentLoaded", modal_init, false);
  } else {
     
       window.attachEvent("onload", modal_init);
  }



////////////////////////////////////////////////////



var TextType = function(el,toRotate, period){
    this.toRotate = toRotate;
    this.el = el;
    this.loopNum = 0;
    this.period = parseInt(period,10) || 2000;
    this.txt = '';
    this.tick();
    this.isDeleting = false;

};

TextType.prototype.tick = function(){
    var i = this.loopNum % this.toRotate.length;
    var fullTxt = this.toRotate[i];
    if(this.isDeleting){
        this.txt = fullTxt.substring(0, this.txt.length-1);
    }else{
        this.txt = fullTxt.substring(0,this.txt.length+1)
    }

    this.el.innerHTML = '<span class="wrap">'+this.txt +'</span>';

    var that = this;
    var delta = 100 - Math.random() * 100;

    if(this.isDeleting){
        delta /= 2;
    }
    if(!this.isDeleting && this.txt === fullTxt){
        delta = this.period;
        this.isDeleting = true;
    }else if(this.isDeleting && this.txt === ''){
        this.isDeleting = false;
        this.loopNum ++;
        delta = 500;
    }

    setTimeout(function(){
        that.tick();
    },delta);
};


window.onload = function(){
    var elements = document.getElementsByClassName('typewrite');
    for(var i=0; i<elements.length; i++){
        var toRotate = elements[i].getAttribute('data-type');
        var period = elements[i].getAttribute('data-period');

        if(toRotate){
            new TextType(elements[i], JSON.parse(toRotate),period);
        }
    }

    var css = document.createElement("style");
    css.type= "text/css";
    css.innerHTML = ".typewrite > .wrap { border-right: 0.08em solid #fff}";
    document.body.appendChild(css);
 
};

function findparameters(parameters){
        var result = null;
        tmp=[];
        window.location.search.substr(1)
        .split("&")
        .forEach(function(item){
            tmp = item.split("=");
            if(tmp[0] === parameters)result = decodeURIComponent(tmp[1]);
        });
       return result;
               
    }

try{
    var cat = findparameters('category')
    var mystring = findparameters("description").split("+").join(" ");
    
    var bucketList = new Object();
    bucketList[findparameters("category")]= mystring;
    console.log(bucketList);
    
    document.getElementById("kamjesh").innerHTML= mystring;
    
    console.log(document.getElementById("kamjeshImage"));
    
    document.getElementById("kamjeshImage").setAttribute("class" ,"media-object thumbnail"); 
    document.getElementById("kamjeshImage").setAttribute("src" ,"images/"+cat +".jpg");
    
    
}catch (err){
    console.log(err);
    
    }













