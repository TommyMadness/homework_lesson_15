import pytest
from selene import have, browser


@pytest.mark.parametrize("desktop_resolution", [(1920, 1080)], indirect=True)
def test_github_signin_desktop(desktop_resolution):
    browser.all("button").element_by(have.text("Sign up")).click()


@pytest.mark.parametrize("mobile_resolution", [(375, 812)], indirect=True)
def test_github_signin_mobile(mobile_resolution):
    browser.element(".Button-content").click()
    browser.all(".HeaderMenu-button").element_by(have.text("Sign up")).click()
