<!DOCTYPE html>
<html lang="es-ES">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>My Site</title>
</head>
<body>
    <?php
        error_reporting(E_ALL);
        ini_set('display_errors', 1);
        $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
    ?>
    <h1 class="cabecera">Lista de canciones</h1>
    <?php
        $query = 'SELECT * FROM tCanciones';
        $result = mysqli_query($db, $query) or die('Query error');

        while($row = mysqli_fetch_array($result)){
            echo '<h1 class="titulo"><a href="detail.php?cancion_id='.$row[0].'">'.$row[1].'</a></h1>';
            echo '<a href="detail.php?cancion_id='.$row[0].'"><img src='.$row[2].' class="caratula"></a>';
            echo '<div class= "info">';
            echo '<div class= "info_grp">';
            echo '<p class="campo">Artista:</p>';
            echo '<p class="data">'.$row[3].'</p></div>';
            echo '<div class= "info_grp">';
            echo '<p class="campo">Álbum:</p>';
            echo '<p class="data">'.$row[4].'</p></div>';
            echo '<div class= "info_grp">';
            echo '<p class="campo">Año:</p>';
            echo '<p class="data">'.$row[5].'</p></div>';
            echo '</div>';
        }

        mysqli_close($db);
    ?>
    
</body>
</html>