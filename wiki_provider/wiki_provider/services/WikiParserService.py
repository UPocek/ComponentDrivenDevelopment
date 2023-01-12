from bs4 import BeautifulSoup
import requests as r
from core.models import Node, Graph


_depth = 0
_num_of_links = 0
_all_pages = set()
_all_links = set()
_pages = set()
_subpages = set()
_titles = set()
_num_of_nodes = 0
_graph = None
_parents = []
_children = []
_map = {}


def scrape(graph_name, wiki_link, depth, num_of_links):
    global _depth, _num_of_links, _pages, _graph, _all_pages, _all_links, _subpages, _titles, _num_of_nodes, _parents, _children
    _depth = int(depth)
    _num_of_links = int(num_of_links)
    _all_pages = set()
    _all_links = set()
    _pages = set()
    _subpages = set()
    _titles = set()
    _num_of_nodes = 0
    _pages.add(wiki_link)
    _all_links.add(wiki_link)
    _parents = []
    _children = []
    _graph = Graph(name=graph_name)
    _graph.save()
    start_scraping()
    print(_graph)


def start_scraping():
    global _depth, _num_of_links, _pages, _subpages
    for i in range(_depth + 1):
        scrape_one_level()
        link_nodes()


def link_nodes():
    global _parents, _children, _map
    if _parents:
        num = 0
        for parent in _parents:
            print(str(_map.get(parent)) + '\n')
            for j in range(_map.get(parent)):
                parent.add_neighbour(_children[num])
                num += 1
    _parents = _children.copy()
    _children = []


def scrape_one_level():
    global _depth, _num_of_links, _pages, _subpages, _all_pages, _num_of_nodes, _graph, _all_links, _children, _parents, _map
    children_num = 0
    for page in _pages:
        # if page in _all_pages:
        #     continue
        soup = make_soup_from_page(page)
        title = add_title(soup)
        # if title is None:
        #     continue
        # description = add_description(soup)
        links, found = find_all_sublinks(soup)
        _num_of_nodes += 1
        node = Node(atributes={'title': str(title), 'description': str("description"), 'number_of_links': str(links)})
        _graph.add_node(node)
        _children.append(node)
        _map[node] = found
        print(_map)

    _all_pages |= _pages
    _pages = _subpages.copy()
    _subpages = set()


def add_description(soup):
    description = ""
    paragraphs = soup.select("p")
    for p in paragraphs:
        if len(p.get_text(strip=True, separator=' ')):
            description = p.get_text(strip=True, separator=' ')
            break
    description = description.replace('"', '')
    return description


def add_title(soup):
    global _titles
    title = soup.title.string.replace(" - Wikipedia", "")
    if title in _titles:
        return None
    _titles.add(title)
    return title


def find_all_sublinks(soup):
    global _depth, _num_of_links, _pages, _subpages
    num = 0
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href is not None and is_href_wiki_link(href) and add_link(href):
            num += 1
        if num == _num_of_links:
            break
    return len(links), num

def add_link(href):
    global _all_links
    link = make_link_from_href(href)
    if link in _all_links:
        return False
    _all_links.add(link)
    _subpages.add(link)
    return True


def make_link_from_href(href):
    return "https://en.wikipedia.org" + href


def is_href_wiki_link(href):
    return "/wiki/" in href and "#" not in href and ":" not in href and len(href) > 0


def make_soup_from_page(page):
    wiki_page_request = r.get(page)
    wiki_page_text = wiki_page_request.text
    return BeautifulSoup(wiki_page_text, 'html.parser')