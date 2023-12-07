from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "Apocolypse-travels",
        "image": "2.png",
        "author": "Earnsforum",
        "date": date(2023, 10, 10),
        "title": "Apacolypse Travels",
        "excerpt": "There's nothing like the views you get when hiking in the mountains.",
        "content": """
            Apocolypse Travels is a travel agency that specializes in taking people to the most dangerous places on earth. We have been in business for over 20 years and have never had an accident. Our guides are all trained professionals who know how to keep you safe while still giving you the adventure of a lifetime. If you're looking for something different, then this is it! We offer tours of Chernobyl, North Korea, and more! You won't find another company like us anywhere else in the world. So what are you waiting for? Book your trip today!
        """,
    },

    {
        "slug": "when-rastafarians-rule-the-world",
        "image": "ras2.png",
        "author": "Earnsforum",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Rastafarian Wilson is now the president of the world.",
        "content": """
          The world is now a better place to live in. Reggae music is now the official music of the world. Politics is now a thing of the past. Its all about the herb and nature now"
        """,
    },
    {
        "slug": "email-marketing-is-still-relevant",
        "image": "emailmarketing.jpg",
        "author": "Earnsforum",
        "date": date(2020, 8, 5),
        "title": "Email Marketing Is Still Relevant!",
        "excerpt": "Email marketing is still one of the most effective ways to grow your business.",
        "content": """
          Email marketing is a form of direct marketing that uses electronic mail as a means of communicating commercial or fundraising messages to an audience. In its broadest sense, every email sent to a potential or current customer could be considered email marketing., 
        """,
    }
]

# get_date function to sort the posts by date
def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    # Your code for posts view
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next((post for post in all_posts if post['slug'] == slug), None)

    if identified_post is None:
        raise Http404("Post not found")
    
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
