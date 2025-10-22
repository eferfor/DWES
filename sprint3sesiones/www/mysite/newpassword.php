<?php
    error_reporting(E_ALL);
    ini_set('display_errors', 1);
    $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

    session_start();
        $user_id = 'NULL';
        if(!empty($_SESSION['user_id'])){
            $user_id = $_SESSION['user_id'];
        } 

    $current_pass_posted = $_POST['f_currentpass'];
    $newpassword1_posted = $_POST['f_newpassword1'];
    $newpassword2_posted = $_POST['f_newpassword2'];


    $query = $db->prepare("SELECT contraseña FROM tUsuarios WHERE id = ?");
        $query->bind_param("s", $user_id);
        $query->execute();

        $result = $query->get_result() or die('Query error');
        $user_row = $result->fetch_array();

        if(!password_verify($current_pass_posted, $user_row[0])){
            echo '<p>La contraseña actual introducida es incorrecta</p>';
        }else{
            $query_changepass = $db->prepare("UPDATE tUsuarios SET contraseña = ? WHERE id = ?");
            $query_changepass->bind_param("si", password_hash($newpassword1_posted, PASSWORD_DEFAULT), $user_id);
            $query_changepass->execute();
            echo '<p>Contraseña actualizada.</p>';
            mysqli_close($db);
            header("Location: main.php");
            exit();
        }
?>