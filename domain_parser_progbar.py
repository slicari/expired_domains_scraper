# Import libraries
import urllib
from bs4 import BeautifulSoup
from furl import furl
from tqdm import tqdm

# define some variables
url_page = 'http://www.expireddomains.net/backorder-expired-domains/'
f = furl(url_page)
query_counter = 0
bla = 25
expired_domains = []

# Iterate through the tbody table, looking for the "field_domain" value
# to grab the 'title' aka expired domain


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


def total_domain_count(fu):
    page = urllib.urlopen(fu.url)
    soup = BeautifulSoup(page, 'html.parser')
    dv = soup.find('div', {'class': 'addoptions left'})
    dv = dv.find('strong').text
    return dv.rstrip('\n\r')

# Affixes the proper 'query' parameter to the url
# Passes this url to expired_domain_parser
# Repeats until 'domain_size' has been met


domain_size = total_domain_count(f)
dms = domain_size.replace(",", "")
final_num = (int(dms))


def domain_scraper(qc, ds):
    if not expired_domains:
        while True:
            try:
                for i in tqdm(range(bla)):
                    f.add(args={'start': [qc]})
                    expired_domain_parser(f)
                    # prints out the urls we want to query so we can check they're correct
                    #print(f.url)
                    del f.args['start']
                    qc = qc + 25
                    # cuts off loop at "domain_size"...
                    # got by dividing total number of domains by 25 (# results displayed on page)
                    # to improve, need to parse and grab total number of domains, divide by 25, and
                    # set a "breaker" variable to that value that will be used to cut off the loop
            except:
                if qc > ds:
                    break



domain_scraper(query_counter, bla)

# Save the scraped domains to a file called "expired_domains.txt"
with open('expired_domains.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % place for place in expired_domains)

#print(final_num)

