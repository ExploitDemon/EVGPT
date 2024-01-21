import pandas as pd
from bs4 import BeautifulSoup, Tag
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

url = "https://www.nba.com/stats/players/advanced?sort=W&dir=-1"

# Set up a headless browser
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

# Fetch the page
driver.get(url)

data = []
headers = []

for i in range(0, 10):
    # Wait for the DOM to load and for the table to be present
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located(
            (By.CSS_SELECTOR, "table.Crom_table__p1iZz")
        )
    )

    # Get the HTML content of the page
    html_content = driver.page_source

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the table in the HTML
    table = soup.find("table", attrs={"class": "Crom_table__p1iZz"})

    # Check if table is not None and is of type Tag
    if table and isinstance(table, Tag):
        # Get the headers of the table, including hidden ones
        if not headers:  # Only get headers once
            headers = [
                header.text
                for header in table.find_all("th")
                if not header.has_attr("hidden")
            ]

        # Find all the rows in the table
        rows = table.find_all("tr")

        # Loop through each row and get the columns
        for row in rows[1:]:  # Skip the first row as it's the header
            cols = row.find_all("td")
            row_data = [col.text.strip() for col in cols]
            # If there are fewer columns than headers, add placeholders
            while len(row_data) < len(headers):
                row_data.append("N/A")  # Placeholder for empty columns
            data.append(row_data)

    # Wait for the 'Next Page' button to be clickable and then click it
    next_button_xpath = (
        "/html[1]/body[1]/div[1]/div[2]/div[2]/div["
        "3]/section[2]/div[1]/div[2]/div[2]/div[1]/div["
        "5]/button[2]"
    )
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, next_button_xpath))
    )
    next_button = driver.find_element(By.XPATH, next_button_xpath)
    next_button.click()

    # Wait for the next page to load by checking the presence of the table
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located(
            (By.CSS_SELECTOR, "table.Crom_table__p1iZz")
        )
    )

# Close the browser
driver.quit()

# Create a pandas DataFrame from the data
df = pd.DataFrame(data, columns=headers)

# Write the DataFrame to a CSV file
df.to_csv("nba_player_stats.csv", index=False)
