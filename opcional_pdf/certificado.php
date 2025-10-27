<?php
    error_reporting(E_ALL);
    ini_set('display_errors', 1);

    if(!isset($_GET['nombre']) || !isset($_GET['ape1']) || !isset($_GET['ape2'])){
            die('No se ha especificado un nombre completo nombre.');
        }


    require('/home/elena/Documentos/DWES/DWES/fpdf186/fpdf.php');

    class PDF extends FPDF{
        // Cabecera de página
        function Header(){
            global $title;

            $this->Image('./img/marco_a4.jpg', 0, 0, -300);

            // Times bold 32
            $this->SetFont('Times','B',32);
            // Ancho y posición del título.
            $w = $this->GetStringWidth($title)+6;
            $this->SetX((290-$w)/2);
            
            // Título
            $this->Cell($w,80,$title,0,0,'C');
            // Salto de línea
            $this->Ln(10);
        }

        function ChapterTitle($nombreCompleto){

            $this->AddFont('Parisienne', '', 'Parisienne-Regular.php');

            // Parisienne 42
            $this->SetFont('Parisienne','',42);
            $this->Cell(0,0, iconv("UTF-8", "ISO-8859-16", $nombreCompleto),0,0,'C');
            $this->Ln(4);
        }

        function ChapterBody(){
            // Times 20
            $this->SetFont('Times','',20);

            // Contenido
            $this->Cell(0,100,'Este certificado se otorga a', 0, 0, 'C');
            $this->Ln(80);

            $nombre = $_GET['nombre'];
            $ape1 = $_GET['ape1'];
            $ape2 = $_GET['ape2'];

            $this->ChapterTitle($nombre." ".$ape1." ".$ape2);

            // Times 20
            $this->SetFont('Times','',20);
            $this->Cell(0,40, 'En reconocimiento por haber completado el sprint 3', 0, 0, 'C');
            $this->Ln();

            // Firmas, Times bold 16
            $this->SetFont('Times','B',16);
            $this->Cell(150,40, 'Felipe VI', 0, 0, 'C');
            
            $this->Image('./img/sello.png', 122, 140, 50, 50);

            $this->SetFont('Times','B',16);
            $this->Cell(90,40, iconv("UTF-8", "ISO-8859-16", "Carlos Méndez"), 0, 0, 'C');

        }

        function Footer() {
            $this->SetY(-15);

            // Fecha, Times italic 8
            $fecha = "Fecha del diploma: " . date("j") . " de " . date("M") . " del " . date("Y");
            $this->SetFont('Times','I',8);
            $this->Cell(0,10,$fecha,0,0,'C');
        }

        function PrintChapter(){
            $this->AddPage();
            $this->ChapterBody();
            
        }
    }

    $pdf = new PDF('L');
    $title = 'Diploma de Desarrollo Web en Entorno Servidor';
    $pdf->SetTitle($title);
    $pdf->PrintChapter();
    $pdf->Output();
?>

<!-- http://localhost:8084/certificado.php?nombre=Elena&ape1=Fern%C3%A1ndez&ape2=Formoso -->