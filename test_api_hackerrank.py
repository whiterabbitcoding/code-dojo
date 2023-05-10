import requests


def get_page_articles(page: int):
    page_request_url = "https://jsonmock.hackerrank.com/api/articles?page={}"
    return requests.get(page_request_url.format(page)).json()["data"]


def topArticles(limit):
    articles = requests.get("https://jsonmock.hackerrank.com/api/articles")
    total_pages = articles.json()["total_pages"]
    articles = []
    for i in range(0, int(total_pages)):
        page_articles = get_page_articles(i)

        page_articles_no_none_for_num_comments = [
            {k: 0 for k in d if k == "num_comments"} if d["num_comments"] == None else d
            for d in page_articles
        ]
        articles = articles + page_articles_no_none_for_num_comments
    print(articles[1:5])

    # Format articles by setting name based off title or story title,
    # if neither then remove
    new_objects = []
    for article in articles:
        name = None
        if "title" in article.keys():
            name = article["title"]
        else:
            if "story_title" in article.keys():
                name = article["story_title"]

        if name is None:
            continue
        else:
            new_objects.append({"name": name, "num_comments": article["num_comments"]})

    # need to fix sorting here
    alph_sorted_articles = sorted(new_objects, key=lambda d: d["name"], reverse=True)
    otuput_sorted_articles = sorted(
        alph_sorted_articles, key=lambda d: d["num_comments"], reverse=True
    )

    return [article["name"] for article in otuput_sorted_articles[:limit]]
