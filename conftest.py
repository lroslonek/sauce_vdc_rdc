import pytest

username = 'xxx'
access_key = 'xxx'
selenium_endpoint = "https://{}:{}@ondemand.us-west-1.saucelabs.com/wd/hub".format(username, access_key)

@pytest.fixture
def desktop_web_driver(request):
    test_name = request.node.name
    build_tag = 'build 666 vdc'  # datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")

    caps = {
        'platformName': 'Windows 10',
        'browserName': 'Chrome',
        'platformVersion': 'latest-1',
        'sauce:options': {
            'build': build_tag,
            'name': 'VDC ' + test_name,
            'extendedDebugging': True,
            'capturePerformance': True
        }
    }

    from selenium import webdriver
    browser = webdriver.Remote(
        command_executor=selenium_endpoint,
        desired_capabilities=caps,
        keep_alive=True
    )
    yield browser
    browser.quit()


@pytest.fixture
def mobile_rdc_driver(request):
    test_name = request.node.name
    build_tag = 'build 666 rdc'  # datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")

    caps = {
        'browserName': 'Chrome',
        # 'deviceName': 'Samsung Galaxy A80',
        # 'platformVersion': '10',
        'platformName': 'Android',
        'phoneOnly': True,
        'build': build_tag,
        'name': 'RDC ' + test_name,
    }

    from appium import webdriver
    browser = webdriver.Remote(selenium_endpoint, caps)
    yield browser
    browser.quit()
