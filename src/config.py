# Configuration settings for the news scraper

NEWS_SOURCES = ["technews", "udn_economy", "ltn_tech", "cw"]

TIMEZONE = "UTC"

GITHUB_SETTINGS = {
    "repo_name": "taiwan-news-scraper",
    "owner": "xuan540",
    "branch": "main"
}

NLP_SETTINGS = {
    "language": "zh_tw",
    "model": "bert-base-chinese"
}