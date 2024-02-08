<?php
$title = "LightningMalware";
$description = "LightningMalware";
require "./include/util.inc.php";
require "./include/header.inc.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $action = $_POST["action"];
    
    if ($action == "URL") {
        $url = $_POST["url"];
        $command = "python3 analyze_url.py " . escapeshellarg($url);
        $output = shell_exec($command);
        echo json_encode(["result" => $output]);
    } elseif ($action == "File") {
        
    } else {
        
        echo json_encode(["error" => "Invalid action"]);
    }
}

?>
<main>
    <h1>Home</h1>
    <section>
        <div class="slogan" style="text-align: center; margin: 30px;"> 
            <img src="./images/logo_lm.png" alt="logo"/>
            <h2>LightningMalware</h2>
            <p>Analyze, Detect, Protect: Your Shield Against Digital Threats</p>
        </div>

        <form method="post" class="form-container" enctype="multipart/form-data">
            <h2>What do you want to analyze?</h2>
            <div class="radio-container">
                <input type="radio" class="form-button" name="action" value="URL" id="urlRadio" onclick="showURLInput()">
                <label for="urlRadio">URL</label>
            </div>
            <div class="radio-container">
                <input type="radio" class="form-button" name="action" value="File" id="fileRadio" onclick="showFileInput()">
                <label for="fileRadio">File</label>
            </div>
            <div id="urlForm" style="display: none;">
                <input type="text" class="form-input" name="url" placeholder="Enter your URL">
            </div>
            <div id="fileForm" style="display: none;">
                <input type="file" class="file-input" id="fileInput" name="file" style="display: none; color: #212121;" onchange="updateSelectedFileName(this)">
                <label for="fileInput" class="form-input" style="border: 1px solid #ccc; padding: 5px; border-radius: 5px; cursor: pointer; color: black; font-family: Arial, sans-serif;">
                    Choose a file
                </label>
                <span id="selectedFileName" style="display: none; padding: 10px;"></span>
            </div>
            <input type="submit" class="form-button submit-button" value="Validate">
            
        </form>
    </section>
</main>

<head>
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
</head>

<script>
    $(document).ready(function(){
        $("form").submit(function(event){
            event.preventDefault();

            var formData = new FormData($(this)[0]);

            $.ajax({
                type: "POST",
                url: "analyze.php",
                data: formData,
                contentType: false,
                processData: false,
                success: function(response){
                    console.log(response.result);
                },
                error: function(error){
                    console.log("Erreur lors de l'analyse de l'URL.");
                }
            });
        });
    });
</script>
<script>
    function showURLInput() {
        document.getElementById('urlForm').style.display = 'block';
        document.getElementById('fileForm').style.display = 'none';
    }

    function showFileInput() {
        document.getElementById('fileForm').style.display = 'block';
        document.getElementById('urlForm').style.display = 'none';
    }

    function updateSelectedFileName(input) {
        var selectedFileName = document.getElementById("selectedFileName");
        selectedFileName.textContent = input.files[0].name;
        selectedFileName.style.display = 'block';
    }

</script>
<?php require "./include/footer.inc.php"; ?>
