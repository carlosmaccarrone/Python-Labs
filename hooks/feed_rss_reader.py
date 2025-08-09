"""
Simple RSS feed reader for Clarin Politics section.
Fetches and parses the RSS feed, then prints the top 3 news items as HTML links.

Uses a custom User-Agent header to avoid HTTP 403 errors.
"""

import urllib.request
from xml.dom import minidom

def get_node_text(node):
    """Extracts text content from an XML node."""
    return ''.join([n.nodeValue for n in node.childNodes if n.nodeType == n.TEXT_NODE])

def main():
    url = 'https://www.clarin.com/rss/politica/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(url, headers=headers)
    
    with urllib.request.urlopen(req) as response:
        doc = minidom.parse(response)
    
    print('<h1>Python news</h1>')
    print('<ol>')
    for item in doc.getElementsByTagName('item')[:3]:
        link = get_node_text(item.getElementsByTagName('link')[0])
        title = get_node_text(item.getElementsByTagName('title')[0])
        print(f'<li>\n <a href="{link}">{title}</a>\n</li>')
    print('</ol>')

if __name__ == '__main__':
    main()