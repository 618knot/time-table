def getPdf():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import chromedriver_binary
    from pathlib import Path
    import time
    remove("download/*")

    dldir_name = 'download'  # 保存先フォルダ名
    dldir_path = Path(dldir_name)
    dldir_path.mkdir(exist_ok=True)  # 存在していてもOKとする（エラーで止めない）
    download_dir = str(dldir_path.resolve())  # 絶対パス

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "plugins.always_open_pdf_externally": True
    })
    # (1)
    driver = webdriver.Chrome(options=options)
    # (2)
    driver.command_executor._commands["send_command"] = (
        "POST",
        '/session/$sessionId/chromium/send_command'
    )
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_dir
        }
    }

    driver.execute("send_command", params=params)
    driver.get("https://www.chitose.ac.jp/info/access")

    elements = driver.find_element(by=By.XPATH, value='//*[@id="paragraph_107_1615971519"]/div/div/div[1]/a')
    elements.click()
    time.sleep(5)

def remove(pathname, recursive = True):
    import glob
    import os
    for i in glob.glob(pathname, recursive=recursive):
        if os.path.isfile(i):
            os.remove(i)
