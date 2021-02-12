function signIn(){
    var uname = btoa(document.getElementById("user").value);
    var passw = btoa(document.getElementById("pass").value);
    if(uname=="VXNlcm5hbWU="&passw=="UGFzc3dvcmQ="){
      setCookie("signin", uname, 1);
      window.location='landing.html';
  }
}
function homePage(){
    console.log("HELLO");
    window.location='landing.html';
}
function repair(){
    console.log("Repair request form opened");
    window.location='https://docs.google.com/forms/d/e/1FAIpQLSepG2hFEUdOpcTV3EpBfJyftrWDuWXSjow9XU39r8SxGvMl0Q/viewform?usp=sf_link';
}

function check(){
  var mode = getCookie("mode");
  var log = getCookie("signin");
  // alert(mode);
  if(log!="VXNlcm5hbWU="){
    window.location='signin.html';
  } else {
    window.location='landing.html';
  }
  if(mode=="dark"){
    darkMode();
  } else {
    lightMode();
  }
}

function darkMode(){
  document.getElementById('seeinlight').style.right = '-100vw';
  document.getElementById('seeindark').style.right = '2vw';
  document.getElementById('body').style.background="#262626";
  // document.getElementById('h1').style.background="linear-gradient(#ff7200, #ff4800)";
  document.getElementById('h1text').style.color="#000000";
  document.getElementById('h1text').style.textShadow="1px 1px white";
  document.getElementById('body').style.color="#FAFAFF";
  setCookie("mode", "dark", 30);
}
function lightMode(){
  document.getElementById('seeindark').style.right = '-100vw';
  document.getElementById('seeinlight').style.right = '2vw';
  document.getElementById('body').style.background="#FAFAFF";
  document.getElementById('h1').style.background="linear-gradient(#2176FF, #33A1FD)";
  document.getElementById('h1text').style.color="#FAFAFF";
  document.getElementById('h1text').style.textShadow="2px 2px black";
  document.getElementById('body').style.color="#000000";
  setCookie("mode", "light", 30);
}
function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  var expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
