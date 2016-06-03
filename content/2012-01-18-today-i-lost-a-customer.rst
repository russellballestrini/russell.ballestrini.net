Today I lost a customer
#######################
:date: 2012-01-18 23:30
:author: Russell Ballestrini
:tags: LinkPeek, Opinion
:slug: today-i-lost-a-customer
:status: published

Today I lost a customer.

I added some new code to `LinkPeek <http://linkpeek.com/website-thumbnail-generator>`__ to accept coupons and I didn't think of an edge case.
This ended up creating an uncaught exception in my server side code which ultimatly served the newly subscribing customer an HTTP 500 error page.

The damage was done.

This error was catastrophic and ultimately killed the conversion. Here
is an excerpt of how the user felt after the experience:

    At this point the website has failed spectacularly enough that I can
    no longer trust you with my business. Please void the charge on my
    American Express card before it's processed. I need to hear from you
    ASAP.

Customers and prospects are forgiving for normal bugs in software.
However, customers are intolerant to bugs in the sign up or payment
flow. An error in payment flow will cause friction and friction will
kill the sale.

Running a start up is hard work, and negative (but justified) feedback
hurts more then I thought it would. This email made me feel awful.

Fortunately I learned from this mistake and the user's card was never
charged.

Always make sure to extensively test payment and sign up code. Try all
the edge cases. Try to make your software break. Don't inflict friction
on your potential customers.
