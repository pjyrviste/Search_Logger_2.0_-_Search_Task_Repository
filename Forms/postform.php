<?php
function getQuestionText($question, $answer)
{
	$text="";
	if($question == 1) 
	{
		switch($answer) {
			case 2:
				$text="Yes, entirely!";
				break;
			case 1:
				$text="Yes, but not everything.";
				break;
			case 0:
				$text="No, not at all.";
				break;
		}
		if ($text != "") 
		{
			return $text;
		} else {
			return "No such answer!";
		}
	} 
	elseif($question == 2) 
	{
		switch($answer) {
			case 1:
				$text="Very easy";
				break;
			case 2:
				$text="Easy";
				break;
			case 3:
				$text="Moderate";
				break;
			case 4:
				$text="Difficult";
				break;
			case 5:
				$text="Very difficult";
				break;
		}
		if ($text != "") 
		{
			return $text;
		} else {
			return "No such answer!";
		}
	}
	elseif($question = 3) 
	{
		switch($answer) {
			case 2:
				$text="Yes, a lot!";
				break;
			case 1:
				$text="Not much but I made some modifications.";
				break;
			case 0:
				$text="No, not at all.";
				break;
		}
		if ($text != "") 
		{
			return $text;
		} else {
			return "No such answer!";
		}
	}
	else 
	{
		return "No such question!";
	}
				 
}
?>

<html>
<body>
<h2>Thank you!</h2>
<br /><br />
<strong>Success:</strong>
<?php echo $_POST["success"] . " - " . getQuestionText(1,$_POST["success"]);
?>
<br />
<strong>Difficulty:</strong>
<?php echo $_POST["difficulty"] . " - " . getQuestionText(2,$_POST["difficulty"]);
?>
<br />
<strong>Change:</strong>
<?php echo $_POST["change"] . " - " . getQuestionText(3,$_POST["change"]);
?>
<br />

</body>
</html>
