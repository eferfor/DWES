<!DOCTYPE html>
<html lang="es-ES">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>Detail</title>
</head>
<body>
    <?php
        error_reporting(E_ALL);
        ini_set('display_errors', 1);
        $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
    ?>
    
    <div class="back">
        <p class="left"><a href="main.php">Volver</a></p>
    </div>

    <?php
        if(!isset($_GET['cancion_id'])){
            die('No se ha especificado una canción.');
        }

        $cancion_id = $_GET['cancion_id'];
        $query = 'SELECT * FROM tCanciones WHERE id='.$cancion_id;
        $result = mysqli_query($db, $query) or die('Query error');
        $only_row = mysqli_fetch_array($result);
        echo '<h1 class="titulo">'.$only_row['nombre'].'</h1>';
        echo '<img src="'.$only_row['url_imagen'].'" class="caratula">';
        echo '<div class="info">';
        echo '<p class="data">'.$only_row['artista'].'</p>';
        echo '<p class="titulo">'.$only_row['album'].'</p>';
        echo '<p class="data">'.$only_row['ano'].'</p>';
        echo '</div>';
    ?>
    
    <h2>Comentarios</h2>
    <ul>
    <?php
        $query2 = 'SELECT * FROM tComentarios WHERE cancion_id='.$cancion_id;
        $result2 = mysqli_query($db, $query2) or die('Query error');

        while($row = mysqli_fetch_array($result2)){
            echo '<li>'.$row['comentario'].' <p class="fecha">'.$row['fecha'].'</p></li>';
        }

        mysqli_close($db);
    ?>
    </ul>

    <div class="formCom">
        <p>Deja un nuevo comentario:</p>
        <form action="/comment.php" method="post">
            <textarea class="left" rows="4" cols="40" name="new_comment"></textarea>
            <input type="hidden" name="cancion_id" value="<?php echo $cancion_id; ?>">
            <div><input class="button" type="submit" value="Comentar"></div>
        </form>
    </div>
    
</body>
</html>