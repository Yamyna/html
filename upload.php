<?php
// upload.php

$target_dir = "uploads/"; // Répertoire où le fichier sera sauvegardé
if (!file_exists($target_dir)) {
    mkdir($target_dir, 0777, true);
}

$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$fileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));

// Ajoutez des messages de débogage
echo "Target file: " . $target_file . "<br>";
echo "File type: " . $fileType . "<br>";
echo "File size: " . $_FILES["fileToUpload"]["size"] . "<br>";

// Vérifie si le fichier est une image réelle ou un faux
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
        echo "File is an image - " . $check["mime"] . ".<br>";
        $uploadOk = 1;
    } else {
        echo "File is not an image.<br>";
        $uploadOk = 0;
    }
}

// Vérifie si le fichier existe déjà
if (file_exists($target_file)) {
    echo "Sorry, file already exists.<br>";
    $uploadOk = 0;
}

// Limite la taille du fichier (exemple: 500KB)
if ($_FILES["fileToUpload"]["size"] > 500000) {
    echo "Sorry, your file is too large.<br>";
    $uploadOk = 0;
}

// Autorise certains formats de fichier (exemple: jpg, png, jpeg, gif)
if($fileType != "jpg" && $fileType != "png" && $fileType != "jpeg" && $fileType != "gif" ) {
    echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.<br>";
    $uploadOk = 0;
}

// Vérifie si $uploadOk est défini à 0 par une erreur
if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.<br>";
// Si tout est correct, essaye de télécharger le fichier
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "The file ". htmlspecialchars(basename( $_FILES["fileToUpload"]["name"])). " has been uploaded.<br>";
    } else {
        echo "Sorry, there was an error uploading your file.<br>";
    }
}
?>