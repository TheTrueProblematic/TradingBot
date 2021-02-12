function signIn(){
    var uname = btoa(document.getElementById("user").value);
    var passw = btoa(document.getElementById("pass").value);
    if(uname=="VXNlcm5hbWU="&passw=="UGFzc3dvcmQ="){
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
