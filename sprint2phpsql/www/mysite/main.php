<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Site</title>
</head>
<body>
    <?php
        error_reporting(E_ALL);
        ini_set('display_errors', 1);
        
        $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

    ?>
    <h1>Conexión establecida</h1>
    
</body>
</html>