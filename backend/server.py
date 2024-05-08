from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/categories/<categoryname>/products')
def get_category_products(categoryname):
    company_name = "AMZ"  # Company name is fixed  we can alter the company name here , Due to so many issues I have hardcoded it
    url = f'http://20.244.56.144/test/companies/{company_name}/categories/{categoryname}/products'
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE1MTY5MzgxLCJpYXQiOjE3MTUxNjkwODEsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6Ijk1YjdkYjFmLTE5MjItNGRlYi05NDg3LWUxZjE0ZTk0MDg4ZiIsInN1YiI6Imd1c2VsdmFyYWFubmkyNEBnbWFpbC5jb20ifSwiY29tcGFueU5hbWUiOiJQU05BIGNvbGxlZ2Ugb2YgRW5naW5lZXJpbmcgYW5kIFRlY2hub2xvZ3kiLCJjbGllbnRJRCI6Ijk1YjdkYjFmLTE5MjItNGRlYi05NDg3LWUxZjE0ZTk0MDg4ZiIsImNsaWVudFNlY3JldCI6InJHTm9TQkF5bm1ncmplVmoiLCJvd25lck5hbWUiOiJTZWx2YSBSYWFubmkgR3UiLCJvd25lckVtYWlsIjoiZ3VzZWx2YXJhYW5uaTI0QGdtYWlsLmNvbSIsInJvbGxObyI6IjEifQ.RuJiE-ny6f2eA3EI4CBgrR8E0yx_v0-32x-JCLcpB2s"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    params = {
        'top': '10',
        'minPrice': '1',
        'maxPrice': '10000'
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return jsonify(data)

@app.route('/categories/<categoryname>/products/<int:index>')
def get_product_by_index(categoryname, index):
    company_name = "AMZ"  # Company name is fixed we can alter the company name here 
    url = f'http://20.244.56.144/test/companies/{company_name}/categories/{categoryname}/products'
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE1MTY5MzgxLCJpYXQiOjE3MTUxNjkwODEsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6Ijk1YjdkYjFmLTE5MjItNGRlYi05NDg3LWUxZjE0ZTk0MDg4ZiIsInN1YiI6Imd1c2VsdmFyYWFubmkyNEBnbWFpbC5jb20ifSwiY29tcGFueU5hbWUiOiJQU05BIGNvbGxlZ2Ugb2YgRW5naW5lZXJpbmcgYW5kIFRlY2hub2xvZ3kiLCJjbGllbnRJRCI6Ijk1YjdkYjFmLTE5MjItNGRlYi05NDg3LWUxZjE0ZTk0MDg4ZiIsImNsaWVudFNlY3JldCI6InJHTm9TQkF5bm1ncmplVmoiLCJvd25lck5hbWUiOiJTZWx2YSBSYWFubmkgR3UiLCJvd25lckVtYWlsIjoiZ3VzZWx2YXJhYW5uaTI0QGdtYWlsLmNvbSIsInJvbGxObyI6IjEifQ.RuJiE-ny6f2eA3EI4CBgrR8E0yx_v0-32x-JCLcpB2s"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    params = {
        'top': '10',
        'minPrice': '1',
        'maxPrice': '10000'
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if 0 <= index < len(data):
        product = data[index]
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
