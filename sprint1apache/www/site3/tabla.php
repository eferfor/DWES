<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 2</title>
</head>
<body>
    <h1>Ejercicio 2</h1>
    <table>
        <?php
            for($i = 1; $i <= 10; $i++){
                $multi = $i * 7;

                echo "<tr>";
                echo "<td>7 x ".$i."</td>";
                echo "<td> = </td>";
                echo "<td>".$multi."</td>";
                echo "</tr>";
            }
        ?>
    </table>
</body>
</html>