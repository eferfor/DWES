document.addEventListener("DOMContentLoaded", function(){
    const formulario = document.getElementById("newpasswordform");
    const mensajeError = document.getElementById("messageError");

    formulario.addEventListener("submit", function(evento){
        evento.preventDefault();

        let claveVieja = document.getElementById('oldPass').value;
        let claveNueva1 = document.getElementById('newPass1').value;
        let claveNueva2 = document.getElementById('newPass2').value;

        // Validación de los campos
        if(claveVieja === '' || claveNueva1 === '' || claveNueva2 === ''){
            mensajeError.innerText = 'Debes cubrir todos los campos.';
            return;
        }else if(claveNueva1 !== claveNueva2){
            mensajeError.innerText = 'Los campos de contraseña nueva no coinciden.'
        }else if(claveVieja === claveNueva1){
                mensajeError.innerText = 'La contraseña nueva debe ser distinta a la anterior.';
        }else{
            // Si todo correcto
            mensajeError.innerText = '';
            formulario.submit();
        }
    });

});