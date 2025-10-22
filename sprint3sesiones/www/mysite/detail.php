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

    <div class="back">
        <p class="left"><a href="main.php">Volver</a></p>
    </div>

    <?php
        if(!isset($_GET['cancion_id'])){
            die('No se ha especificado una canción.');
        }

        $cancion_id = $_GET['cancion_id'];
        $query = $db->prepare('SELECT * FROM tCanciones WHERE id= ?');
        $query->bind_param("i", $cancion_id);
        $query->execute();
        $result = $query->get_result() or die('Query error');
        $only_row = $result->fetch_array();
        echo '<h1 class="titulo">'.$only_row['nombre'].'</h1>';
        echo '<img src="'.$only_row['url_imagen'].'" class="caratula">';
        echo '<div class="info">';
        echo '<p class="data">'.$only_row['artista'].'</p>';
        echo '<p class="titulo">'.$only_row['album'].'</p>';
        echo '<p class="data">'.$only_row['ano'].'</p>';
        echo '</div>';
    ?>
    
    <h2>Comentarios</h2>
    <div class="listaComentarios">
    <?php
        $query2 = $db->prepare('SELECT * FROM tComentarios WHERE cancion_id= ?');
        $query2->bind_param("i", $cancion_id);
        $query2->execute();
        $result2 = $query2->get_result() or die('Query error');

        while($row = $result2->fetch_array()){
            echo '<div class="userComment">';
            
            if($row['usuario_id'] != NULL){

                $user_id = $row['usuario_id'];
                $query3 = $db->prepare('SELECT * FROM tUsuarios WHERE id = ?');
                $query3->bind_param("i", $user_id);
                $query3->execute();
                $result3 = $query3->get_result() or die('Query error');
                $user_row = $result3->fetch_array();

                echo '<p class="left user">'.$user_row['nombre'].' '.$user_row['apellidos'].':</p>';
            }
            
            echo '<p class="left">'.$row['comentario'].' <span class="fecha">'.$row['fecha'].'</span></p>';
            echo '</div>';
        }

        mysqli_close($db);
    ?>
    </div>

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