<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $url = $_POST["url"];
    $command = "python3 analyze_url.py " . escapeshellarg($url);
    $output = shell_exec($command);
    echo json_encode(["result" => $output]);
}
?>