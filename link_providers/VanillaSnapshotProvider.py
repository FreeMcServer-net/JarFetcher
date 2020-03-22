links = {}


# noinspection DuplicatedCode
def get():
    import selenium.webdriver as webdriver
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chrome_options)
    driver.get('https://mcversions.net/')
    from datetime import datetime, timedelta
    date_limit = datetime.utcnow() - timedelta(days=30)
    try:
        print('lalala')
        for version in driver.find_element_by_xpath(
                '/html/body/main/div/div[2]/div[2]/div').find_elements_by_tag_name('div'):
            version_name = version.find_element_by_class_name('info').find_elements_by_tag_name("p").text
            print(version_name)
            # version_name = str(version_name).replace('-', '_')
            # version_date = datetime.strptime(version.find_element_by_class_name("time").text, '%m/%d/%y')
            #
            # version_link = version.find_element_by_class_name("server").get_attribute('href')
            # import Storage
            # if version_date < date_limit:
            #     continue
            #
            # target_file_name = "vanila-%s-snapshot.jar" % version_name
            # Storage.logger.info(f'Found download link for Vanilla Snapshot {version_name}: {version_link}')
            # links[target_file_name] = version_link
    except:
        pass
    return links
