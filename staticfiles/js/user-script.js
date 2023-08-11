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
