
let intervalID = setInterval(myCallback, 2000);

const url = "logger.json";
let myJSON

async function asyncCall() {
  console.log('calling');
  try{
    const result = await fetch(url)
    console.log(result);
    myJSON = await result.json();
    console.log(myJSON)
    writeToLogger1_HTML();
    writeToLogger2_HTML();
    writeToLogger3_HTML();
    writeToLogger4_HTML();
  } 
  catch (error){
    console.log(error);
  }
}

function writeToLogger1_HTML(){
  for (let i = 0; i < 24; i++) {
    // document.getElementById("T1_1").value = myJSON["1"][0]
    document.getElementById("T1_" + String(i+1)).value = myJSON["1"][i]
    document.getElementById("T1_" + String(i+1)).style.color = "black"
    if (myJSON["1"][i] == 1372){
      document.getElementById("T1_" + String(i+1)).value = "??"
      document.getElementById("T1_" + String(i+1)).style.color = "red"
    }
  }

  if (isNaN(myJSON["1"][0])){
    document.getElementById("HeaderLogger1").style.backgroundColor = "red"
    return
  }
  document.getElementById("HeaderLogger1").style.backgroundColor = "green"
  return
  }
  
function writeToLogger2_HTML(){
  for (let i = 0; i < 24; i++) {
    // document.getElementById("T2_1").value = myJSON["2"][0]
    document.getElementById("T2_" + String(i+1)).value = myJSON["2"][i]
    document.getElementById("T2_" + String(i+1)).style.color = "black"
    if (myJSON["2"][i] == 1372){
      document.getElementById("T2_" + String(i+1)).value = "??"
      document.getElementById("T2_" + String(i+1)).style.color = "red"
    }
  }

  if (isNaN(myJSON["2"][0])){
    document.getElementById("HeaderLogger2").style.backgroundColor = "red"
    return
  }
  document.getElementById("HeaderLogger2").style.backgroundColor = "green"
  return
  } 
function writeToLogger3_HTML(){
  for (let i = 0; i < 24; i++) {
    // document.getElementById("T3_1").value = myJSON["3"][0]
    document.getElementById("T3_" + String(i+1)).value = myJSON["3"][i]
    document.getElementById("T3_" + String(i+1)).style.color = "black"
    if (myJSON["3"][i] == 1372){
      document.getElementById("T3_" + String(i+1)).value = "??"
      document.getElementById("T3_" + String(i+1)).style.color = "red"
    }
  }

  if (isNaN(myJSON["3"][0])){
    document.getElementById("HeaderLogger3").style.backgroundColor = "red"
    return
  }
  document.getElementById("HeaderLogger3").style.backgroundColor = "green"
  return
  }  
function writeToLogger4_HTML(){
  for (let i = 0; i < 24; i++) {
    // document.getElementById("T4_1").value = myJSON["4"][0]
    document.getElementById("T4_" + String(i+1)).value = myJSON["4"][i]
    document.getElementById("T4_" + String(i+1)).style.color = "black"
    if (myJSON["4"][i] == 1372){
      document.getElementById("T4_" + String(i+1)).value = "??"
      document.getElementById("T4_" + String(i+1)).style.color = "red"
    }
  }

  if (isNaN(myJSON["4"][0])){
    document.getElementById("HeaderLogger4").style.backgroundColor = "red"
    return
  }
  document.getElementById("HeaderLogger4").style.backgroundColor = "green"
  return
  }  

function myCallback(){
    asyncCall();
}
