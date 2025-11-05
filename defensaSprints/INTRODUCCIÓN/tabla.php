<html>
  <body>
    <h1>Tabla del 7</h1>
    <table border="1">
      <tr><th>Expresión</th><th>Resultado</th></tr>
      <?php
      /*Cambia el for por un while*/
        $res = 0;
        $i = 1;
        while($res < 70){
          $res = 7 * $i;
          echo "<tr>";
          echo "<td>7 x " . $i . "</td>";
          echo "<td>" . $res . "</td>";
          echo "</tr>";
          $i++;
        }

      ?>
    </table>
  </body>
</html>