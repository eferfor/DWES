<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 3</title>
</head>
<body>
    <h1>Ejercicio 3</h1>
    <?php
        // Peso / (altura * altura)
        function calcular_imc($peso, $altura){
            return $peso / ($altura * $altura);
        }

        $imc = calcular_imc($_GET["peso"], $_GET["altura"]);

        echo "<h3>Resultado:</h3>";
        echo "<p>IMC = ".$imc."</p>";

        if($imc < 18.5){
            echo "Bajo peso";
        }else if($imc <= 24.9){
            echo "Normal";
        }else{
            echo "Sobrepeso";
        }
    ?>
</body>
</html>