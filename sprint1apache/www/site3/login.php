<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 7</title>
</head>
<body>
    <h1>Ejercicio 7</h1>
    <h2>Iniciar sesión</h2>

    <form action="/login.php" method="post">
        <label for="user_input">Usuario:</label><br>
        <input type="text" id="user_input" name="usuario">
        <br><br>
        
        <label for="pass_input">Contraseña:</label><br>
        <input type="password" id="pass_input" name="contrasena">
        <br><br>
        
        <input type="submit" value="Login">
        <br><br>
    </form>

    <?php
        if(empty($_POST["usuario"])){
            echo "Te falta introducir el usuario.";
        }else if (empty($_POST["contrasena"])){
            echo "Te falta introducir la contraseña.";
        }else{
            $v_usuario = $_POST["usuario"];
            $v_contrasena = $_POST["contrasena"];
            $check;

            $usuarioOK = $v_usuario == "admin";
            $contrasenaOK = $v_contrasena == "1234";

            if($usuarioOK && $contrasenaOK){
                $check = "Acceso concedido.";
            }else{
                $check = "Acceso denegado.";
            }
            
            echo $check;

        }

    ?>

</body>
</html>