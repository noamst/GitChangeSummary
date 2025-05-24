import requests

def test_api_with_git_diff():
    # Example git diff
    git_diff = """
    diff --git a/example.py b/example.py
    index 83db48f..bf3e3c6 100644
    --- a/example.py
    +++ b/example.py
    @@ -1,4 +1,4 @@
    -print("Hello, World!")
    +print("Hello, Universe!")
    """

    # API endpoint
    api_url = "http://localhost:8000/summarize"

    # Payload for the API
    payload = {
        "commit_hash": "abc123",
        "diff": git_diff
    }

    # Make a POST request to the API
    response = requests.post(api_url, json=payload)

    # Check the response
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    result = response.json()
    print("API Response:", result)

    # Add additional assertions based on expected API behavior
    assert "summary" in result, "Response should contain a 'summary' field"
    assert "Hello, Universe!" in result["summary"], "Summary should include the updated content"

# Run the test function
if __name__ == "__main__":
    test_api_with_git_diff()