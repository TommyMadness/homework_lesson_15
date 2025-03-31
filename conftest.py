import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080)])
def desktop_resolution(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    browser.open("https://github.com")
    yield
    browser.quit()


@pytest.fixture(params=[(375, 812)])
def mobile_resolution(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    browser.open("https://github.com")
    yield
    browser.quit()


@pytest.fixture(params=[(1920, 1080), (375, 812)])
def setup_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    browser.open("https://github.com")

    if width >= 1012:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()
