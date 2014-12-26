<html>
<head>
<?php
 // error_reporting(E_ALL);
 // ini_set('display_errors', 'On');
 // ini_set('error_log','/var/log/phperror1.log');

if (isset($_POST['PUNDT']) AND !empty($_POST['PUNDT'])) {
 if ($_POST['PUNDT'] == "Rund") { shell_exec("sudo /home/pi/pi-pan/rundfahrt.py"); }
 if ($_POST['PUNDT'] == "Lade") { shell_exec("sudo /home/pi/pi-pan/ladestation.py"); }
}

// echo 'Und jetzt der Fehler: ';
// echo gibtsnicht(); 

?>

<title></title>
</head>
<body>
<form method="post">
  <table style="width: 75%; text-align: left; margin-left: auto; margin-right: auto;" border="0" cellpadding="2" cellspacing="2">
    <tr>
      <th style="text-align: center;">RUNDFAHRT</th>
      <th style="text-align: center;">LADESTATION</th>
    </tr>
    <tr>
      <td style="text-align: center;"><button type="submit" name="PUNDT" value="Rund">Rundfahrt</button></td>
      <td style="text-align: center;"><button type="submit" name="PUNDT" value="Lade">Ladestation</button></td>
    </tr>
  </table>
</form>
   <iframe src="http://192.168.20.230:8081/?action=stream" height="800" width="800" frameborder="0"></iframe>
</body>
</html> 
