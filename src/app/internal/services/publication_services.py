from bs4 import BeautifulSoup

from app.internal.models.publication import Publication


def get_publication_fields(html_doc: str, publication_url: str) -> Publication:
    """
    Extracting header, author name, author url, publication text, datetime from habr.com publication

    :param html_doc: Html document
    :param publication_url: Publication url from which you extract header, author name, author url, publication text,
    datetime
    :return: Publication django model
    """
    soup = BeautifulSoup(html_doc, "html.parser")
    article_snippet_meta = soup.find("div", {"class": "tm-article-snippet__meta"})
    article_snippet_author_meta = article_snippet_meta.find(
        "span", {"class": "tm-user-info tm-article-snippet__author"}
    )
    article_snippet_author_user_info_meta = article_snippet_author_meta.find("a", {"class": "tm-user-info__username"})
    header = soup.h1.span.text
    datetime = article_snippet_meta.find("span", {"class": "tm-article-snippet__datetime-published"}).time.get(
        "datetime"
    )
    author_name = article_snippet_author_user_info_meta.text.strip()
    author_url = article_snippet_author_user_info_meta.get("href")
    text = get_publication_text(html_doc)
    return Publication(
        header=header, url=publication_url, author_name=author_name, author_url=author_url, text=text, datetime=datetime
    )


def get_publication_text(html_doc: str) -> str:
    """
    Extract text from habr.com publication

    :param html_doc: Html document
    :return: Publication text
    """
    soup = BeautifulSoup(html_doc, "html.parser")
    publication_text = soup.find("div", {"xmlns": "http://www.w3.org/1999/xhtml"})
    white_tag_list = ["h2", "p", "pre", "h1", "br"]
    text = "\n".join([x.text for x in publication_text.findAll(white_tag_list)])
    return text if len(text.strip()) != 0 else publication_text.get_text().strip()
