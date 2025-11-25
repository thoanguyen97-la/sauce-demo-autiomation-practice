🧪 **SauceDemo Automation Testing – Python Selenium + Pytest + POM**

Một framework Automation Test được xây dựng bằng Python + Selenium + Pytest, áp dụng Page Object Model (POM) để kiểm thử website:
👉 https://www.saucedemo.com/

*Framework này được thiết kế, tập trung vào:*

  Clean Code
  
  Reusability
  
  Maintainability
  
  Type Safety
  
  Pytest Fixtures
  
  POM Practices

**🚀 Tech Stack**
    Component	Version
    Python	3.10+
    Selenium	4.x
    Pytest	7.x
    ChromeDriverManager	latest
    Page Object Model (POM)	✔
    WebDriverWait (Explicit Wait)	✔

**🏗 Features Covered**


✔ Login

    Login thành công
    
    Login với sai username

    Login với sai password

    Hiển thị error message

✔ Inventory Page

    Verify redirect sau khi login
    
    Kiểm tra hiển thị danh sách sản phẩm
    
    Add to cart
    
    Verify cart count

✔ Framework Features

    BasePage cho common actions
    
    Locator type safety (Tuple[str, str])
    
    Custom Exception: ElementNotFound
    
    Global WebDriver Fixture

Parallel execution (ready)

Pytest markers & configuration
