#!/usr/bin/env python
"""
Web crawler 
"""
import argparse
import sys;
from pyvirtualdisplay import Display

from lib.crawler import Crawler

from functools import lru_cache

def parse_args():
    """
    Parse arguments
    """
    parser = argparse.ArgumentParser(description='This tool recursively traverses through Web site and reports dead pages or Javascript errors.')

    parser.add_argument('--site', type=str, default='',
                        help='Which site to crawl')
    
    parser.add_argument('--delay', type=int, default=3,
                        help='Time to wait after each page load to ensure all elements have loaded')
    
    parser.add_argument('--json', type=str, default='',
                        help='Use config JSON file')

    parser.add_argument('-b', '--browser',type=str, default='',
                        help='Browser to use for crawler run: Chrome or Firefox')

    # Output Options
    parser.add_argument('-t', '--text', action='store_true',
                        help='Capture visible text')

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Verbose output')

    parser.add_argument('-o', '--output', type=str, default='',
                        help='Output Folder')

    # Login Options
    parser.add_argument('-u', '--username', type=str, default='',
                        help='Username to use for login')

    parser.add_argument('-p', '--password', type=str, default='',
                        help='Password to use for login')


    return parser.parse_args()


if __name__ == '__main__':
    sys.setrecursionlimit(15000)

    ARGS = parse_args()

    ENVIRONMENT = {'base_url': ARGS.site, 'username': ARGS.username, 'password': ARGS.password,
                   'browser': ARGS.browser,
                   'locale': ARGS.locale, 'xvfb': ARGS.xvfb, 'proxy': ARGS.proxy, 'json': ARGS.json, 'rolename': ARGS.rolename }

    OUTPUT_OPTS = {'text': ARGS.text, 'output_folder': ARGS.output }



    CRAWLER = Crawler(ENVIRONMENT, ARGS.delay, **OUTPUT_OPTS)

    CRAWLER.start_crawl()

    CRAWLER.visited_pages_report(ARGS.verbose)
    res=CRAWLER.notfound_pages_report()
    CRAWLER.notificationpopup_pages_report()

    sys.exit(res)
