from bs4 import BeautifulSoup
import requests as r
from core.models import Node, Graph

_pages = set()
_titles = set()
_num_of_links = 0
_depth = 0
_graph = None

map = {}

def scrape(graph_name, wiki_link, depth, num_of_links):
    global _pages, _num_of_links, _depth, _graph, _titles
    _pages = set()
    _titles = set()
    _depth = int(depth)
    _num_of_links = int(num_of_links)

    _pages.add(wiki_link)
    _graph = Graph(name=graph_name)
    _graph.save()
    print(depth, num_of_links)
    scrape_node(None, wiki_link, 0)
    print(_graph)


def scrape_node(parent, child, lvl):
    global _pages, _num_of_links, _depth, _graph, _titles
    if lvl > _depth:
        return
    soup = make_soup_from_page(child)

    title = soup.title.string.replace(" - Wikipedia", "")
    if title in _titles:
        link_with_parent(title, parent)
        return
    _titles.add(title)

    description = add_description(soup)

    # all_links = soup.find_all('a')
    all_links = soup.select('p a')
    node = Node(atributes={'title': str(title), 'description': description, 'number_of_links': len(all_links)})
    _graph.add_node(node)
    map[title] = node

    if parent != None:
        parent.add_neighbour(node)

    num = 0

    for link in all_links:
        if link == child:
            continue
        href = link.get('href')
        if href is not None and is_href_wiki_link(href):
            num += 1
            link = make_link_from_href(href)
            scrape_node(node, link, lvl+1)
        if num == _num_of_links:
            break



def add_description(soup):
    description = ""
    paragraphs = soup.select("main p")
    for p in paragraphs:
        if len(p.get_text(strip=True, separator=' ')):
            description = p.get_text(strip=True, separator=' ')
            break
    description = description.replace('"', '')
    return description


def make_link_from_href(href):
    return "https://en.wikipedia.org" + href


def is_href_wiki_link(href):
    return "/wiki/" in href and "#" not in href and ":" not in href and len(href) > 0 and ':' not in href.split('wiki')[1] and 'Main_Page' not in href


def make_soup_from_page(page):
    wiki_page_request = r.get(page)
    wiki_page_text = wiki_page_request.text
    return BeautifulSoup(wiki_page_text, 'html.parser')


def link_with_parent(title, parent):
    parent.add_neighbour(map[title])