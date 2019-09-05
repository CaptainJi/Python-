from selenium import webdriver
import os

def insert_img(driver,filename):
    func_path=os.path.dirname(__file__)
    base_dir=os.path.dirname(func_path)
    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')

    base=base_dir.split('/Website')[0]
    print(base)
    filepath=base+'/Website/test_report/screenshot/'+filename
    driver.get_screenshot_as_file(filepath)


if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get('http://www.baidu.com')
    insert_img(driver,'baidu.png')
    driver.quit()