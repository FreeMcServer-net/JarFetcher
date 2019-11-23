import os
import requests

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
def versiontuple(v):
    return tuple(map(int, (v.split("."))))


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chrome_options)
driverDownload = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chrome_options)
# driver.get('https://getbukkit.org/download/craftbukkit')
# for version in driver.find_elements_by_class_name("download-pane"):
#     versionName = version.find_element_by_tag_name("h2").text
#     versionSize = version.find_element_by_tag_name("h3").text
#     versionLink = version.find_element_by_tag_name("a").get_attribute('href')
#     if versiontuple(versionName) < versiontuple("1.5.2"):
#         continue;
#     driverDownload.get(versionLink)
#     versionLinkReal = driverDownload.find_element_by_class_name("well").find_element_by_tag_name("a").get_attribute(
#         'href')
#     targetFileName = "craftbukkit-%s.jar" % versionName
#     print("Downloading CraftBukkit %s, %sMB with filename %s" % (versionName, versionSize, targetFileName))
#     r = requests.get(versionLinkReal, allow_redirects=True)
#     open('downloads/jar/stable/craftbukkit/%s' % targetFileName, 'wb').write(r.content)
#     print("-------------------")
driver.get('https://getbukkit.org/download/spigot')
for version in driver.find_elements_by_class_name("download-pane"):
    versionName = version.find_element_by_tag_name("h2").text
    versionSize = version.find_element_by_tag_name("h3").text
    versionLink = version.find_element_by_tag_name("a").get_attribute('href')
    if versiontuple(versionName) < versiontuple("1.5.2"):
        continue;
    driverDownload.get(versionLink)
    versionLinkReal = driverDownload.find_element_by_class_name("well").find_element_by_tag_name("a").get_attribute(
        'href')
    targetFileName = "spigot-%s.jar" % versionName
    print("Downloading Spigot %s, %sMB with filename %s" % (versionName, versionSize, targetFileName))
    r = requests.get(versionLinkReal, allow_redirects=True)
    open('downloads/jar/stable/spigot/%s' % targetFileName, 'wb').write(r.content)
    print("-------------------")
# driver.get('https://getbukkit.org/download/vanilla')
# for version in driver.find_elements_by_class_name("download-pane"):
#     versionName = version.find_element_by_tag_name("h2").text
#     versionSize = version.find_element_by_tag_name("h3").text
#     versionLink = version.find_element_by_tag_name("a").get_attribute('href')
#     if versiontuple(versionName) < versiontuple("1.5.2"):
#         continue;
#     driverDownload.get(versionLink)
#     versionLinkReal = driverDownload.find_element_by_class_name("well").find_element_by_tag_name("a").get_attribute(
#         'href')
#     targetFileName = "vanilla-%s.jar" % versionName
#     print("Downloading Vanilla %s, %sMB with filename %s" % (versionName, versionSize, targetFileName))
#     r = requests.get(versionLinkReal, allow_redirects=True)
#     open('downloads/jar/stable/vanilla/%s' % targetFileName, 'wb').write(r.content)
#     print("-------------------")


