from selenium import webdriver
import xlrd
import pdb
import openpyxl
from xlwt import Workbook
# import
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pynput.keyboard import Key, Controller


def start():
    driver = webdriver.Chrome(executable_path='chromedriver_win32//chromedriver.exe')
    driver.maximize_window()
    return driver


def start_minize():
    driver = webdriver.Chrome(executable_path='chromedriver_win32//chromedriver.exe')
    driver.minimize_window()
    return driver
