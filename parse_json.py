import requests

url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    products_dict = data['products']
    products_list = []
    for key, value in products_dict.items():
        product = value
        product['id'] = key
        products_list.append(product)

    sorted_products = sorted(products_list, key=lambda x: int(x['popularity']), reverse=True)

    for product in sorted_products:
        print(f"Title: {product['title']} - Price: {product['price']} - Popularity: {product['popularity']}")
else:
    print("Failed to fetch data.")
