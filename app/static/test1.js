$(document).ready(function(){
    


    var tiempo_inicio = Date.now();

    const siguiente = document.querySelector("#siguiente");
    const anterior = document.querySelector("#anterior");
    const img1 = document.querySelector("#img1");
    const img2 = document.querySelector("#img2");
    const img3 = document.querySelector("#img3");
    const img5 = document.querySelector("#img5");
    const verde = document.querySelector("#verde");
    const azul = document.querySelector("#azul");
    const rojo = document.querySelector("#rojo");
    const amarillo = document.querySelector("#amarillo");
    const opciones = document.getElementsByClassName("opcion");
    const img4 = document.querySelector("#img4");
    const mensaje_ = document.querySelector("#mensaje");
            
    var puntos = 0
         
    const arreglo=[azul, verde, rojo,amarillo];
    const arreglo2=[img1,img2,img3,img5];
    const respuestas=['B','C','C',"A"]
    var preguntas_respondidas = []
    const tamanios=["400px", "600px", "600px","600px"]
    var contenido = []
    var indice = 0;
          
    var nivel = document.querySelector("#nivel");
    
    
    
    function desaparecer(a,b,c){
                a.style.width = c;
                
                b.style.width = "0px";
    }
    
    function correccion(indice){
        var bool = false;
        for(var i=0; i<contenido.length; ++i)
    
            if(contenido[i][0] == indice){
                   
                mensaje_.innerText = contenido[i][1];
                img4.src = contenido[i][2];
                img4.style.visibility = "visible";
                bool = true;
                for(var j=0; j<opciones.length; ++j)
                    if(opciones[j].innerText == contenido[i][3])
                        opciones[j].style.color = "red"
                    else 
                        opciones[j].style.color = "gold"
                            
            }

            if(!bool){ 
                mensaje_.innerText = ""
                img4.style.visibility = "hidden";
                for(var j=0; j<opciones.length; ++j)  
                    opciones[j].style.color = "gold"
            }
    }

function getCookie(c_name) {
    if (document.cookie.length > 0){
        c_start = document.cookie.indexOf(c_name + "=");

        if (c_start != -1){
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}

            
           
anterior.onclick = function(){
                
    if(indice != 0){ 
        arreglo[indice].style.width = "0%";
        arreglo2[indice].style.opacity ="0";
        --indice;
                    
        correccion(indice);
    
        arreglo[indice].style.width = "100%";
        setTimeout(desaparecer,200,arreglo2[indice], arreglo2[indice+1], tamanios[indice])
        setTimeout(function(){arreglo2[indice].style.opacity = "1";}, 1200)
        nivel.innerText = indice+1;
        }
    }
    
function aparecer(a,b){
    a.style.width = b
    a.style.opacity = "1";
}
    
            
    
siguiente.onclick = function(){
                
    if(indice != 3){ 
        
        arreglo[indice].style.width = "0%";
        arreglo2[indice].style.opacity ="0";
        ++indice;
                     
        correccion(indice)
    
    
        arreglo[indice].style.width = "100%";
        setTimeout(aparecer,1300,arreglo2[indice],tamanios[indice])
        nivel.innerText = indice+1;
        }
                
}
    

function pregunta_no_respondida(a){
                
        for(var i =0; i<preguntas_respondidas.length; ++i)
            if(preguntas_respondidas[i] == a)  return false;
               
        return true;
}
    


var contador_preguntas_respondidas = 0;

for(var i=0; i<4; ++i)
    opciones[i].onclick = function(){
                    
    if(pregunta_no_respondida(indice)){

        ++contador_preguntas_respondidas;
        this.style.color = "red";
        var mensaje, icono;
        preguntas_respondidas.push(indice);
        img4.style.visibility ="visible";
        img4.style.width = "60px"

        if(this.innerText == respuestas[indice]) {                     
                            
            puntos+=5;
            document.getElementById("puntos").innerText=puntos;
            mensaje = "¡Su respuesta es correcta!"
            icono="/static/check.png"
        }
        else{
            mensaje = "Su respuesta es incorrecta, la respuesta correcta es la opción "+respuestas[indice];
            icono="/static/error.png"
        }
                        
            
        //Envio de datos modo Jquery
        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        });
   
        var URL = "/enviar_info/";
        var data = {'puntos': puntos};
        $.post(URL, data, function(response){
            /*if(response === 'success'){ alert('Yay!'); }
            else{ alert('Error! :('); }  */  })



            
        

        /*
        var formData = new FormData();
        formData.append("puntos", puntos)
        
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/enviar_info/", true);
        xhr.send(formData)
        */

        mensaje_.innerText=mensaje;
        img4.src = icono
        contenido.push([indice, mensaje,icono,this.innerText])

    }      
                    
                   

    if(contador_preguntas_respondidas == 4){
        alert("Examen finalizado")
        



        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        });

        var tiempo_total = ((Date.now()-tiempo_inicio)/60000).toFixed(2)
        var URL = "/enviar_info/";
        var data = {'tiempo':  tiempo_total  };

        $.post(URL, data, function(_response){
            /*if(response === 'success'){ alert('Yay!'); }
            else{ alert('Error! :('); }*/
        });

        
        
/*
        var formData = new FormData();
        var tiempo = ((Date.now()-tiempo_inicio)/60000).toFixed(2);
        formData.append("tiempo", tiempo)

        
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/enviar_info/", true);
        xhr.send(formData);*/
        

    }
}


})
