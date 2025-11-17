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
        $db = mysqli_connect('172.16.0.2', 'root', '1234', 'mysitedb') or die('Fail');
    ?>

    <header>
        
        <?php
            session_start();
            $user_id_a_insertar = 'NULL';
            if(!empty($_SESSION['user_id'])){
                $user_id_a_insertar = $_SESSION['user_id'];

                $queryLog = $db->prepare('SELECT email FROM tUsuarios WHERE id = ?');
                $queryLog->bind_param("s", $user_id_a_insertar);
                $queryLog->execute();

                $resultLog = $queryLog->get_result() or die('Query error');
                $currentUser = $resultLog->fetch_array();
                $currentEmail = $currentUser[0];

                echo '<div class="login">';
                echo '<p>Sesión iniciada como: '.$currentEmail;
                echo '<span class="button"><a href="./newpassword.html">Cambiar contraseña</a></span></p>';
                echo '</div>';

                echo '<div class="logout">';
                echo '<div class="button"><a href="./logout.php">Cerrar sesión</a></div>';
                echo '</div>';
            }else{
                echo '<div class="button"><a href="./login.html">Iniciar sesión</a></div>';
            } 
        ?>
    
    </header>

    <h1 class="cabecera">Lista de canciones</h1>
    <?php
        $query = $db->prepare('SELECT * FROM tCanciones');
        $query->execute();

        $result = $query->get_result() or die('Query error');

        while($row = $result->fetch_array()){
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