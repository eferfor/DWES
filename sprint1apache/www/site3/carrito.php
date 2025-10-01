<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 4</title>
</head>
<body>
    <h1>Ejercicio 4</h1>
    <table>
        <thead>
            <tr>
                <th>Producto</th>
                <th>Precio</th>
            </tr>
        </thead>
        <?php
            $total = 0;
            $lista = array(
                "Manzana" => 0.5,
                "Pan" => 1.2,
                "Huevos" => 2,
                "Galletas" => 2.85,
            );

            echo "<tbody>";
            foreach($lista as $item => $precio){

                $total += $precio;

                echo "<tr>";
                echo "<td>".$item."</td>";
                echo "<td>".$precio."</td>";
                echo "</tr>";
            }

            echo "</tbody>";
            echo "<tfoot>";
            echo "<tr>";
            echo "<td>TOTAL:</td>";
            echo "<td>".$total."</td>";
            echo "</tr>";
            echo "</tfoot>";


        ?>
    </table>
</body>
</html>