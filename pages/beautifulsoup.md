title: BeautifulSoupがすごく便利
date: 2013-07-10
tags: python

スクレイピングするときに <a href="http://www.crummy.com/software/BeautifulSoup/">Beautiful Soup</a>がすごく便利だったので使い方を簡単にメモしておく。


    soup = BeautifulSoup(html_text)
    
    ## return elements which has class = 'foo'
    soup.select('.foo')

    ## return all a tag.

    all_hrefs = soup.find_all('a')
    
    ## return get href data.
    
    hrefs  = [item.get('href') for item in all_hrefs]

    ## return inner text.
    
    [href.get_text() for href in hrefs]

  
  
