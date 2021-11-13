// Set the date we're counting down to
var countDownDate = new Date("Dec 14, 2055").getTime();

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
updateCountDown()
// Update the count down every 1 second
var x = setInterval(updateCountDown, 1000);

function getDateForDate() {
	// some how get data from api
	var dateToSend = document.getElementById("dateToSend").value;
	alert(dateToSend)
}

//TODO: no days in selector