const usernameField = document.querySelector("#usernameField");

usernameField.addEventListener("keyup", (e) => {
  const usernameVal = e.target.value;
  console.log('usernameVal', usernameVal);
})
