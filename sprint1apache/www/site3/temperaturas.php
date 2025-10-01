<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 5</title>
</head>
<body>
    <h1>Ejercicio 5</h1>
    <h2>Conversor temperatura</h2>

    <p>Nueva conversión:</p>
    <form action="/temperaturas.php" method="post">
        <label for="temperatura_input">Temperatura:</label><br>
        <input type="text" id="temperatura_input" name="ftemperatura"><br>

        <input type="radio" id="celsius_input" name="ftipo" value="celsius">
        <label for="celsius_input">Celsius</label><br>

        <input type="radio" id="fah_input" name="ftipo" value="fahrenheit">
        <label for="fah_input">Fahrenheit</label><br>

        <input type="submit" value="Convertir">
        <br><br>
    </form>

    <h3>Resultado:</h3>
    <?php
        if(isset($_POST["ftipo"])){
            if($_POST["ftipo"] == "celsius"){
                $v_celsius = $_POST["ftemperatura"];
                // (0 °C × 9 / 5) + 32
                $v_fah = ($v_celsius * 9 / 5) + 32;
                echo $v_celsius."ºC = ".$v_fah."ºF";
            }else if($_POST["ftipo"] == "fahrenheit"){
                $v_fah = $_POST["ftemperatura"];
                // (32 °F − 32) × 5 / 9
                $v_celsius = ($v_fah - 32) * 5 / 9;
                echo $v_fah."ºF = ".$v_celsius."ºC";
            }
        }else{
            echo "Indica de qué tipo es la temperatura.";
        }
        $cantidad;

    ?>

</body>
</html>