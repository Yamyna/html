<?php
require_once 'config.php';

$action = $_POST['action'];

if ($action === 'URL') {
    $url = $_POST['url'];
    
} elseif ($action === 'File') {
    
}


if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['action'])) {

    if ($_POST['action'] === 'File' && isset($_FILES['file']) && $_FILES['file']['error'] === UPLOAD_ERR_OK) {
        $file_name = $_FILES['file']['name'];
        $file_content = file_get_contents($_FILES['file']['tmp_name']);

        try {
            $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $stmt = $conn->prepare("INSERT INTO file (name, content) VALUES (:file_name, :file_content)");
            $stmt->bindParam(':file_name', $file_name);
            $stmt->bindParam(':file_content', $file_content);
            $stmt->execute();
            echo "File saved successfully";
        } catch(PDOException $e) {
            echo "Error connecting to database: " . $e->getMessage();
        }
        $conn = null;
    } 
    elseif ($_POST['action'] === 'URL' && isset($_POST['url'])) {
        $url = $_POST['url'];
        try {
            $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $stmt = $conn->prepare("INSERT INTO url (url) VALUES (:url)");
            $stmt->bindParam(':url', $url);
            $stmt->execute();
            echo "URL saved successfully";
        } catch(PDOException $e) {
            echo "Error connecting to database: " . $e->getMessage();
        }
        $conn = null;
    } else {
        echo "Invalid request";
    }
} else {
    echo "Invalid request";
}
$response = array('success' => true);
echo json_encode($response);
?>