import scrapy

#Definition of the spider
class EventSpider(scrapy.Spider):
    name = 'eventspider'

    # Link to start crawling from
    start_urls = ['https://allevents.in/new_delhi/all']

    # This function is run for each page that's crawled
    def parse(self, response):
        # Using CSS selectors to get each event heading
        # CSS selectors are easier than XPATH to get started with
        # - #event-list gets the element with "id" event-list
        # - >.event-item get each element inside #event-list with class event-item
        # - h3 gets each h3 element inside .event-item 
        # We extract title and link from the h3 element below
        for event_title in response.css('#event-list>.event-item h3'):
            yield {
              'title': event_title.css('a ::text').get(),
              'link': event_title.css('a::attr(href)').get()
            }

