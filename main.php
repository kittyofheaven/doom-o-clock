<?php
// venv pyhon source ..\env\Scripts\python.exe
$output = shell_exec('..\env\Scripts\python.exe main.py');
// $outputtwo = shell_exec('.\env\Scripts\python.exe main.py 2>&1');
$outputtwo = shell_exec('..\env\Scripts\python.exe climate_data.py 2>&1');
echo "output one:".$output."<br>";
echo "output two:".$outputtwo;
?>