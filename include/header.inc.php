<!DOCTYPE html>
<html lang= "en">
    <head>
        <title> <?=$title;?> </title>
        <meta charset="UTF-8"/>
        <link rel = "icon" href = "./images/logo_lm.ico"/>
        <meta name = "description" content = "<?=$description?>"/>
        <meta name = "author" content = "REYNAUD Morgane - RENAI Yamyna - RIBEIRO Hugo"/>
        <link rel="stylesheet" href="<?=style();?>"/>
        <script src="https://kit.fontawesome.com/48c37e4e82.js" crossorigin="anonymous"></script>
    </head>
    <body>
        <header tabindex="0">
            <a class="logo" href="index.php" title="Home page">
                <span>LightningMalware</span>
                <img src="./images/logo_lm_min.png" alt="Logo LightningMalware" style="margin-left: 10px;">
            </a>
            <div id="nav-container">
                <div class="bg"></div>
                <div class="button" tabindex="0">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </div>
                <div id="nav-content" tabindex="0">
                    <ul>
                        <li><a href="index.php">Home</a></li>
                        <li><a href="contact.php">Contact</a></li>
                        <li><a href="manuel.php">Manual</a></li>
                        <li><a href="<?=$_SERVER['PHP_SELF'];?><?=urlStyle();?>"> style </a></li>
                    </ul>
                </div>
            </div>
        </header>
   
