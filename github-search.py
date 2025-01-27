import requests

GITHUB_API_URL = "https://api.github.com/search/repositories"

def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    # Example: "stars:>50000 language:python language:javascript"
    return query

def repos_with_most_stars(languages, sort="stars", order="desc", per_page=10):
    query = create_query(languages)
    params = {"q": query, "sort": sort, "order": order, "per_page": per_page}

    response = requests.get(GITHUB_API_URL, params=params)
    status_code = response.status_code
    
    if status_code != 200:
        body = response.json()
        raise RuntimeError(f"An error occurred. HTTP code: {status_code}. Response: ${body}")
    else:
        response_json = response.json()
        return response_json["items"]

def main():
    languages = ["python", "javascript"]
    repos = repos_with_most_stars(languages)

    for repo in repos:
        language = repo["language"]
        stars = repo["stargazers_count"]
        name = repo["name"]

        print(f"-> {name} [{language}] - ⭐ {stars}")

"""
Only runs if file is executed directly, not imported as a module.

How it works:
1. When Python runs a file directly, the special variable __name__ is set to "__main__"
2. When Python imports a file as a module, __name__ is set to the module's name
"""
if __name__ == "__main__":
    main()
