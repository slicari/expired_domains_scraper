# Import libraries
import urllib
from bs4 import BeautifulSoup
from furl import furl

# Define some variables
url_page = 'http://www.expireddomains.net/backorder-expired-domains/'
f = furl(url_page)
query_counter = 0
expired_domains = []


# Iterate through the tbody table, looking for the "field_domain" value
# Grab the 'title' value aka the expired domain

def expired_domain_parser(fu):
    # Query the site and return the sites html
    page = urllib.urlopen(fu.url)
    # Save the html as a beautiful soup object
    soup = BeautifulSoup(page, 'html.parser')
    # Parse the html and grab the tbody section
    body = soup.find('tbody')
    for ex in body.findAll('tr'):
        for expire in ex.find('td', {'class': 'field_domain'}):
            # When I remove this line it breaks so for now it stays
            for domain in expire:
                dom = expire.find('title')
            for e in body.findAll('li'):
                e.extract()
        expired_domains.append(domain)


# Grabs the total number of expired domains for the current day

def total_domain_count(fu):
    page = urllib.urlopen(fu.url)
    soup = BeautifulSoup(page, 'html.parser')
    dv = soup.find('div', {'class': 'addoptions left'})
    dv = dv.find('strong').text
    return dv.rstrip('\n\r')


# Parse the value from total_domain_count
# Divide by 25 to give us the number of pages to scrape (25 domains per page)

domain_size = total_domain_count(f)
dms = domain_size.replace(",", "")
final_num = (int(dms))
all_the_doms = (int(final_num/25))


# This function affixes the proper 'query' parameter to the url
# Passes this url to expired_domain_parser
# Repeats until 'domain_size' has been met

def domain_scraper(qc, ds):
    if not expired_domains:
        while True:
            try:
                f.add(args={'start': [qc]})
                expired_domain_parser(f)
                del f.args['start']
                qc = qc + 25
            except:
                if qc > ds:
                    break


if __name__ == '__main__':
    domain_scraper(query_counter, all_the_doms)
    # Save the scraped domains to a file called "expired_domains.txt"
    with open('expired_domains.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in expired_domains)
      
