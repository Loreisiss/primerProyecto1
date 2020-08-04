const Cuadro_Principal = document.querySelector("#Cuadro_Principal")
const boton_login = document.querySelector("#login_boton")
const boton_registro = document.querySelector("#registro_boton")
const div_login = document.querySelector("#login")
const div_select_registro = document.querySelector("#seleccionar_registro")
const div_registro_estudiante = document.querySelector("#registro_estudiante")
const div_registro_profesor = document.querySelector("#registro_profesor")
const reg_prof = document.querySelector("#reg_prof")
const reg_est = document.querySelector("#reg_est")

    

boton_registro.onclick=function(){

        div_login.style.display="none";
        div_registro_estudiante.style.display = "none";
        div_registro_profesor.style.display = "none";
        div_select_registro.style.display ="block";
        Cuadro_Principal.style.height = "30vh";
}

reg_prof.onclick=function(){
        div_select_registro.style.display = "none";
        div_registro_profesor.style.display="block";
        Cuadro_Principal.style.height = "90vh"
}

reg_est.onclick=function(){
        div_select_registro.style.display = "none";
        div_registro_estudiante.style.display="block";
        Cuadro_Principal.style.height = "90vh"
}

boton_login.onclick = function(){
        div_select_registro.style.display = "none";
        div_registro_estudiante.style.display = "none";
        div_registro_profesor.style.display = "none";
        div_login.style.display = "block";
        Cuadro_Principal.style.height = "50vh";
}       