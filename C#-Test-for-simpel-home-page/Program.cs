using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

class Program
{
    static void Main(string[] args)
    {
      IWebDriver driver = new ChromeDriver();
      driver.Url =("https://www.selenium.dev/documentation/webdriver/getting_started/first_script/");
      driver.Close();

    }
}
