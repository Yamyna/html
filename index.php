<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

set_time_limit(0);  // Augmente le temps d'exécution maximum
ini_set('max_execution_time', 0); // temps d'exécution illimité
ini_set('memory_limit', '512M');  // ajustez selon les besoins de votre script

$message = "";
if (isset($_POST["scanF"])) {
    $uploadDir = "/uploads/";
    $uploadFile = $uploadDir . basename($_FILES["fileToUpload"]["name"]);
    
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $uploadFile)) {
        chmod($uploadFile, 0777);
        $message = "File upload successfully. <br>";

        $command = "/script/script_LightningMalware/docker/script_lancement.sh $uploadFile";
        $message .= "Executing command: $command <br>";

        exec($command, $output, $return_var).;

        if ($return_var !== 0) {
            $message .= "Command failed to execute.<br>";
        } else {
            $message .= "Command output: " . nl2br(htmlspecialchars(implode("\n", $output))) . "<br>";
        }

        $message .= "Return status: " . $return_var . "<br>";
    } else {
        $message = "Error with the file upload. <br>";
    }
} elseif (isset($_POST["scanURL"])) {
    $urlToScan = $_POST["urlToScan"];

    $command = "/script/script_LightningMalware/docker/script_lancement_url.sh $urlToScan";
    $message .= "Executing command: $command <br>";

    exec($command, $output, $return_var);

    if ($return_var !== 0) {
        $message .= "Command failed to execute.<br>";
    } else {
        $message .= "Command output: " . nl2br(htmlspecialchars(implode("\n", $output))) . "<br>";
    }
    $message .= "Return status: " . $return_var . "<br>";
}
?>
<!DOCTYPE html>
<html lang="en">

    <head>
        <!-- Metadata -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="Analyze, Detect, Protect: Your Shield Against Digital Threats">
        <meta name="author" content="Yamyna RENAI - Morgane REYNAUD">

        <!-- Metadata -->
        <link rel="icon" href="assets/images/lmlogo.ico" type="image/x-icon">
        <link href="https://fonts.googleapis.com/css?family=Raleway:100,200,300,400,500,600,700,800,900&display=swap" rel="stylesheet">
        
        <!-- Title -->
        <title>LightningMalware</title>

        <!-- Additional CSS Files -->
        <link rel="stylesheet" type="text/css" href="assets/css/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="assets/css/font-awesome.css">
        <link rel="stylesheet" href="assets/css/templatemo-breezed.css">
        <link rel="stylesheet" href="assets/css/owl-carousel.css">
        <link rel="stylesheet" href="assets/css/lightbox.css">
    </head>
    
    <body>
    
        <!-- ***** Preloader Start ***** -->
        <div id="preloader">
            <div class="jumper">
                <div></div>
                <div></div>
                <div></div>
            </div>
        </div>  
        <!-- ***** Preloader End ***** -->
    
    
        <!-- ***** Header Area Start ***** -->
        <header class="header-area header-sticky">
            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <nav class="main-nav">
                            <!-- ***** Logo Start ***** -->
                            <a href="index.html" class="logo">
                                LightningMalware
                            </a>
                            <!-- ***** Logo End ***** -->
                            <!-- ***** Menu Start ***** -->
                            <ul class="nav">
                                <li class="scroll-to-section"><a href="#top" class="active">Home</a></li>
                                <li class="scroll-to-section"><a href="#about">About Us</a></li>
                                <li class="scroll-to-section"><a href="#testimonials">Team</a></li>
                                <li class="scroll-to-section"><a href="#analyze">Analyze</a></li>
                                <li class="scroll-to-section"><a href="#contact-us">Contact Us</a></li> 
                            </ul>        
                            <a class='menu-trigger'>
                                <span>Menu</span>
                            </a>
                            <!-- ***** Menu End ***** -->
                        </nav>
                    </div>
                </div>
            </div>
        </header>
        <!-- ***** Header Area End ***** -->

        <!-- ***** Main Banner Area Start ***** -->
        <div class="main-banner header-text" id="top">
            <div class="Modern-Slider">
            <!-- Item -->
            <div class="item">
                <div class="img-fill">
                    <img src="assets/images/slide-01.jpg" alt="">
                    <div class="text-content">
                    <h3>Welcome To LigthningMalware</h3>
                    <h5>Analyze, Detect, Protect: Your Shield Against Digital Threats</h5>
                    <a href="#about" class="main-stroked-button">About us</a>
                    </div>
                </div>
            </div>
            <!-- // Item -->
            <!-- Item -->
            <div class="item">
                <div class="img-fill">
                    <img src="assets/images/slide-02.jpg" alt="">
                    <div class="text-content">
                    <h3>Start now to protect yourself </h3>
                    <h5>Scan your url or your file</h5>
                    <a href="#analyze" class="main-stroked-button">Scan File</a>
                    <a href="#analyze" class="main-filled-button">Scan URL</a>
                    </div>
                </div>
            </div>

            </div>
        </div>
        <div class="scroll-down scroll-to-section"><a href="#about"><i class="fa fa-arrow-down"></i></a></div>
        <!-- ***** Main Banner Area End ***** -->

        <!-- ***** About Area Starts ***** -->
        <section class="section" id="about">
            <div class="container">
                <div class="row">
                    <div class="col-lg-6 col-md-6 col-xs-12">
                        <div class="left-text-content">
                            <div class="section-heading">
                                <h6>About Us</h6>
                                <h2>Project inspired by VirusTotal</h2>
                            </div>
                            <div class="row">
                                <div class="col-md-6 col-sm-6">
                                    <div class="service-item">
                                        <img src="assets/images/service-item-01.png" alt="">
                                        <h4>API</h4>
                                    </div>
                                </div>
                                <div class="col-md-6 col-sm-6">
                                    <div class="service-item">
                                        <img src="assets/images/service-item-01.png" alt="">
                                        <h4>Anti virus</h4>
                                    </div>
                                </div>
                                <div class="col-md-6 col-sm-6">
                                    <div class="service-item">
                                        <img src="assets/images/service-item-01.png" alt="">
                                        <h4>Malware</h4>
                                    </div>
                                </div>
                                <div class="col-md-6 col-sm-6">
                                    <div class="service-item">
                                        <img src="assets/images/service-item-01.png" alt="">
                                        <h4>File & URL</h4>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 col-md-6 col-xs-12">
                        <div class="right-text-content">
                            <p><a rel="nofollow noopener" href="https://templatemo.com/tm-543-breezed" target="_parent">LightningMalware</a> is a project inspired by VirusTotal. 
                            <br><br>Do you have a suspicious URL? Or a suspicious file? No problem! LightningMalware is here to help !
                        <br><br>Enter your url or upload your file and you will know if you are in danger. Trust us and enjoy safe browsing. If you have any questions, please <a rel="nofollow noopener" href="https://templatemo.com/contact" target="_parent">contact us</a>.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- ***** About Area Ends ***** -->

        <!-- ***** Features Big Item Start ***** -->
        <section class="section" id="features">
            <div class="container">
                <div class="row">
                    <div class="col-lg-4 col-md-6 col-sm-12 col-xs-12" data-scroll-reveal="enter left move 30px over 0.6s after 0.4s">
                        <div class="features-item">
                            <div class="features-icon">
                                <img src="assets/images/features-icon-1.png" alt="">
                            </div>
                            <div class="features-content">
                                <h4>API</h4>
                                <p>We use Google and OTX APIs to analyze your urls.</p>
                                <a href="#" class="text-button-icon">
                                    Learn More <i class="fa fa-arrow-right"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12 col-xs-12" data-scroll-reveal="enter bottom move 30px over 0.6s after 0.4s">
                        <div class="features-item">
                            <div class="features-icon">
                                <img src="assets/images/features-icon-1.png" alt="">
                            </div>
                            <div class="features-content">
                                <h4>Antivirus</h4>
                                <p>To analyze your files we use anti viruses like Clamav and Yara.</p>
                                <a href="#" class="text-button-icon">
                                    Learn More <i class="fa fa-arrow-right"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-12 col-xs-12" data-scroll-reveal="enter right move 30px over 0.6s after 0.4s">
                        <div class="features-item">
                            <div class="features-icon">
                                <img src="assets/images/features-icon-1.png" alt="">
                            </div>
                            <div class="features-content">
                                <h4>Our antivirus</h4>
                                <p>We develop an antivirus that analyzes supsicious behavior in your files. You will receive a report of the scan of your file to determine if it is potentially malicious.</p>
                                <a href="#" class="text-button-icon">
                                    Learn More <i class="fa fa-arrow-right"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- ***** Features Big Item End ***** -->


        <style>
            .form-container {
                background: #fff;
                padding: 2%;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                margin: 1%;
                width: 80%;
                max-width: 300px;
            }
            .form-input {
                width: 96%;
                padding: 1%;
                margin-bottom: 2%;
                border: 1px solid #ccc;
                border-radius: 5px;
                transition: border-color 0.3s;
            }
            .form-input:focus {
                border-color: #007bff;
            }
            .form-submit {
                width: 100%;
                padding: 1.5%;
                border: none;
                border-radius: 5px;
                background-color: #007bff;
                color: #fff;
                font-size: 14px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .form-submit:hover {
                background-color: #0056b3;
            }
            .form-title {
                font-size: 16px;
                margin-bottom: 2%;
                color: #333;
                text-align: center;
            }
            .custom-file-input-container {
                position: relative;
                width: 100%;
                height: 36px;
                overflow: hidden;
            }
            .custom-file-input {
                position: absolute;
                width: 100%;
                height: 100%;
                opacity: 0;
                cursor: pointer;
            }
            .custom-file-label {
                width: 96%;
                padding: 1%;
                margin-bottom: 2%;
                border: 1px solid #ccc;
                border-radius: 5px;
                display: inline-block;
                cursor: pointer;
                text-align: center;
                background-color: #fff;
            }
        </style>
        <script>
            document.getElementById('fileToUpload').addEventListener('change', function() {
                var fileName = this.files[0].name;
                this.previousElementSibling.textContent = fileName ? fileName : 'Choose a file';
            });
        </script>
        <!-- ***** Analyze Starts-->
        <section class="section" id="analyze">
            <div class="container">
                <div class="row">
                    <div class="col-lg-6 col-md-6 col-xs-12">
                        <div class="left-text-content">
                            <div class="section-heading">
                                <h6>Analyze</h6>
                                <h2>Choose what you want to scan!</h2>
                            </div>
                            <div class="row">
                                <div class="col-md-6 col-sm-6">
                                    <br><br>
                                    <form name="fo" id="fileUploadForm" class="form-container" action="" method="post" enctype="multipart/form-data">
                                        <div class="form-title">Scan File</div>
                                        <div class="custom-file-input-container">
                                            <label for="fileToUpload" class="custom-file-label">Choose a file</label>
                                            <input type="file" name="fileToUpload" id="fileToUpload" class="custom-file-input" required />
                                        </div>
                                        <input type="submit" name="scanF" class="form-submit" value="Scan File" />
                                    </form>
                                </div>
                                <div class="col-md-6 col-sm-6">
                                    <br><br>
                                    <form name="fo" id="urlScanForm" class="form-container" action="" method="post">
                                        <div class="form-title">Scan URL</div>
                                        <input type="text" name="urlToScan" class="form-input" required placeholder="Enter a URL"/>
                                        <input type="submit" name="scanURL" class="form-submit" value="Scan URL" />
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 col-md-6 col-xs-12">
                        <div class="right-text-content">
                            <p><a rel="nofollow noopener" href="https://templatemo.com/tm-543-breezed" target="_parent">Scan result</a>
                                <br><br>Scan result :
                                <br><br><div><?php echo $message; ?></div>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- ***** Analyze End-->

        <!-- ***** Team Starts ***** -->
        <section class="section" id="testimonials">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12">
                        <div class="section-heading">
                            <h6>Team</h6>
                            <h2>young and talented members</h2>
                        </div>
                    </div>
                    <div class="col-lg-12 col-md-12 col-sm-12 mobile-bottom-fix-big" data-scroll-reveal="enter left move 30px over 0.6s after 0.4s">
                        <div class="owl-carousel owl-theme">
                            <div class="item author-item">
                                <div class="member-thumb">
                                    <img src="assets/images/member-item-04.jpg" alt="">
                                    <div class="hover-effect">
                                        <div class="hover-content">
                                            <ul>
                                                <li><a href="https://www.linkedin.com/in/morgane-reynaud-70625014b"><i class="fa fa-linkedin"></i></a></li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                                <h4>Morgane REYNAUD</h4>
                                <span>Cybersecurity student</span>
                            </div>
                            <div class="item author-item">
                                <div class="member-thumb">
                                    <h4>Web</h4>
                                    <span>The most important</span> 
                                </div> 
                            </div>
                            <div class="item author-item">
                                <div class="member-thumb">
                                    <img src="assets/images/member-item-05.jpg" alt="">
                                    <div class="hover-effect">
                                        <div class="hover-content">
                                            <ul>
                                                <li><a href="https://www.linkedin.com/in/yamyna-renaï"><i class="fa fa-linkedin"></i></a></li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                                <h4>Yamyna RENAI</h4>
                                <span>Cybersecurity student</span>
                            </div>                            
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- ***** Team Ends ***** -->
        
        <!-- ***** Contact Us Starts ***** -->
        <section class="section" id="contact-us">
            <div class="container">
                <div class="row">
                    <div class="col-lg-4 col-md-4 col-xs-12">
                        <div class="left-text-content">
                            <div class="section-heading">
                                <h6>Contact Us</h6>
                                <h2>Feel free to keep in touch with us!</h2>
                            </div>
                            <ul class="contact-info">
                                <li><img src="assets/images/contact-info-02.png" alt="">lightningmalware@gmail.com</li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-8 col-md-8 col-xs-12">
                        <div class="contact-form">
                            <form id="contact" action="" method="get">
                            <div class="row">
                                <div class="col-md-6 col-sm-12">
                                <fieldset>
                                    <input name="name" type="text" id="name" placeholder="Your Name *" required="">
                                </fieldset>
                                </div>
                                <div class="col-md-6 col-sm-12">
                                <fieldset>
                                    <input name="phone" type="text" id="phone" placeholder="Your Phone" required="">
                                </fieldset>
                                </div>
                                <div class="col-md-6 col-sm-12">
                                <fieldset>
                                    <input name="email" type="email" id="email" placeholder="Your Email *" required="">
                                </fieldset>
                                </div>
                                <div class="col-md-6 col-sm-12">
                                <fieldset>
                                    <input name="subject" type="text" id="subject" placeholder="Subject">
                                </fieldset>
                                </div>
                                <div class="col-lg-12">
                                <fieldset>
                                    <textarea name="message" rows="6" id="message" placeholder="Message" required=""></textarea>
                                </fieldset>
                                </div>
                                <div class="col-lg-12">
                                <fieldset>
                                    <button type="submit" id="form-submit" class="main-button-icon">Send Message Now <i class="fa fa-arrow-right"></i></button>
                                </fieldset>
                                </div>
                            </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- ***** Contact Us Ends ***** -->
    
        <!-- ***** Footer Start ***** -->
        <footer>
            <div class="container">
                <div class="row">
                    <div class="col-lg-6 col-xs-12">
                        <div class="left-text-content">
                            <p>Copyright &copy; 2024 Yamyna RENAI - Morgane REYNAUD. </p>
                        </div>
                    </div>
                    <div class="col-lg-6 col-xs-12">
                        <div class="right-text-content">
                                <ul class="social-icons">
                                    <li><p>Follow Us</p></li>
                                    <li><a rel="nofollow" href="https://www.linkedin.com/in/yamyna-renaï"><i class="fa fa-linkedin"></i></a></li>
                                    <li><a rel="nofollow" href="https://www.linkedin.com/in/morgane-reynaud-70625014b"><i class="fa fa-linkedin"></i></a></li>
                                </ul>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
        <!-- ***** Footer Ends ***** -->

        <!-- jQuery -->
        <script src="assets/js/jquery-2.1.0.min.js"></script>

        <!-- Bootstrap -->
        <script src="assets/js/popper.js"></script>
        <script src="assets/js/bootstrap.min.js"></script>

        <!-- Plugins -->
        <script src="assets/js/owl-carousel.js"></script>
        <script src="assets/js/scrollreveal.min.js"></script>
        <script src="assets/js/waypoints.min.js"></script>
        <script src="assets/js/jquery.counterup.min.js"></script>
        <script src="assets/js/imgfix.min.js"></script> 
        <script src="assets/js/slick.js"></script> 
        <script src="assets/js/lightbox.js"></script> 
        <script src="assets/js/isotope.js"></script> 
        
        <!-- Global Init -->
        <script src="assets/js/custom.js"></script>

        <script>
            $(function() {
                var selectedClass = "";
                $("p").click(function(){
                selectedClass = $(this).attr("data-rel");
                $("#portfolio").fadeTo(50, 0.1);
                    $("#portfolio div").not("."+selectedClass).fadeOut();
                setTimeout(function() {
                $("."+selectedClass).fadeIn();
                $("#portfolio").fadeTo(50, 1);
                }, 500);  
                });
            });
        </script>
  </body>
</html>