<?php
$title = "LightningMalware - Analyze";
$description = "LightningMalware";
require "./include/util.inc.php";
require "./include/header.inc.php";
require "./include/analyze.inc.php";

require_once 'config.php';
?>

<main>     
    <h1>Analyze</h1>
    <?php
        if(isset($_GET['action'])) {                
            try {
                $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
                $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

                if ($_GET['action'] === 'URL') {
                    $stmt = $conn->prepare("SELECT url FROM url WHERE url = :url");
                    $stmt->bindParam(':url', $url);
                    $stmt->execute();
                    $url_data = $stmt->fetch(PDO::FETCH_ASSOC);

                    if ($url_data) {
                        $url = $url_data['url'];
                        echo "<p>URL Retrieved from Database: $url</p>";
                    } else {
                        echo "<p>No URL found in the database</p>";
                    }
                }
                if ($_GET['action'] === 'File') {
                    $stmt = $conn->prepare("SELECT content FROM file WHERE name = :file_name");
                    $stmt->bindParam(':file_name', $file);
                    $stmt->execute();
                    $file_data = $stmt->fetch(PDO::FETCH_ASSOC);
                    
                    if ($file_data) {
                        $file_name = $file;
                        $file_content = $file_data['content'];
                        
                        $result = scan_with_clamav($file_content);
                        
                        echo "<p>File Selected: $file_name</p>";
                        echo "<p>ClamAV Result: $result</p>";
                    } else {
                        echo "<p>File not found</p>";
                    }
                }
            } catch(PDOException $e) {
                echo "Error: " . $e->getMessage();
            }
        }
    ?>
</main>

<?php require "./include/footer.inc.php"; ?>
