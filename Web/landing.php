<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
<link rel="alternate" media="only screen and (max-width: 640px)"
 href="mobile.html">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Power Cloud</title>
<link rel="icon" type="image/x-icon" href="favicon.ico" />
<link rel="stylesheet" href="lib.css">
<style>
/*hello*/
</style>
<script src="lib.js"></script>
<script language=javascript>
 if ((navigator.userAgent.match(/iPhone/i)) || (navigator.userAgent.match(/iPod/i))) {
   location.replace("mobile.html");
}
</script>
</head>

<body>
    <h1><span onClick="homePage()" value=""><img class="logo2" src="PowerCloudLogo.png"></span></h1>
    <span class = "signon" onClick="signIn()" value=""><img id="signin" src = "logo2.png" alt="Sign in with Google"></span>
    <div id="h2">Data - Product Repair - IT</div>
    
<!--    <div class="menu">-->
<!--        <span class="menuBar">&#9776;</span><br><br>-->
<!--        <span class="menuTxt">-->
<!--<a class="black" href="landing.php">Home</a><br><br>-->
<!--<a class="black" href="protips.html">Pro Internet Tips</a><br><br>-->
<!--<a class="black" href="privacy.html">Privacy Policy</a><br><br>-->
<!--<a class="black" href="repairs.html">Repairs</a><br><br>-->
<!--<a class="black" href="it.html">IT</a><br><br>-->

<ul class="menu">
  <li><a class="active" href="landing.php">Home</a></li>
  <li><a href="protips.html">Pro Internet Tips</a></li>
  <li><a href="privacy.html">Privacy Policy</a></li>
  <li><a href="repairs.html">Product Repair</a></li>
  <li><a href="it.php">IT</a></li>
</ul>

</span>
</div>
    
    <div class="maintitle">Our mission</div>
    <p class="one">Data<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        Power Cloud is working hard to accomplish our goal of providing affordable, uncompressed, and reliable online storage to those in our communities. Many users face problems with compression and online storage, and we aim to fix this. Compression is a process that shrinks the size of files, at a significant cost to their quality. This process is very common and is used by many popular web storage solutions, such as Google Drive. Power cloud provides a solution where data will never be compressed at a cost much lower than that of solutions like Onedrive and iCloud. You are the priority at Power Cloud which is why we offer free services like our <a href = "protips.html">pro internet tips!</a> We are also dedicated to privacy and we will never share your information to <b>ANYONE</b>. View our Privacy Policy <a href="privacy.html">here.</a> 
        <!--Thank you for your support, The Power Cloud Team. -->
    </p>
    <p  class="two">Product Repair<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        Power Cloud is a company dedicated to helping people get the tech they need for the price they should. We are dedicated to to help and support first, and our core values will not change. To <span class="link" onClick="repair()" value="">make a repair request</span> 
        please select "Product Repair" from the menu. 
        <!--Thank you for choosing us, The Power Cloud Team.-->
    </p>
    <p class="three">IT<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        Power Cloud wants to help people who sometimes have dificulity getting all the tech they have set up. 
        Our IT service is simply an opportunity for you as the customer to receive the care you need for all of your products. This service is intended to be used for everything from a simple tech question to house calls for setting up products. 
    Options for service include house calls, support lines, live chats, and a variety of in-person visits. 
    To <span class="link" onClick="it()" value="">make a request</span> please select "IT" from the menu. 
    <!--Thank you for choosing us, The Power Cloud Team. -->
    </p>
    
    
<!--
https://www.sanwebe.com/2012/11/login-with-google-api-php
https://console.developers.google.com/apis/credentials/consent?project=powercloud-230416
-->

</body>
<?php

// $str = $_GET['string'];

// $emailto = '7206447060@vtext.com';

// $toname = '';
// $emailfrom = 'pump@bot.net';
// $fromname = 'PumpBot';
// $subject = 'Sale report';
// $messagebody = $str;
// $headers = 
// 	'Return-Path: ' . $emailfrom . "\r\n" . 
// 	'From: ' . $fromname . ' <' . $emailfrom . '>' . "\r\n" . 
// 	'X-Priority: 3' . "\r\n" . 
// 	'X-Mailer: PHP ' . phpversion() .  "\r\n" . 
// // 	'Reply-To: ' . $fromname . ' <' . $emailfrom . '>' . "\r\n" .
// 	'MIME-Version: 1.0' . "\r\n" . 
// 	'Content-Transfer-Encoding: 8bit' . "\r\n" . 
// 	'Content-Type: text/plain; charset=UTF-8' . "\r\n";
// $params = '-f ' . $emailfrom;

// $test = mail($emailto, $subject, $messagebody, $headers, $params);

// $emailto = '+17203014754@mailmymobile.net';

// $test = mail($emailto, $subject, $messagebody, $headers, $params);
// // $test should be TRUE if the mail function is called correctly
// echo $test
?>

</html>