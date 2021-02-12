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

function darkMode(){
  document.getElementById('seeinlight').style.right = '-100vw';
  document.getElementById('seeindark').style.right = '2vw';
  document.getElementById('body').style.background="#262626";
  // document.getElementById('h1').style.background="linear-gradient(#ff7200, #ff4800)";
  document.getElementById('h1text').style.color="#000000";
  document.getElementById('h1text').style.textShadow="1px 1px white";
  document.getElementById('body').style.color="#FAFAFF";
}
function lightMode(){
  document.getElementById('seeindark').style.right = '-100vw';
  document.getElementById('seeinlight').style.right = '2vw';
  document.getElementById('body').style.background="#FAFAFF";
  document.getElementById('h1').style.background="linear-gradient(#2176FF, #33A1FD)";
  document.getElementById('h1text').style.color="#FAFAFF";
  document.getElementById('h1text').style.textShadow="2px 2px black";
  document.getElementById('body').style.color="#000000";
}
