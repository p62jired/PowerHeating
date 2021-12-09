
let intervalID = setInterval(myCallback, 2000);

const url = "logger.json";
let myJSON

async function asyncCall() {
  console.log('calling');
  try{
    const result = await fetch(url)
    console.log(result);
    myJSON = await result.json();
    console.log("T1")
    console.log(myJSON["1"][0])
  } 
  catch (error){
    console.log(error);
  }
}
function writeToLogger1_HTML(){
  for (let i = 0; i < 24; i++) {
    // document.getElementById("T1_1").value = myJSON["1"][0]
    document.getElementById("T1_" + String(i+1)).value = myJSON["1"][i]
  }
}  
function writeToLogger2_HTML(){
  for (let i = 0; i < 24; i++) {
    // document.getElementById("T2_1").value = myJSON["2"][0]
    document.getElementById("T2_" + String(i+1)).value = myJSON["2"][i]
  }
}  
function writeToLogger3_HTML(){
  for (let i = 0; i < 24; i++) {
    // document.getElementById("T3_1").value = myJSON["3"][0]
    document.getElementById("T3_" + String(i+1)).value = myJSON["3"][i]
  }
}  
function writeToLogger4_HTML(){
  for (let i = 0; i < 24; i++) {
    // document.getElementById("T4_1").value = myJSON["4"][0]
    document.getElementById("T4_" + String(i+1)).value = myJSON["4"][i]
  }
} 

function myCallback(){
    asyncCall();
    writeToLogger1_HTML();
    writeToLogger2_HTML();
    writeToLogger3_HTML();
    writeToLogger4_HTML();
}
