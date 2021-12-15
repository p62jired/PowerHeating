
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
function setOpenWireStyle(strIndxLog, i) {
  if (myJSON[strIndxLog][i] == 1372) {
    document.getElementById("T"+ strIndxLog + "_" + String(i + 1)).value = "??";
    document.getElementById("T"+ strIndxLog + "_" + String(i + 1)).style.color = "red";
  }
}

function writeToLogger1_HTML(){
  const index = "1"
  for (let i = 0; i < 24; i++) {
    // document.getElementById("T1_1").value = myJSON["1"][0]
    document.getElementById("T" + index + "_" + String(i+1)).value = myJSON[index][i]
    document.getElementById("T" + index + "_" + String(i+1)).style.color = "black"
    setOpenWireStyle(index, i);
  }

  if (isNaN(myJSON[index][0])){
    document.getElementById("HeaderLogger" + index).style.backgroundColor = "red"
    return
  }
  document.getElementById("HeaderLogger" + index).style.backgroundColor = "green"
  return
  }
  


function writeToLogger2_HTML(){
  const index = "2"
  for (let i = 0; i < 24; i++) {
    // document.getElementById("T2_1").value = myJSON["1"][0]
    document.getElementById("T" + index + "_" + String(i+1)).value = myJSON[index][i]
    document.getElementById("T" + index + "_" + String(i+1)).style.color = "black"
    setOpenWireStyle(index, i);
  }

  if (isNaN(myJSON[index][0])){
    document.getElementById("HeaderLogger" + index).style.backgroundColor = "red"
    return
  }
  document.getElementById("HeaderLogger" + index).style.backgroundColor = "green"
  return
  } 
function writeToLogger3_HTML(){
  const index = "3"
  for (let i = 0; i < 24; i++) {
    // document.getElementById("T3_1").value = myJSON["1"][0]
    document.getElementById("T" + index + "_" + String(i+1)).value = myJSON[index][i]
    document.getElementById("T" + index + "_" + String(i+1)).style.color = "black"
    setOpenWireStyle(index, i);
  }

  if (isNaN(myJSON[index][0])){
    document.getElementById("HeaderLogger" + index).style.backgroundColor = "red"
    return
  }
  document.getElementById("HeaderLogger" + index).style.backgroundColor = "green"
  return
  }  
function writeToLogger4_HTML(){
  const index = "4"
  for (let i = 0; i < 24; i++) {
    // document.getElementById("T4_1").value = myJSON["1"][0]
    document.getElementById("T" + index + "_" + String(i+1)).value = myJSON[index][i]
    document.getElementById("T" + index + "_" + String(i+1)).style.color = "black"
    setOpenWireStyle(index, i);
  }

  if (isNaN(myJSON[index][0])){
    document.getElementById("HeaderLogger" + index).style.backgroundColor = "red"
    return
  }
  document.getElementById("HeaderLogger" + index).style.backgroundColor = "green"
  return
  }  

function myCallback(){
    asyncCall();
}
