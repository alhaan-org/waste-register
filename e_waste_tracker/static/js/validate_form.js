window.addEventListener("DOMContentLoaded", () => {
  const username = document.getElementById("username");
  const emailField = document.getElementById("email");
  const password = document.getElementById("password");
  const confirmPassword = document.getElementById("confirmPassword");
  const phone = document.getElementById("phone");
  const cnicNo = document.getElementById("id-card");
  const err = document.getElementById("error");
  const errDiv = document.getElementById("errorDiv");

  const showError = (msg) => {
    err.textContent = msg;
    errDiv.classList.remove("d-none");
  };

  const clearError = () => {
    err.textContent = "";
    errDiv.classList.add("d-none");
  };

  const validateUserName = () => {
    const userPattern = /^[A-Za-z0-9_]+$/;
    const value = username.value.trim();

    if (!value) showError("Please add your username");
    else if (value.length > 20)
      showError("Username should not exceed 20 characters");
    else if (!userPattern.test(value))
      showError("Username can only contain letters, numbers, and underscores");
    else clearError();
  };

  const validateEmail = () => {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const value = emailField.value.trim();

    if (!value) showError("Please add your email");
    else if (!emailPattern.test(value)) showError("Please enter a valid email");
    else clearError();
  };

  const validatePassword = () => {
    const value = password.value.trim();

    if (!value) showError("Please add a password");
    else if (value.length < 8)
      showError("Password must be at least 8 characters long");
    else if (!/[A-Z]/.test(value) || !/[0-9]/.test(value))
      showError(
        "Password must contain at least one uppercase letter and number"
      );
    else clearError();
  };

  const validateConfirmPassword = () => {
    const value = confirmPassword.value.trim();

    if (!value) showError("Please confirm your password");
    else if (value !== password.value.trim())
      showError("Passwords do not match");
    else clearError();
  };

  const validateCnicNo = () => {
    const value = cnicNo.value.trim();
    const cnicPattern = /^\d{5}-\d{7}-\d{1}$/;

    if (!value) showError("Please enter your CNIC");
    else if (!cnicPattern.test(value))
      showError("Please enter valid CNIC with Dashes and 13 Digits");
    else if (value.length > 16) showError("Please enter 13 Digits with dashes");
    else clearError();
  };

  const validatePhoneNumber = () => {
    const value = phone.value.trim();
    const pattern = /^03\d{2}-\d{7}$/;

    if (!value) showError("Please enter phone number");
    else if (!pattern.test(value))
      showError("Please enter valid number with format 03XX-XXXXXXX");
    else clearError();
  };
  // add listeners
  username.addEventListener("input", validateUserName);
  emailField.addEventListener("input", validateEmail);
  password.addEventListener("input", validatePassword);
  confirmPassword.addEventListener("input", validateConfirmPassword);
  cnicNo.addEventListener("input", validateCnicNo);
  phone.addEventListener("input", validatePhoneNumber);
  // run initial validations
  validateCnicNo();
  validatePhoneNumber();
  validateConfirmPassword();
  validatePassword();
  validateEmail();
  validateUserName();
});
