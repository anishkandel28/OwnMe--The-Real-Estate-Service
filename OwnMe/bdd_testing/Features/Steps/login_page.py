from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bdd_testing.Pages.LandingPage import LandingPage
from bdd_testing.Pages.LoginPage import LoginPage
from bdd_testing.Utilities.customLogger import LogGen
from bdd_testing.Utilities.readproperty import ReadConfig
import time

baseURL = ReadConfig.getURL()
mylogger = LogGen.loggen()


@given(u'Launch the App')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylogger.info("*****Driver Initialised*****")
    context.driver.get(baseURL)
    mylogger.info("*****Browser launched*****")


@when(u'enter login credentials')
def step_impl(context):
    mylogger.info("*****Passing credential******")
    global landingpage
    global loginpage
    landingpage = LandingPage(context.driver)
    landingpage.clickOnLogin()
    loginpage = LoginPage(context.driver)
    user = ReadConfig.getUserName()
    pwd = ReadConfig.getPassword()
    time.sleep(3)
    loginpage.setusername(user)
    loginpage.setpassword(pwd)
    mylogger.info ("*****Entered credential*****")




@then(u'click login')
def step_impl(context):
    loginpage.clickOnLogin()
    mylogger.info("*****Login button clicked*******")


@then(u'close the App')
def step_impl(context):
    context.driver.close()
    mylogger.info("******Browser Closed*****")
