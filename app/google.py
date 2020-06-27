from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-setuid-sandbox")

chromeOptions.add_argument("--remote-debugging-port=9222")  # this
chromeOptions.add_argument("--window-size=1024x768")
chromeOptions.add_argument("disable-infobars")
chromeOptions.add_argument("--headless")


driver = webdriver.Chrome(chrome_options=chromeOptions)


def ask_google(query):
    # Search for query
    query = query.replace(" ", "+")
    driver.get("http://www.google.com/search?q=define+" + query)

    xpaths = [
        '//*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[1]/div/span/span',
        '//*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[2]/div/span/span',
    ]

    for xpath in xpaths:
        try:
            answer = "\n" + driver.find_element_by_xpath(xpath).text
            return answer
        except:
            pass

    return None
