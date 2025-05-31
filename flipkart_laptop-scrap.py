
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import matplotlib.pyplot as plt
# import seaborn as sns

# # ---------------------------------------------
# # Step 1: Setup
# num_pages = 3
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
#     "Accept-Language": "en-US,en;q=0.9",
#     "Accept-Encoding": "gzip, deflate, br",
#     "DNT": "1",
#     "Connection": "keep-alive"
# }
# all_products = []

# # ---------------------------------------------
# # Step 2: Scrape Data
# for page in range(1, num_pages + 1):
#     print(f"Scraping Page {page}...")
#     url = f"https://www.flipkart.com/search?q=laptops&page={page}"
#     response = requests.get(url, headers=headers)

#     if response.status_code != 200:
#         print(f"Failed to retrieve Page {page}")
#         continue

#     soup = BeautifulSoup(response.content, "html.parser")
#     containers = soup.find_all("div", class_="_1AtVbE col-12-12")

#     for item in containers:
#         name = item.find("div", class_="_4rR01T")
#         price = item.find("div", class_="_30jeq3 _1_WHN1")
#         rating = item.find("div", class_="_3LWZlK")
#         link_tag = item.find("a", class_="_1fQZEK")

#         if name and price:
#             full_name = name.text.strip()
#             brand = full_name.split()[0]  # First word = brand
#             clean_price = price.text.strip()
#             clean_rating = rating.text.strip() if rating else "No Rating"
#             product_link = "https://www.flipkart.com" + link_tag['href'] if link_tag else "No Link"

#             all_products.append([
#                 full_name, brand, clean_price, clean_rating, product_link
#             ])

#     time.sleep(2)

# # ---------------------------------------------
# # Step 3: Convert to DataFrame
# df = pd.DataFrame(all_products, columns=["Product Name", "Brand", "Price", "Rating", "Link"])

# # Step 4: Clean Data
# df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
# df["Price"] = df["Price"].str.replace("₹", "").str.replace(",", "").astype(int)

# # ---------------------------------------------
# # Step 5: Save CSV
# df.to_csv("flipkart_laptops_full.csv", index=False, encoding="utf-8")
# print("\n✅ Data saved to 'flipkart_laptops_full.csv'")

# # ---------------------------------------------
# # Step 6: Filter - Top 5 Cheapest Laptops
# print("\n💸 Top 5 Cheapest Laptops:")
# print(df.sort_values(by="Price").head(5)[["Product Name", "Brand", "Price", "Rating"]])

# # ---------------------------------------------
# # Step 7: Highlight Highest Rated Laptop
# highest_rated = df[df["Rating"] == df["Rating"].max()]
# print("\n🌟 Highest Rated Laptop(s):")
# print(highest_rated[["Product Name", "Brand", "Price", "Rating"]])

# # ---------------------------------------------
# # Step 8: Visualization

# # Rating Distribution
# plt.figure(figsize=(8, 5))
# sns.countplot(x='Rating', data=df)
# plt.title("Rating Distribution of Laptops")
# plt.xlabel("Rating")
# plt.ylabel("Number of Products")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Price vs Rating
# plt.figure(figsize=(8, 5))
# sns.scatterplot(x='Rating', y='Price', data=df, hue='Brand', palette='Set2')
# plt.title("Laptop Price vs Rating")
# plt.xlabel("Rating")
# plt.ylabel("Price (₹)")
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.tight_layout()
# plt.show()

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
# Flipkart Laptop Scraper
# ---------------------------------------------
# Step 1: Setup
num_pages = 1
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Accept-Language": "en-US,en;q=0.9",
}
all_products = []

# ---------------------------------------------
# Step 2: Scrape Data
for page in range(1, num_pages + 1):
    print(f"Scraping Page {page}...")
    url = f"https://www.flipkart.com/search?q=laptops&page={page}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve Page {page}")
        continue

    soup = BeautifulSoup(response.content, "html.parser")
    containers = soup.find_all("div", class_="cPHDOP col-12-12")

    for item in containers:
        try:
            name = item.find("div", class_="KzDlHZ")
            price = item.find("div", class_="Nx9bqj _4b5DiR")
            rating = item.find("div", class_="XQDdHH")
            link_tag = item.find("a", class_="CGtC98")
          

            if name and price:
                full_name = name.get_text(strip=True)
                brand = full_name.split()[0]
                clean_price = price.get_text(strip=True).replace("₹", "").replace(",", "")
                clean_rating = rating.get_text(strip=True) if rating else "No Rating"
                product_link = "https://www.flipkart.com" + link_tag['href'] if link_tag else "No Link"

                all_products.append({
                    "Product Name": full_name,
                    "Brand": brand,
                    "Price (INR)": clean_price,
                    "Rating": clean_rating,
                    "Product Link": product_link
                })
                print(all_products)

        except Exception as e:
            print(f"Error parsing product: {e}")
            continue

    time.sleep(4)

# ---------------------------------------------
# Step 3: Save to CSV

print(all_products)
df = pd.DataFrame(all_products)
df.to_csv("flipkart_laptops.csv", index=False, encoding='utf-8-sig')
print("Data saved to flipkart_laptops.csv")

