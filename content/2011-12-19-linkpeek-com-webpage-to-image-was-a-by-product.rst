LinkPeek.com, webpage to image, was a by-product
################################################
:date: 2011-12-19 00:23
:author: Russell Ballestrini
:tags: LinkPeek, Opinion
:slug: linkpeek-com-webpage-to-image-was-a-by-product
:status: published

**tldr;** When faced with pivoting or killing a project, take a good
look at all possible by-products. Don't miss the hidden gem in a
project's slag!

Last year I built yoursitemakesmebarf.com, a novelty web application
which allowed anonymous link submission. The software would
automatically take
`screenshots <http://russell.ballestrini.net/linkpeek-com-web-address-thumbnail-api-alpha-release/>`__
of submitted links and curate a blog. I enjoyed building the site and
the project served as my first Pyramid application.

The project's original intent was to jokingly poke fun at ugly design.
The idea never caught on. Instead the application angered website owners
and attracted undesirable people. Eventually, I decided to take it down
and come up with less combative idea.

After witnessing the Goog release of "instant previews", I knew there
was a market for a fast and reliable web screen shot service.

.. linkpeek:: 
   uri = https://linkpeek.com
   size = 500x240
   action = link_image
   title = web page screen shot service
   style = float: left; border-radius: 15px; margin-right: 15px;

So I decided to bring instant previews to anyone who needed them. I
wanted to build a fast, flexible, and easy to use screenshot API. After
a few months I had a working prototype. I named the product LinkPeek
because it described what the service was, and the domain was available.

Next I built a website thumbnail generator to show off the software. The
generator application helped reinforce the simplicity of the underlying
LinkPeek API. It didn't require any downloading, installation, or
waiting.

About a week later on a whim I posted the generator to hacker news.
I gave an honest title: 

[linkpeek-hover uri="http://linkpeek.com/website-thumbnail-generator" text="Convert Any Webpage to an Image"]
and within about about 30 minutes LinkPeek.com was placed on the front page in the number 1 spot.

**Remember, when faced with pivoting or killing a project, take a good
look at all possible by-products. Don't miss the hidden gem in a
project's slag!**
