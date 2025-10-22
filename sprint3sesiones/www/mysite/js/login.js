document.addEventListener("DOMContentLoaded", function(){
    const formulario = document.getElementById("loginForm");
    const mensajeError = document.getElementById("messageError");

    formulario.addEventListener("submit", function(evento){
        evento.preventDefault();

        let usuario = document.getElementById('user').value;
        let clave = document.getElementById('pass').value;

        // Validación de los campos
        if(usuario.trim() === ''){
            mensajeError.innerText = 'El campo email no puede estar vacío.';
            return;
        }else if(clave === ''){
            mensajeError.innerText = 'Debes introducir una contraseña.';
            return;
        }else if(!validarEmail(usuario)){
            mensajeError.innerText = 'El formato del email no es válido.';
            return;
        }else{
            // Si todo correcto
            mensajeError.innerText = '';
            formulario.submit();
        }
    });

    function validarEmail(email){
        const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }

});