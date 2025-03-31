import pytest
from selene import browser, query, have


@pytest.mark.parametrize(
    "setup_browser",
    [(1920, 1080), (375, 812)],
    ids=["desktop_1920x1080", "mobile_375x812"],
    indirect=True,
)
def test_mobile_skip(setup_browser):
    if setup_browser == "mobile":
        pytest.skip("Мобильный режим — не для десктопного теста")
    browser.all("button").element_by(have.text("Sign up")).click()


@pytest.mark.parametrize(
    "setup_browser",
    [(1920, 1080), (375, 812)],
    ids=["desktop_1920x1080", "mobile_375x812"],
    indirect=True,
)
def test_desktop_skip(setup_browser):
    if setup_browser == "desktop":
        pytest.skip("Десктопный режим — не для мобильного теста")
    browser.element(".Button-content").click()
    browser.all(".HeaderMenu-button").element_by(have.text("Sign up")).click()
