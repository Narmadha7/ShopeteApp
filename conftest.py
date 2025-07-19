import pytest

from BasePage.DriverPage import DriverPage


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser name")


def pytest_configure(config):
    pytest.browser = config.getoption("browser")


@pytest.fixture(scope="class")
def selenium_driver(request):
    driver_obj = DriverPage()
    driver = driver_obj.set_driver_details()
    request.cls.driver = driver
    print("driver started...")
    driver.get("https://rahulshettyacademy.com/angularpractice/#")
    driver.maximize_window()
    yield
    driver.close()
    del driver_obj
    print("driver killed...")

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra

#
# def _capture_screenshot(name):
#         driver.get_screenshot_as_file(name)
