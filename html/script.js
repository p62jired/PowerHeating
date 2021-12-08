
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
  document.getElementById("T1_1").value = myJSON["1"][0]
  document.getElementById("T1_2").value = myJSON["1"][1]
  document.getElementById("T1_3").value = myJSON["1"][2]
  document.getElementById("T1_4").value = myJSON["1"][3]
  document.getElementById("T1_5").value = myJSON["1"][4]
  document.getElementById("T1_6").value = myJSON["1"][5]
  document.getElementById("T1_7").value = myJSON["1"][6]
  document.getElementById("T1_8").value = myJSON["1"][7]
  document.getElementById("T1_9").value = myJSON["1"][8]
  document.getElementById("T1_10").value = myJSON["1"][9]
  document.getElementById("T1_11").value = myJSON["1"][10]
  document.getElementById("T1_12").value = myJSON["1"][11]
  document.getElementById("T1_13").value = myJSON["1"][12]
  document.getElementById("T1_14").value = myJSON["1"][13]
  document.getElementById("T1_15").value = myJSON["1"][14]
  document.getElementById("T1_16").value = myJSON["1"][15]
  document.getElementById("T1_17").value = myJSON["1"][16]
  document.getElementById("T1_18").value = myJSON["1"][17]
  document.getElementById("T1_19").value = myJSON["1"][18]
  document.getElementById("T1_20").value = myJSON["1"][19]
  document.getElementById("T1_21").value = myJSON["1"][20]
  document.getElementById("T1_22").value = myJSON["1"][21]
  document.getElementById("T1_23").value = myJSON["1"][22]
  document.getElementById("T1_24").value = myJSON["1"][23]
}  
function writeToLogger2_HTML(){
  document.getElementById("T2_1").value = myJSON["2"][0]
  document.getElementById("T2_2").value = myJSON["2"][1]
  document.getElementById("T2_3").value = myJSON["2"][2]
  document.getElementById("T2_4").value = myJSON["2"][3]
  document.getElementById("T2_5").value = myJSON["2"][4]
  document.getElementById("T2_6").value = myJSON["2"][5]
  document.getElementById("T2_7").value = myJSON["2"][6]
  document.getElementById("T2_8").value = myJSON["2"][7]
  document.getElementById("T2_9").value = myJSON["2"][8]
  document.getElementById("T2_10").value = myJSON["2"][9]
  document.getElementById("T2_11").value = myJSON["2"][10]
  document.getElementById("T2_12").value = myJSON["2"][11]
  document.getElementById("T2_13").value = myJSON["2"][12]
  document.getElementById("T2_14").value = myJSON["2"][13]
  document.getElementById("T2_15").value = myJSON["2"][14]
  document.getElementById("T2_16").value = myJSON["2"][15]
  document.getElementById("T2_17").value = myJSON["2"][16]
  document.getElementById("T2_18").value = myJSON["2"][17]
  document.getElementById("T2_19").value = myJSON["2"][18]
  document.getElementById("T2_20").value = myJSON["2"][19]
  document.getElementById("T2_21").value = myJSON["2"][20]
  document.getElementById("T2_22").value = myJSON["2"][21]
  document.getElementById("T2_23").value = myJSON["2"][22]
  document.getElementById("T2_24").value = myJSON["2"][23]
}  
function myCallback()
{
    asyncCall();
    writeToLogger1_HTML();
    writeToLogger2_HTML();
}
