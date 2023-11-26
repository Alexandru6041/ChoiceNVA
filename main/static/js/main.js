import CookieController from "./utils/CookieManager.js";

const cookie_expire = 291443;
const CookieManager = new CookieController();

const has_submitted = CookieManager.getCookie("submitted");
console.log("has_submitted: ", has_submitted);
if(has_submitted == 1)
{
    const submit_button = document.getElementById("submit_button");
    submit_button.disabled = true;
    submit_button.innerHTML = "You have already submitted this form.";
    console.log("You have already submitted this form.");
}
