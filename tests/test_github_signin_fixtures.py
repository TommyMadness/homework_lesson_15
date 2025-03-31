from selene import have, browser


def test_github_sign_in_desktop(desktop_resolution):
    browser.all("button").element_by(have.text("Sign up")).click()


def test_github_sign_in_mobile(mobile_resolution):
    browser.element(".Button-content").click()
    browser.all(".HeaderMenu-button").element_by(have.text("Sign up")).click()
