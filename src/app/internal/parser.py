import concurrent.futures as pool
from urllib.parse import urljoin
from typing import Tuple

import requests

from app.internal.models.hub import Hub
from app.internal.models.publication import Publication
from app.internal.services.hub_services import get_urls
from app.internal.services.publication_services import get_publication_fields
from config.celery import app

HUBR = "https://habr.com/"


def fetch(url: str) -> Tuple[str, str]:
    """
    Fetch html document

    :param url: Url
    :return: Tuple of html document and url
    """
    return requests.get(url).content.decode("utf-8"), url


@app.task
def start_parser(hub_id: int) -> None:
    """
    Start hub parser

    :param hub_id: Hub id from DB
    """
    exists_urls = {p.url for p in Publication.objects.all()}
    hub = Hub.objects.get(id=hub_id)
    html_doc = requests.get(hub.url).content.decode("utf-8")
    urls = list({urljoin(HUBR, url) for url in get_urls(html_doc)}.difference(exists_urls))
    with pool.ThreadPoolExecutor(100) as executor:
        publications = [get_publication_fields(html, url) for html, url in executor.map(fetch, urls)]
        for publication in publications:
            print(publication)
            publication.hub = hub
            publication.save()
