import undetected_chromedriver as webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from datetime import datetime
@pytest.fixture
def setup():
    #chrome_driver_path = "C:\\Drivers\\chromedriver-win64\\undetected_chromedriver.exe"
    options = Options()
    options.add_argument("--guest")
    options.add_argument("--disable-sync")
#    options.add_argument("--autoplay-policy=no-user-gesture-required")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    driver.close()

###########################Pytest HTML Report############

def pytest_html_report_title(report):
    report.title = "YT Music Web - Test Automation Report"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        f'<p><b>Project Name:</b> YT Music app</p>',
        f'<p><b>Module Name:</b> Login</p>',
        f'<p><b>Tester:</b> Ankur</p>'
        f'<p><b>Pytest Version:</b> {pytest.__version__}</p>'
        f'<p><b>Test Execution Time: </b> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>'
    ])


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)