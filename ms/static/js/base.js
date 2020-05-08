
    let coorA;
    let coorB;
    let btn = null;
    let lastMouseX;
    let lastMouseY;
  /*  function createDevice( x, y)
    {
        var b = document.createElement('button');
        b.id = "node"+4;
        b.className = "device";
        b.style.left = y;
        b.style.top = x;
        b.draggable=true;
        b.textContent="4";
        return b;
    }

    dev.appendChild(createDevice({{devices.node_x}}, {{devices.node_y}}));
*/
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
     var cookies = document.cookie.split(';');
     for (var i = 0; i < cookies.length; i++) {
           var cookie = jQuery.trim(cookies[i]);
           if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
           }
     }
    }
    return cookieValue;
    }

    function node_url()
        {
            if (event.target.className.indexOf("device") > -1) 
            {
                btn =event.target;
                document.location='node/' + btn.innerHTML;
            }
        }
    function click() 
    {
            if (event.target.className.indexOf("device") > -1) {
                btn = event.target;
                if(btn.style.top === "" || btn.style.left === "") {
                btn.style.position = "relative";
                btn.style.top = btn.offsetTop/4 + "px";
                btn.style.left = btn.offsetLeft/4 + "px";
                }
                coorA = btn.offsetTop;
                coorB = btn.offsetLeft;
            }
    }

        function dblclick() {
            btn = null;
        }

        function mousemove() {
            if (btn !== null) {
                btn.style.top = parseInt(btn.style.top) + (event.clientY - lastMouseY) + "px";
                btn.style.left = parseInt(btn.style.left) + (event.clientX - lastMouseX) + "px";
            }
            lastMouseX = event.clientX;
            lastMouseY = event.clientY;
        }
        

    function click_edit_button()
    {
        let s = document.getElementById("edit").innerHTML;
        if(s==="Сохранить")
        {
            change_c.style.display = 'none';
            not_edit_butt();
            document.getElementById("edit").innerHTML = "Вкл режим редактирования";
            let div = document.getElementById('dev');

            let elems = div.getElementsByTagName('*');
            for(let i=0; i<elems.length; i++)
            {
                let id =  elems[i].id;
                let _y =  String(elems[i].style.top);
                let _x =  String(elems[i].style.left);
                let node_x = parseInt(_x, 10);
                let node_y = parseInt(_y, 10);
                console.log("x" + node_x);
                console.log("y" + node_y);
                
                $.ajax({
                    url: '',
                    type: 'POST',
                    data: {'id': id,'node_x':node_x, 'node_y':node_y, csrfmiddlewaretoken: getCookie('csrftoken')},
                    error:function(){
                        console.log("Ошибка!");
                    },
                    success: function(data){
                        console.log(data.result);
                    return 0;
                    }
                 });

            }

            

        }
        if(s==="Вкл режим редактирования")
        {
            edit_butt();
            document.getElementById("edit").innerHTML = "Сохранить";
            change_c.style.display = "inline-block";

        }


    }


    function change_color()
    {
        let div = document.getElementById('dev');
        let color = Math.floor(Math.random()*16777215).toString(16);
        let elems = div.getElementsByTagName('*');
        for(let i=0; i<elems.length; i++)
        {
            elems[i].style.backgroundColor ="#" + color;
            elems[i].style.backgroundColor = Math.floor(Math.random()*16777215).toString(16);
           
        }

        
    }

    function not_edit_butt()
    {
        let div = document.getElementById('dev');
        
        let elems = div.getElementsByTagName('*');
        for(let i=0; i<elems.length; i++){

            
            //elems[i].style.backgroundColor = "red";
           // alert(elems[i].id)
            elems[i].addEventListener("click", node_url);
        
            elems[i].removeEventListener("click", click);
            elems[i].removeEventListener("mousemove", mousemove);
            elems[i].removeEventListener("dblclick", dblclick);

        }
         
        
       /* dev.onclick = function(event)
        {

            btn = event.target;
            btn.addEventListener("click", node_url);
        
            btn.removeEventListener("click", click);
            btn.removeEventListener("mousemove", mousemove);
            btn.removeEventListener("dblclick", dblclick);
        //document.getElementById("node").removeEventListener("onclick", onclick);
        }*/
        
    }



    function edit_butt()
    {
        let s = document.getElementById("edit").innerHTML;
        console.log(s);

        let div = document.getElementById('dev');

        let elems = div.getElementsByTagName('*');
        for(let i=0; i<elems.length; i++)
        {

            //alert(elems[i].id)
            elems[i].removeEventListener("click", node_url);
        
            elems[i].addEventListener("click", click);
            elems[i].addEventListener("mousemove", mousemove);
            elems[i].addEventListener("dblclick", dblclick);

        }
        

        /*dev.onclick = function(event)
        {
            btn = event.target;
            
            btn.removeEventListener("click", node_url);
            btn.addEventListener("click", click);
            btn.addEventListener("mousemove", mousemove);
            btn.addEventListener("dblclick", dblclick);
        }*/

        
    }
    //document.getElementById("edit").innerHTML ="Вкл режим редактирования";
