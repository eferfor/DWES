<!DOCTYPE html>

<?php
    $db = mysqli_connect('172.16.0.2', 'root', '1234', 'mysitedb') or die('Fail');
    error_reporting(E_ALL);
    ini_set('display_errors', 1);
?>

<html lang="es-ES">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>Comment</title>
</head>
<body>
    <?php
        session_start();
        $user_id_a_insertar = 'NULL';
        if(!empty($_SESSION['user_id'])){
            $user_id_a_insertar = $_SESSION['user_id'];
        }

        $id = $_POST['cancion_id'];
        $comentario = $_POST['new_comment'];

        $query = $db->prepare("INSERT INTO tComentarios(comentario, cancion_id, usuario_id, fecha)
        VALUES (?, ?, ?, CURRENT_DATE())");
        $query->bind_param("sii", $comentario, $id, $user_id_a_insertar);
        $query->execute();

        // mysqli_query($db, $query) or die('Error');

        echo '<div class="back">';
        echo '<p class="left"><a href="detail.php?cancion_id='.$id.'">Volver</a></p>';
        echo '</div>';

        echo '<p>Nuevo comentario ';
        echo mysqli_insert_id($db);
        echo ' añadido</p>';

        mysqli_close($db);
    ?>
</body>
</html>