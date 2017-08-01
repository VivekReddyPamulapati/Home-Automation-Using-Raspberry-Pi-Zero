//Home Automation System
//Intruder Detection System
//Save this file as /var/www/html/index.php

<!DOCTYPE html>
<html>
<?php
$page = $_SERVER['PHP_SELF'];
$sec = "5";
?>
<head>
<meta http-equiv="refresh" content=<?php echo $sec;?> URL=<?php echo $page;?>>
<style>
        body
        {
            font-family: arial,verdana,sans-serif,Georgia, "Times New Roman", Times, serif;
            text-align:center;
            background:#cceeff;
        }
        h1
        {
            text-shadow: 5px 5px 5px #aaaaaa;
        }
</style>​
</head>
<body>
<img src= 'makerdemy.png'align="center" height="200" width="800">
<h1>INTRUDER DETECTION USING RASPBERRY PI ZERO</h1>
<?php
$username = "root";
$password = "12345678";
$database = 'intruder';
//Create connection
mysql_connect("localhost",$username,$password) or die ("Unable to connect");
@mysql_select_db($database) or die ("Could not select database");
$query = "SELECT * FROM PIR1";
$result=mysql_query($query);
$num=mysql_numrows($result);
mysql_close();?>
<table border=1 align=center>
<tr>	<th><font div style="color:red" face="Arial, Helvetica, sans-serif">Date</font></th>
	<th><font div style="color:red" face="Arial, Helvetica, sans-serif">Day</font></th>
	<th><font div style="color:red" face="Arial, Helvetica, sans-serif">Time</font></th>
	<th><font div style="color:Blue" face="Arial, Helvetica, sans-serif">Image of the Intruder</font></th>
</tr>
<?php
$i=0;
while ($i < $num)
{
$datetime=mysql_result($result,$i,"DateTime");
$date = date('jS F Y', strtotime($datetime));
$day = date('l', strtotime($datetime));
$time = date('H:i:s A', strtotime($datetime));
$image=mysql_result($result,$i,"Image");?>
<tr>
<td><font face="Arial, Helvetica, sans-serif"><?php echo $date; ?></font></td>
<td><font face="Arial, Helvetica, sans-serif"><?php echo $day; ?></font></td>
<td><font face="Arial, Helvetica, sans-serif"><?php echo $time; ?></font></td>
<td><font face="Arial, Helvetica, sans-serif"><?php echo '<a href="'.$image.'" target="_blank"><img src="'.$image.'" align=center height="100" width="150"></a>';?></font></td></tr>
<?php $i++;
}?>
</table>
</body>
</html>
