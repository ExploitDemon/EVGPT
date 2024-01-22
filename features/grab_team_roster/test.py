import pandas as pd
from bs4 import BeautifulSoup, Tag
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from teams import teams

url = f"https://www.nba.com/stats/team/{teams.miami_heat.id}"

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

# Define the desired headers
desired_headers = [
    "Player",
    "No.",
    "Pos",
    "Height",
    "Weight",
    "Birthdate",
    "Age",
    "Exp",
    "School",
    "How Acquired",
]

# Check if table is not None and is of type Tag
if table and isinstance(table, Tag):
    # Find all the rows in the table
    rows = table.find_all("tr")

    # Loop through each row and get the columns, starting from the second row
    data = []
    for row in rows[
        1:
    ]:  # Skip the first two rows as the first is the title and
        # the second is the header
        cols = row.find_all("td")
        row_data = [col.text.strip() for col in cols]
        # Ensure the row data matches the length of desired headers
        row_data = row_data[: len(desired_headers)]
        data.append(row_data)

    # Create a pandas DataFrame from the data using the desired headers
    df = pd.DataFrame(data, columns=desired_headers)
    df = df.iloc[1:]  # This will drop the first row of the DataFrame

    # Write the DataFrame to a CSV file
    team_name = str(teams.miami_heat.name)

    team_name = team_name.replace(" ", "_").lower()
    df.to_csv(f"{team_name}.csv", index=False)
