# Scrapping-Amazon-Product-Reviews

The task is to perform Sentiment Analysis on any product reviews of any product of your choice (atleast with 10k reviews). Here, in this repository, let's just obtain the data.

The product reviews can be obtained simply by scrapping directly from the amazon website using [Scrapy](https://scrapy.org), which is an open source and collaborative framework for extracting the data you need from websites in python.

If you're wondering if it's legal?! Check out [this](https://www.blog.datahut.co/post/is-web-data-scraping-legal) blog.

NOTE: I would recommend you to use google chrome

Let's begin! 

This is how a typical url for any product on amazon looks like.
https://www.amazon.com/Kindle-Paperwhite-Waterproof-Storage-Special/dp/B07PS737QQ/ref=cm_cr_arp_d_product_top?ie=UTF8
What matters is just the ASIN number, which in this case is B07PS737QQ. You can simple get rid of the rest of details and simply use https://www.amazon.com/dp/B07PS737QQ/ instead and it yeilds the same result.


