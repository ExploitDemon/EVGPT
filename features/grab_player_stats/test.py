import pandas as pd
from bs4 import BeautifulSoup, Tag
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = "https://www.nba.com/stats/players/advanced?sort=W&dir=-1"

# Set up a headless browser
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

# Fetch the page
driver.get(url)

# Get the HTML content of the page
html_content = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find the table in the HTML
table = soup.find("table", attrs={"class": "Crom_table__p1iZz"})

# Check if table is not None and is of type Tag
if table and isinstance(table, Tag):
    # Get the headers of the table, including hidden ones
    headers = [
        header.text
        for header in table.find_all("th")
        if not header.has_attr("hidden")
    ]

    # Find all the rows in the table
    rows = table.find_all("tr")

    # Loop through each row and get the columns
    data = []
    for row in rows[1:]:  # Skip the first row as it's the header
        cols = row.find_all("td")
        row_data = [col.text.strip() for col in cols]
        # If there are fewer columns than headers, add placeholders
        while len(row_data) < len(headers):
            row_data.append("N/A")  # Placeholder for empty columns
        data.append(row_data)

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data, columns=headers)

    # Write the DataFrame to a CSV file
    df.to_csv("nba_player_stats.csv", index=False)
