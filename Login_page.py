from browser_helper import login


if __name__ == "__main__":
    browser = login("https://qa-agent-admin-ui.alphaatlus.com/")
    browser.open()
    browser.fill_email_and_submit("rsatti@alphaprotemps.com")
    browser.fill_password_and_sign_in("SRNR@27265")
    browser.stay_open()
