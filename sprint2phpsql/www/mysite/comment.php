<!DOCTYPE html>

<?php
    $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
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
        $id = $_POST['cancion_id'];
        $comentario = $_POST['new_comment'];

        $query = "INSERT INTO tComentarios(comentario, cancion_id, usuario_id, fecha)
        VALUES ('".$comentario."',".$id.",NULL, CURRENT_DATE())";

        mysqli_query($db, $query) or die('Error');

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