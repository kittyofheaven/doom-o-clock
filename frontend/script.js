

function updateCountDown() {

	// Get today's date and time
	var now = new Date().getTime();

	// Find the distance between now and the count down date
	var distance = countDownDate - now;

	// Time calculations for days, hours, minutes and seconds
	var years = Math.floor(distance / (1000 * 60 * 60 * 24 * 365.25));
	// console.table({"dis":distance/ (1000 * 60 * 60 * 24* 365.25),"leftover":distance %  (1000 * 60 * 60 * 24* 365.25), "getmonths":(1000 * 60 * 60),"res":(distance %  (1000 * 60 * 60 * 24* 365.25)) / (1000 * 60 * 60 *24 * 30.5)})
	var months = Math.floor((distance %  (1000 * 60 * 60 * 24 * 365.25)) / (1000 * 60 * 60 *24 * 30));
	var days = Math.floor(((distance %  (1000 * 60 * 60 * 24 * 30))) / (1000 * 60 * 60 *24));
	// var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
	// var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
	// var seconds = Math.floor((distance % (1000 * 60)) / 1000);

	// Display the result in the element with id="demo"
	document.getElementById("countDown").innerHTML = years + " years : " + months + " months : " + days + " days";

	// If the count down is finished, write some text
	if (distance < 0) {
		clearInterval(x);
		document.getElementById("countDown").innerHTML = "EXPIRED";
	}
}

//update the timer on page load

// Update the count down every 1 second
var x = setInterval(updateCountDown, 1000);

async function getDateForDate() {
	// some how get data from api
	let dateToSend = new Date(document.getElementById("dateToSend").value);
	// console.table('en-US', {
  //   minimumIntegerDigits: 2,
  //   useGrouping: false
  // });
	document.getElementById("dateToSend").value = dateToSend.getFullYear()+"-"+(dateToSend.getMonth()+1).toLocaleString('en-US', {
    minimumIntegerDigits: 2,
    useGrouping: false
  })+"-01";
	let resultsObj = await fetchAsync("https://doom-clock-api.herokuapp.com/atmosphere?Year="+dateToSend.getFullYear()+"&Month="+(dateToSend.getMonth()+1));
	console.log(resultsObj)


	let numberElls = document.getElementsByClassName("outputRate");

	for(let i = 0; i < numberElls.length; i++){
		if(i == 0){
			numberElls[i].innerText = Math.round(resultsObj.CO2)+" ppmv"
		}
		if(i == 1){
			numberElls[i].innerText = Math.round(resultsObj.CH4)+" ppmv"
		}
		if(i == 2){
			numberElls[i].innerText = Math.round(resultsObj.N2O)+" ppmv"
		}
		if(i == 3){
			numberElls[i].innerText = Math.round(resultsObj.TSI)+" W/m2"
		}
		if(i == 4){
			numberElls[i].innerText = Math.round(resultsObj["CFC-11"])+" ppbv"
		}
		if(i == 5){
			numberElls[i].innerText = Math.round(resultsObj["CFC-12"])+" ppbv"
		}
		if(i == 6){
			numberElls[i].innerText = (parseFloat(resultsObj.Aerosols)*100).toFixed(3)+"% nm"
		}
		if(i == 7){
			numberElls[i].innerText = "+"+parseFloat(resultsObj.Temp).toFixed(3) +" °C"
		}
	}
}

async function fetchAsync(url) {
  let response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
  });
  let data = await response.json();
  return data;
}

let countDownDate;

async function startCountDownTimer() {
  let response = await fetch("https://doom-clock-api.herokuapp.com/atmosphere", {
    method: 'GET', // *GET, POST, PUT, DELETE, etc.
  });
  let data = await response.json();
	// console.table(data)
	// Set the date we're counting down to
	countDownDate = new Date(data.doom_year+"-"+(data.doom_month+1)+"-01").getTime();
	updateCountDown()
}

startCountDownTimer()


getDateForDate()