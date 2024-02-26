"""
Simulate the consumption of a paged API, 
where each "page" of data is processed in a loop until there are no more pages.
"""

actual_page = 1
num_pages = 5

while actual_page <= num_pages:
    print(f"Processing page {actual_page} of {num_pages}.")
    actual_page += 1

print("All pages were processed.")