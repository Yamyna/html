<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST["email"];
    $message = $_POST["message"];
    $subject = "Contact from LightningMalware";

    if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $mailto_link = "mailto:lightningmalware@gmail.com?subject=$subject&body=$message";
        echo '<a href="' . $mailto_link . '">Contact Us</a>';
    } else {
        echo "Invalid email address. Please enter a valid email.";
    }
}
?>
