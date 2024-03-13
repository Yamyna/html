<?php
$title = "LightningMalware - Contact";
$description = "LightningMalware";
require "./include/util.inc.php";
require "./include/header.inc.php";
require "./include/analyze.inc.php";
?>
<main>
  <h1>Contact</h1>
  <section style="margin: 30px;">
    <div class="contact-form-container">
        <h2 class="contact-form-title">Contact us</h2>
        <form action="process.php" method="post" id="contact-form">     
            <p class="contact-form-label">Email</p>
            <input type="email" name="email" class="contact-form-input contact-form-placeholder" placeholder="Your email" required>
    
            <p class="contact-form-label">Message</p>
            <textarea name="message" class="contact-form-input contact-form-placeholder" placeholder="Your message"></textarea>
            
            <input type="button" value="Send the message" class="contact-form-button" id="validate-button">
        </form>
    </div>           
  </section>
  <script>
  document.addEventListener("DOMContentLoaded", function () {
      var validateButton = document.getElementById("validate-button");
      validateButton.addEventListener("click", function () {
          var emailInput = document.querySelector("input[type='email']");
          var messageTextarea = document.querySelector("textarea");

          if (emailInput.checkValidity()) {
              var email = emailInput.value;
              var message = messageTextarea.value;
              var subject = "Contact from LightningMalware";
              var mailtoLink = "mailto:lightningmalware@gmail.com?subject=" + subject + "&body=" + message;
              
              window.location.href = mailtoLink;
          } else {
              alert("Invalid email address. Please enter a valid email.");
          }
      });
  });
  </script>

</main>
<?php require"./include/footer.inc.php";?>