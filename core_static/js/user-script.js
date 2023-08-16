// This is for PopUp of User Menu on the top right corner.
const toggleBtn = document.querySelector(".user-toggle-btn-display");
const toggleDiv = document.querySelector(".user-list-block-display");

toggleBtn.addEventListener("click", () => {
  toggleDiv.style.display =
    toggleDiv.style.display === "none" ? "block" : "none";
});

document.addEventListener("click", (event) => {
  if (!toggleDiv.contains(event.target) && event.target !== toggleBtn) {
    toggleDiv.style.display = "none";
  }
});

const sideBarBtn = document.querySelector("[user-toggle-menu]");
const sideBar = document.querySelector("[data-sidebar]");

sideBarBtn.addEventListener("click", () => {
  sideBar.classList.toggle("open");
});

// This Block Belongs to the Calender.
const monthYearElement = document.querySelector(".monthYear");
const datesElement = document.querySelector(".dates");
const prevBtn = document.querySelector(".prevBtn");
const nextBtn = document.querySelector(".nextBtn");

let currentDate = new Date();

function updateCalendar() {
  const currentYear = currentDate.getFullYear();
  const currentMonth = currentDate.getMonth();

  const firstDay = new Date(currentYear, currentMonth, 0);
  const lastDay = new Date(currentYear, currentMonth + 1, 0);
  const totalDays = lastDay.getDate();
  const firstDayIndex = firstDay.getDay();
  const lastDayIndex = lastDay.getDay();

  const monthYearString = currentDate.toLocaleString("default", {
    month: "long",
    year: "numeric",
  });
  monthYearElement.textContent = monthYearString;
  let datesHTML = "";
  for (let i = firstDayIndex; i > 0; i--) {
    const prevDate = new Date(currentYear, currentMonth, 0 - i + 1);
    datesHTML += `<div class="date inactive"> ${prevDate.getDate()} </div>`;
  }

  for (let i = 1; i <= totalDays; i++) {
    const date = new Date(currentYear, currentMonth, i);
    const activeClass =
      date.toDateString() === new Date().toDateString() ? "active" : "";
    datesHTML += `<div class='date ${activeClass}'> ${i} </div>`;
  }

  for (let i = 1; i <= 7 - lastDayIndex; i++) {
    const nextDate = new Date(currentYear, currentMonth + 1, i);
    datesHTML += `<div class="date inactive"> ${nextDate.getDate()} </div>`;
  }

  datesElement.innerHTML = datesHTML;
}

prevBtn.addEventListener("click", () => {
  // console.log('Worked')
  currentDate.setMonth(currentDate.getMonth() - 1);
  updateCalendar();
});

nextBtn.addEventListener("click", () => {
  // console.log('also worked')
  currentDate.setMonth(currentDate.getMonth() + 1);
  updateCalendar();
});

updateCalendar();

// Bmi Calculator.
const bmiWeight = document.querySelector(".bmi-weight-input");
const bmiHeight = document.querySelector(".bmi-height-input");
const bmiBtn = document.querySelector(".bmi-btn-js");

const resultBmi = document.querySelector(".bmi-weight-js");
const resultComment = document.querySelector(".bmi-comment-js");
const resultDiv = document.querySelector(".bmi-result-div");

bmiBtn.addEventListener("click", () => {
  let weight = parseInt(bmiWeight.value);
  let height = parseFloat(bmiHeight.value);
  var bmi = weight / (height * height);
  if (bmi < 18.5) {
    resultDiv.style.background = "red";
    resultDiv.style.color = "White";
    resultBmi.innerHTML = bmi.toFixed(2);
    resultComment.innerHTML = "Under Weight";
  } else if (bmi >= 18.5 && bmi <= 24.9) {
    resultDiv.style.background = "green";
    resultDiv.style.color = "White";
    resultBmi.innerHTML = bmi.toFixed(2);
    resultComment.innerHTML = "Normal Weight";
  } else if (bmi >= 25 && bmi <= 29.9) {
    resultDiv.style.background = "red";
    resultDiv.style.color = "White";
    resultBmi.innerHTML = bmi.toFixed(2);
    resultComment.innerHTML = "Over Weight";
  } else if (bmi >= 30 && bmi <= 34.9) {
    resultDiv.style.background = "red";
    resultDiv.style.color = "White";
    resultBmi.innerHTML = bmi.toFixed(2);
    resultComment.innerHTML = "Obesity (Class I)";
  } else if (bmi >= 35 && bmi <= 39.9) {
    resultDiv.style.background = "red";
    resultDiv.style.color = "White";
    resultBmi.innerHTML = bmi.toFixed(2);
    resultComment.innerHTML = "Obesity (Class II)";
  }
});
