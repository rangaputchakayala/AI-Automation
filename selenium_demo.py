from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main():
    workspace_dir = Path.cwd()
    print("Using current folder:", workspace_dir)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    try:
        driver.maximize_window()
        driver.get("https://qa-agent-admin-ui.alphaatlus.com/")
        print("Title:", driver.title)
        print("Page loaded successfully.")
        driver.find_element(By.TAG_NAME, "body")

        output_file = workspace_dir / "selenium_result.txt"
        output_file.write_text(f"Title: {driver.title}\nURL: https://qa-agent-admin-ui.alphaatlus.com/\n", encoding="utf-8")
        print("Saved result to:", output_file)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
