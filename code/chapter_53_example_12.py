"""
Using This Code Example
=========================
The code examples provided are provided by Daniel and Audrey Feldroy of
Feldroy to help you reference Django Crash Course. Code samples follow
PEP-0008, with exceptions made for the purposes of improving book
formatting. Example code is provided "as is".

Permissions
============
In general, you may use the code we've provided with this book in your
programs . You do not need to contact us for permission unless you're
reproducing a significant portion of the code and using it in educational
distributions. Examples:
* Writing an education program or book that uses several chunks of code from
    this course requires permission.
* Selling or distributing a digital package from material taken from this
    book does require permission.
* Answering a question by citing this book and quoting example code does not
    require permission.
* Incorporating a significant amount of example code from this book into your
    product's documentation does require permission.
Attributions usually include the title, author, publisher and an ISBN. For
example, "Django Crash Course, by Daniel and
Audrey Feldroy. Copyright 2020 Feldroy."

If you feel your use of code examples falls outside fair use of the permission
given here, please contact us at hi@feldroy.com.
"""

def test_detail_contains_cheese_data(rf):
    cheese = CheeseFactory()
    # Make a request for our new cheese
    url = reverse("cheeses:detail", 
        kwargs={'slug': cheese.slug})
    request = rf.get(url)
    # Use the request to get the response
    callable_obj = CheeseDetailView.as_view()
    response = callable_obj(request, slug=cheese.slug)   
    # Let's test our Cheesy details!
    assertContains(response, cheese.name) 
    assertContains(response, cheese.get_firmness_display())
    assertContains(response, cheese.country_of_origin.name)
