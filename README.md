# Scrapping-Amazon-Product-Reviews

The task is to perform Sentiment Analysis on any product reviews of any product of your choice (atleast with 10k reviews). Here, in this repository, let's just obtain the data.

The product reviews can be obtained simply by scrapping directly from the amazon website using [Scrapy](https://scrapy.org), which is an open source and collaborative framework for extracting the data you need from websites in python.

If you're wondering if it's legal?! Check out [this](https://www.blog.datahut.co/post/is-web-data-scraping-legal) blog.

NOTE: I would recommend you to use google chrome

Let's begin! 

This is how a typical url for any product on amazon looks like.
https://www.amazon.com/Kindle-Paperwhite-Waterproof-Storage-Special/dp/B07PS737QQ/ref=cm_cr_arp_d_product_top?ie=UTF8 
What matters is just the ASIN number, which in this case is B07PS737QQ. You can simply get rid of the rest of details and just use https://www.amazon.com/dp/B07PS737QQ/ instead and it yeilds the same result.

Since we're interested only in scraping the reviews, we can rather use https://www.amazon.com/product-reviews/B07PS737QQ/ which directs to the review section of that product.


## Installationa and Creating a Spider Project

Open your command prompt and start a spider as follows:

1. Activate the virtual environment
2. Make you you install the packages here. Follow [these](https://docs.scrapy.org/en/latest/intro/install.html#intro-install) steps
3. ~ % scrapy
4. ~ % scrapy startproject amazon
Here, amazon is the project name. You can give any name of your choice
This will create a amazon directory with the following contents:

amazon/
    scrapy.cfg            # deploy configuration file

    amazon/               # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py

2. ~ % cd amazon
3. ~ % scrapy genspider reviews

