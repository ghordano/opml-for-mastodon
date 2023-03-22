import csv

def mastodon_account_to_openrss_url(mastodon_account):
    username, instance = mastodon_account.split('@')
    return f'https://{instance}/@{username}.rss'

input_filename = 'following_accounts.csv'
output_filename = 'following_accounts.opml'

with open(input_filename, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    mastodon_accounts = [row[0] for row in reader]

openrss_urls = [mastodon_account_to_openrss_url(account) for account in mastodon_accounts]

with open(output_filename, 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<opml version="1.0">\n')
    f.write('  <head>\n')
    f.write('    <title>Open RSS Feeds</title>\n')
    f.write('  </head>\n')
    f.write('  <body>\n')

    for url in openrss_urls:
        if url:
            username = url.split('/')[-1][1:-4]
            f.write(f'    <outline text="{username}" type="rss" xmlUrl="{url}"/>\n')

    f.write('  </body>\n')
    f.write('</opml>\n')