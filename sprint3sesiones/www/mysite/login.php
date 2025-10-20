<?php
    $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

    $email_posted = $_POST['f_email'];
    $password_posted = $_POST['f_password'];

    $query = $db->prepare("SELECT id, contraseña FROM tUsuarios WHERE email = ?");
    $query->bind_param("s", $email_posted);
    $query->execute();
    
    $result = $query->get_result();
    if(mysqli_num_rows($result) > 0){
        $only_row = $result->fetch_array();
        if(password_verify($password_posted, $only_row[1])) {
            session_start();
            $_SESSION['user_id'] = $only_row[0];
            $query->close();
            header('Location: main.php');
        }else{
            echo '<p>Contraseña incorrecta</p>';
        }
    }else{
        echo '<p>Usuario no encontrado con ese email</p>';
    }

?>