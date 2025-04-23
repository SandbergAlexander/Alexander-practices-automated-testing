using OpenQA.Selenium;
using OpenQA.Selenium.BiDi;
using OpenQA.Selenium.Chrome;

class Program
{
    static void Main(string[] args)
    {
      IWebDriver driver = new ChromeDriver();
      driver.Url =("http://127.0.0.1:5500/test-app-or-home-page/simpel-home-page/index.html");
      Thread.Sleep(1000);
      driver.FindElement(By.XPath("/html/body/header/a")).Click();
      Thread.Sleep(1000);
      driver.Close();

    }
}
