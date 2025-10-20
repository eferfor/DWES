<?php
    error_reporting(E_ALL);
    ini_set('display_errors', 1);
    $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

    $name_posted = $_POST['f_name'];
    $lastname_posted = $_POST['f_lastname'];
    $email_posted = $_POST['f_email'];
    $password1_posted = $_POST['f_password1'];
    $password2_posted = $_POST['f_password2'];

    if($name_posted === "" || $lastname_posted === "" || $email_posted === "" || $password1_posted === "" || $password2_posted === ""){
        echo '<p>Debes rellenar todos los campos</p>';
    }else if($password1_posted != $password2_posted){
        echo '<p>Las contraseñas no coinciden</p>';

    }else{
        $query_checkemail = $db->prepare("SELECT id FROM tUsuarios WHERE email = ?");
        $query_checkemail->bind_param("s", $email_posted);
        $query_checkemail->execute();

        $result = $query_checkemail->get_result();

        if(mysqli_num_rows($result) > 0){
            echo '<p>Ya existe un usuario con ese email</p>';
        }else{
            
            $query_createuser = "INSERT INTO tUsuarios (nombre, apellidos, email, contraseña) VALUES ('".$name_posted."', '".$lastname_posted."', '".$email_posted."', '".password_hash($password1_posted, PASSWORD_DEFAULT)."')";
            $result_newuser = mysqli_query($db, $query_createuser) or die('Query error');
            
            mysqli_close($db);
            header("Location: main.php");
            exit();
        }
    }

?>