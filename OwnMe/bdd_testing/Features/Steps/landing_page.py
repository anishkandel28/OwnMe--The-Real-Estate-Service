from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bdd_testing.Utilities.customLogger import LogGen
from bdd_testing.Utilities.readproperty import ReadConfig

baseURL = ReadConfig.getURL()
mylogger = LogGen.loggen()

@given(u'Launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylogger.info("*****Driver Initialised*****")
    context.driver.get(baseURL)
    mylogger.info("*****Browser launched*****")


@then(u'verify the page title')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = "Ownme"
    if actual_title == expected_title:
        assert True
        mylogger.info("*****Title matched*****")
    else:
        mylogger.info("*****Title not matched*****")
        assert False


@then(u'close the browser')
def step_impl(context):
    context.driver.close()
    mylogger.info("******Browser Closed*****")