<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 6</title>
</head>
<body>
    <h1>Ejercicio 6</h1>
    <h2>Calculadora básica</h2>

    <form action="/calc.php" method="post">
        <label for="num1_input">Primer número:</label><br>
        <input type="number" id="num1_input" name="numero1"><br>
        <br>

        <label for="operacion">Elige tipo de operación:</label><br>
        <select name="operacion" id="operacion">
            <option value="suma">Suma</option>
            <option value="resta">Resta</option>
            <option value="multi">Multiplicación</option>
            <option value="div">División</option>
        </select>

        <br><br>
        <label for="num2_input">Segundo número:</label><br>
        <input type="number" id="num2_input" name="numero2"><br>

        <br><br>
        <input type="submit" value="Calcular">
        <br><br>
    </form>

    <h3>Resultado:</h3>
    <?php
        //if(isset($_POST["numero1"]) && isset($_POST["numero2"])){
            
            $v_operacion = $_POST["operacion"];
            $resultado;
            $v_numero1 = $_POST["numero1"];
            $v_numero2 = $_POST["numero2"];

            switch($v_operacion){
                case "suma":
                    $resultado = $v_numero1 + $v_numero2;
                    break;
                case "resta": 
                    $resultado = $v_numero1 - $v_numero2;
                    break;
                case "multi": 
                    $resultado = $v_numero1 * $v_numero2;
                    break;
                case "div": 
                    $resultado = $v_numero1 / $v_numero2;
            }
            
            echo $resultado;

        //}else{
        //    echo "Te falta introducir algún número.";
        //}

    ?>

</body>
</html>