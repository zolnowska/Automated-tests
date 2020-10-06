# Automated-tests
Examples of automated tests of Presta Shop 1.7.5.0. in Python 3.8 and Framework Selenium for Browser Google Chrome 

#Requirements:
* Windows 10 
* Google Chrome version 85.0
* Firefox 81.0
* PrestaShop version 1.7.5.0 on localhost with PHP version 5.6-7.2 and shop named "Prestashop" also english choosed
 as language front-end of shop
* Folder with name "webdriver" in folder of Project "Automated-tests" and pasted there downloaded chromedriver.exe 
and geckodriver.exe v0.27.0
* Python 3.8 
* Install used packages in project by the command "pip install -r requirements.txt"
* Created user in shop "Prestashop" with data: First name: "Test", Last Name: "Test", Email: "test@test.test",  
Password: "test1" (the rest of the data isn't important) 

#How to run tests
* Go to folder "tests" and run tests by the command "py.test"

#Information about code
* Code of function move_to_element in lib.pages.base.Base() is more developed that classic move_to_element from action chain 
because for geckodriver.exe it made problem when element wasn't in the viewport  
* Code of function get_selected_paper_type_squarred in lib.pages.product_page.ProductPage() is more developed that classic 
function in this code to get a text because website refresh after change paper type in Product Page and this code let to 
to handle an unexpected exception


