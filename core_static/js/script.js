const menuBtn = document.querySelector(".hamburger-menu-icon");
const navigationBar = document.querySelector(".navigation");

menuBtn.addEventListener("click", () => {
  const dataVisible = navigationBar.getAttribute("data-visible");
  if (dataVisible == "true") {
    navigationBar.setAttribute("data-visible", "false");
  } else if (dataVisible == "false") {
    navigationBar.setAttribute("data-visible", "true");
  }
  //   console.log(dataVisible);
});

const signIn = document.querySelector(".login-btn-popup");
const optionBox = document.querySelector(".login-options-for-user");
const closeOptionBox = document.querySelector(".clos-btn-xxx");

const patientBtn = document.querySelector(".login-as-patient");
const doctorBtn = document.querySelector(".login-as-doctor");

const loginFormPatient = document.querySelector(".login-form-patient-modal");
const loginFormDoctor = document.querySelector(".login-form-doctor-modal");
const signUpForm = document.querySelector(".sign-up-form-modal");
const signUp = document.querySelector(".sign-up-btn");

const loginCloseBtn = document.querySelector(".login-form-close-btn");
const loginCloseBtnDoctor = document.querySelector(
  ".login-form-close-btn-doctor"
);
const signUpCloseBtn = document.querySelector(".sign-up-form-close-btn");

signIn.addEventListener("click", () => {
  optionBox.showModal();
  // loginForm.showModal();
});

closeOptionBox.addEventListener("click", () => {
  optionBox.close();
});

patientBtn.addEventListener("click", () => {
  optionBox.close();
  loginFormPatient.showModal();
});

doctorBtn.addEventListener("click", () => {
  optionBox.close();
  loginFormDoctor.showModal();
});

loginCloseBtn.addEventListener("click", () => {
  loginFormPatient.close();
});

loginCloseBtnDoctor.addEventListener("click", () => {
  loginFormDoctor.close();
});

signUp.addEventListener("click", () => {
  signUpForm.showModal();
});

signUpCloseBtn.addEventListener("click", () => {
  signUpForm.close();
});
