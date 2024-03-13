<?php
$title = "LightningMalware - Analyze";
$description = "LightningMalware";
require "./include/util.inc.php";
require "./include/header.inc.php";
require "./include/analyze.inc.php";
?>
<main>     
    <h1>Analyze</h1>
    <?php
    
    if(isset($_GET['action']) && $_GET['action'] === 'URL' && isset($_GET['url'])) {
        $url = $_GET['url'];
        echo "<p>URL Entered: $url</p>";
    }
    
    if(isset($_GET['action']) && $_GET['action'] === 'File' && isset($_GET['file'])) {
        $file_name = $_GET['file'];
        echo "<p>File Selected: $file_name</p>";
    }
    ?>
</main>
<?php require"./include/footer.inc.php";?>