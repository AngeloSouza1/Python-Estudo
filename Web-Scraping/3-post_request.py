import requests

new_data = {
    "userID": 1,
    "id": 1,
    "title": "Aprendendo Python",
    "body": "Manipulando informações em API com Requests."
}

# The API endpoint to communicate with
url_post = "https://jsonplaceholder.typicode.com/posts"

# A POST request to tthe API
post_response = requests.post(url_post, json=new_data)

print(post_response.status_code)

# Print the response
post_response_json = post_response.json()
print(post_response_json)