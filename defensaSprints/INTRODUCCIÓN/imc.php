<html>
  <body>
    <h1>IMC</h1>
    <p>
    <?php
    /* Haz que el usuario pueda introducir su edad, peso y altura por GET*/
      function calcular_imc($peso, $altura) {
        return $peso / ($altura * $altura);
      }

      if (isset($_GET["peso"]) && isset($_GET["altura"]) && isset($_GET["edad"])) {
        $peso = $_GET["peso"];
        $altura = $_GET["altura"];
        $edad = $_GET['edad'];
        $imc = calcular_imc($peso, $altura);

        if ($imc < 18.5) {
          echo "IMC: " . $imc . " → Bajo peso";
        } else if ($imc < 25) {
          echo "IMC: " . $imc . " → Normal";
        } else {
          echo "IMC: " . $imc . " → Sobrepeso";
        }

        echo "<br>";
        echo "Edad: " . $edad . ".";
      } else {
        echo "Proporciona peso, altura y edad por GET.";
      }
    ?>
    </p>
  </body>
</html>