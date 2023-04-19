<?php
class pulpen
{
    var string $pilot;
    var string $Snowman;
    var string $faster;
    var string $balpoin;

    function panjang(string $balpoin)
    {
        echo "pulpen merek $balpoin" . PHP_EOL;
    }
    function pendek(string $balpoin)
    {
        echo "pulpen merek $balpoin" . PHP_EOL;
    }
}
class pensil
{
    function tajam(string $balpoin)
    {
        echo "pensil sangat tajam $balpoin" . PHP_EOL;
    }
    function __construct()
    {
        echo "ini adalah isi method construct" . PHP_EOL;
    }
}
$alat_menulis = new pulpen();
$alat_menulis->panjang("Snowman");
$alat_menulis->pendek("faster");



$alat_menggambar = new pensil();
$alat_menggambar->tajam("jika diruncingkan");