links = {}


# noinspection DuplicatedCode
def get():
    import selenium.webdriver as webdriver
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chrome_options)
    driver_download = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chrome_options)
    driver.get('https://getbukkit.org/download/vanilla')
    for version in driver.find_elements_by_class_name("download-pane"):
        version_name = version.find_element_by_tag_name("h2").text
        version_size = version.find_element_by_tag_name("h3").text
        version_link = version.find_element_by_tag_name("a").get_attribute('href')
        import Storage
        if Storage.versiontuple(version_name) < Storage.versiontuple("1.5.2"):
            continue

        driver_download.get(version_link)
        version_link_real = driver_download.find_element_by_class_name("well").find_element_by_tag_name("a") \
            .get_attribute('href')
        target_file_name = "vanila-%s.jar" % version_name
        Storage.logger.info(f'Found download link for Vanilla {version} with {version_size}: {version_link_real}')
        links[target_file_name] = version_link_real
    return links
