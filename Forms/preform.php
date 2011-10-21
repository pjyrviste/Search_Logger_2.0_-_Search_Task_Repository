<html>
<body>
<h2>Thank you!</h2>
<br /><br />
<strong>Search task description:</strong><br />
<?php echo $_POST["description"]; ?>
<br />
<strong>Tags:</strong><br />
<?php
$x=1;
while (isset($_POST['tag_' . $x])) 
{
	echo $_POST["tag_" . $x] . "<br />";
	$x++;
}
?>

</body>
</html>