<?php
$title = "LightningMalware";
$description = "LightningMalware";
require "./include/util.inc.php";
require "./include/header.inc.php";
?>

<main>
    <h1>Home</h1>
    <section>
        <div class="slogan" style="text-align: center; margin: 30px;"> 
            <img src="./images/logo_lm.png" alt="logo"/>
            <h2>LightningMalware</h2>
            <p>Analyze, Detect, Protect: Your Shield Against Digital Threats</p>
        </div>
        <form id="analysisForm" method="post" class="form-container" enctype="multipart/form-data">
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
            <input type="button" onclick="submitForm()" class="form-button submit-button" value="Validate">
        </form>
    </section>
</main>

<head>
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
</head>

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
    
    function submitForm() {
        var action = document.querySelector('input[name="action"]:checked').value;
        var xhr = new XMLHttpRequest();

        if (action === 'URL') {
            var url = document.querySelector('input[name="url"]').value;
            var formData = new FormData();
            formData.append('action', 'URL');
            formData.append('url', url);

            xhr.onload = function() {
                if (xhr.status === 200) {
                    try {
                        var response = JSON.parse(xhr.responseText);
                        if (response.success) {
                            window.location.href = 'analyze.php?action=URL&url=' + encodeURIComponent(url);
                        } else {
                            alert('Error saving URL: ' + response.message);
                        }
                    } catch (e) {
                        alert('An error occurred while processing the response.');
                    }
                } else {
                    alert('An error occurred while saving the URL.');
                }
            };
            xhr.send(formData);
        }
        
        if (action === 'File') {
            var fileInput = document.querySelector('input[name="file"]');
            var file = fileInput.files[0];
            var formData = new FormData();
            formData.append('action', 'File');
            formData.append('file', file);

            xhr.onload = function() {
                if (xhr.status === 200) {
                    try {
                        var response = JSON.parse(xhr.responseText);
                        if (response.success) {
                            window.location.href = 'analyze.php?action=File&file=' + encodeURIComponent(file.name);
                        } else {
                            alert('Error saving file: ' + response.message);
                        }
                    } catch (e) {
                        alert('An error occurred while processing the response.');
                    }
                } else {
                    alert('An error occurred while saving the file.');
                }
            };
            xhr.send(formData);
        }
    }
</script>

<?php require "./include/footer.inc.php"; ?>