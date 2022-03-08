from typing import List

from bs4 import BeautifulSoup


def get_urls(html_doc: str) -> List:
    """
    Get urls from habr.com

    :param html_doc: Html document
    :return: List of urls
    """
    soup = BeautifulSoup(html_doc, "html.parser")
    urls = [x.get("href") for x in soup.findAll("a", {"class": "tm-article-snippet__title-link"})]
    return urls
