import { CookieController } from "./utils/CookieManager.js";

const cookie_expire = 291443;

const CookieManager = new CookieController();
CookieManager.setCookie("submitted", 1, cookie_expire);