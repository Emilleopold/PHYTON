<html>
<head>
<?php
// error_reporting(E_ALL);
// ini_set('display_errors', 'On');
// ini_set('error_log','/var/log/phperror1.log');

if (isset($_POST['PUNDT']) AND !empty($_POST['PUNDT'])) {
 if ($_POST['PUNDT'] == "Rund") { shell_exec("./rundfahrt.py"); }
 if ($_POST['PUNDT'] == "Eing") { shell_exec("./eingang.py"); }
 if ($_POST['PUNDT'] == "Links") { shell_exec("./links.py"); }
 if ($_POST['PUNDT'] == "Rechts") { shell_exec("./rechts.py"); }
 if ($_POST['PUNDT'] == "Oben") { shell_exec("./oben.py"); }
 if ($_POST['PUNDT'] == "Unten") { shell_exec("./unten.py"); }
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
      <th style="text-align: center;">EINGANG</th>
      <th style="text-align: center;">LINKS</th>
      <th style="text-align: center;">RECHTS</th>
      <th style="text-align: center;">OBEN</th>
      <th style="text-align: center;">UNTEN</th>
    </tr>
    <tr>
      <td style="text-align: center;"><button type="submit" name="PUNDT" value="Rund">Rundfahrt</button></td>
      <td style="text-align: center;"><button type="submit" name="PUNDT" value="Eing">Eingang</button></td>
      <td style="text-align: center;"><button type="submit" name="PUNDT" value="Links">Links</button></td>
      <td style="text-align: center;"><button type="submit" name="PUNDT" value="Rechts">Rechts</button></td>
      <td style="text-align: center;"><button type="submit" name="PUNDT" value="Oben">Oben</button></td>
      <td style="text-align: center;"><button type="submit" name="PUNDT" value="Unten">Unten</button></td>
    </tr>
  </table>
</form>
   <iframe src="http://192.168.20.231:8081/?action=stream" height="800" width="800" frameborder="0"></iframe>
</body>
</html> 
