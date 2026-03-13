import dns.resolver
import sys
import argparse

def handleError():
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

parser = argparse.ArgumentParser(description='Simple script to pull MX records for a target domain, or a list of domains from a file.')
subparsers = parser.add_subparsers(dest='mode')

# Single URL Mode
parser_url = subparsers.add_parser('single', help='Pull MX records for a single URL.')
parser_url.add_argument('url', help='The URL to pull MX records for.')

# File Mode
parser_file = subparsers.add_parser('multi', help='Pull MX records for all domains listed in a file. Each domain must be own its own line.')
parser_file.add_argument('file', help='The path to the file to read.')

handleError()

args = parser.parse_args()

if args.mode == 'single':
    result = dns.resolver.resolve(args.url, 'MX')

    for val in result:
        print(args.url, ' : ', val.to_text())

if args.mode == 'multi':
    domains = open(args.file, 'r')
    for domain in domains:
        domain = domain.strip()
        result = dns.resolver.resolve(domain, 'MX')

        for val in result:
            print(domain, ':', val.to_text().strip())
