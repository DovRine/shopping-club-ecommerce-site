from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static

company_info = {
    'phone': '(+1) 234 5678 9101',
    'email': 'shop@yourdomain.com',
    'team': [
        {
            'name': 'John Rooster',
            'job_title': 'Co-Founder, President',
            'avatar': static('public/images/person_3.jpg'),
            'bio': 'Nisi at consequatur unde molestiae quidem provident voluptatum deleniti quo iste error eos est praesentium distinctio cupiditate tempore suscipit inventore deserunt tenetur.',
            'facebook_url': '#',
            'twitter_url': '#',
            'linkedin_url': '#',
            'instagramt_url': '#',
        },
        {
            'name': 'Tom Sharp',
            'job_title': 'Co-Founder, COO',
            'avatar': static('public/images/person_2.jpg'),
            'bio': 'Nisi at consequatur unde molestiae quidem provident voluptatum deleniti quo iste error eos est praesentium distinctio cupiditate tempore suscipit inventore deserunt tenetur.',
            'facebook_url': '#',
            'twitter_url': '#',
            'linkedin_url': '#',
            'instagramt_url': '#',
        },
        {
            'name': 'Winston Hodson',
            'job_title': 'Marketing',
            'avatar': static('public/images/person_1.jpg'),
            'bio': 'Nisi at consequatur unde molestiae quidem provident voluptatum deleniti quo iste error eos est praesentium distinctio cupiditate tempore suscipit inventore deserunt tenetur.',
            'facebook_url': '#',
            'twitter_url': '#',
            'linkedin_url': '#',
            'instagramt_url': '#',
        },
    ]
}
product_items = [
    {
        'title': 'Wild West Hoodie',
        'image': static('public/images/model_1_bg.jpg'),
        'rating': 5.0,
        'likes': 29,
        'short_description': 'Lorem ipsum dolor sit amet, consectetur adipisicing.',
        'cart_link': '#',
        'detail_link': '#'
    },
    {
        'title': 'Wild West Hoodie',
        'image': static('public/images/model_2_bg.jpg'),
        'rating': 5.0,
        'likes': 29,
        'short_description': 'Lorem ipsum dolor sit amet, consectetur adipisicing.',
        'cart_link': '#',
        'detail_link': '#'
    },
    {
        'title': 'Wild West Hoodie',
        'image': static('public/images/model_3_bg.jpg'),
        'rating': 5.0,
        'likes': 29,
        'short_description': 'Lorem ipsum dolor sit amet, consectetur adipisicing.',
        'cart_link': '#',
        'detail_link': '#'
    },
    {
        'title': 'Wild West Hoodie',
        'image': static('public/images/model_4_bg.jpg'),
        'rating': 5.0,
        'likes': 29,
        'short_description': 'Lorem ipsum dolor sit amet, consectetur adipisicing.',
        'cart_link': '#',
        'detail_link': '#'
    },
    {
        'title': 'Wild West Hoodie',
        'image': static('public/images/model_5_bg.jpg'),
        'rating': 5.0,
        'likes': 29,
        'short_description': 'Lorem ipsum dolor sit amet, consectetur adipisicing.',
        'cart_link': '#',
        'detail_link': '#'
    },
    {
        'title': 'Wild West Hoodie',
        'image': static('public/images/product_1_bg.jpg'),
        'rating': 5.0,
        'likes': 29,
        'short_description': 'Lorem ipsum dolor sit amet, consectetur adipisicing.',
        'cart_link': '#',
        'detail_link': '#'
    },
]
blog_posts = [
    {
        'id' : '#',
        'image': static('public/images/model_1_bg.jpg'),
        'title': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Natus eligendi nobis ea maiores sapiente veritatis reprehenderit suscipit quaerat rerum voluptatibus a eius.',
        'author': 'Ham Brook',
        'date': 'Jan 18, 2019',
        'category': 'News',
        'category_url': '#',
    },
    {
        'id' : '#',
        'image': static('public/images/product_1_bg.jpg'),
        'title': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Natus eligendi nobis ea maiores sapiente veritatis reprehenderit suscipit quaerat rerum voluptatibus a eius.',
        'author': 'James Phelps',
        'date': 'Jan 18, 2019',
        'category': 'News',
        'category_url': '#',
    },
    {
        'id' : '#',
        'image': static('public/images/model_5_bg.jpg'),
        'title': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Natus eligendi nobis ea maiores sapiente veritatis reprehenderit suscipit quaerat rerum voluptatibus a eius.',
        'author': 'James Phelps',
        'date': 'Jan 18, 2019',
        'category': 'News',
        'category_url': '#',
    },
]
services = [
    {
        'title': 'Business Consulting',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis quis molestiae vitae eligendi at.',
        'details_url': '#',
        'icon': 'pie_chart'
    },
    {
        'title': 'Market Analysis',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis quis molestiae vitae eligendi at.',
        'details_url': '#',
        'icon': 'backspace'
    },
    {
        'title': 'User Monitoring',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis quis molestiae vitae eligendi at.',
        'details_url': '#',
        'icon': 'av_timer'
    },
    {
        'title': 'Seller Consulting',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis quis molestiae vitae eligendi at.',
        'details_url': '#',
        'icon': 'beenhere'
    },
    {
        'title': 'Financial Investment',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis quis molestiae vitae eligendi at.',
        'details_url': '#',
        'icon': 'business_center'
    },
    {
        'title': 'Financial Management',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis quis molestiae vitae eligendi at.',
        'details_url': '#',
        'icon': 'cloud_done'
    },
]
testimonials = [
    {
        'image': static('public/images/person_3.jpg'),
        'client': 'John Smith',
        'quote': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur unde reprehenderit aperiam quaerat fugiat repudiandae explicabo animi minima fuga beatae illum eligendi incidunt consequatur. Amet dolores excepturi earum unde iusto.'
    },
    {
        'image': static('public/images/person_2.jpg'),
        'client': 'Robert Aguilar',
        'quote': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur unde reprehenderit aperiam quaerat fugiat repudiandae explicabo animi minima fuga beatae illum eligendi incidunt consequatur. Amet dolores excepturi earum unde iusto.'
    },
    {
        'image': static('public/images/person_4.jpg'),
        'client': 'Roger Spears',
        'quote': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur unde reprehenderit aperiam quaerat fugiat repudiandae explicabo animi minima fuga beatae illum eligendi incidunt consequatur. Amet dolores excepturi earum unde iusto.'
    },
    {
        'image': static('public/images/person_1.jpg'),
        'client': 'Kyle McDonald',
        'quote': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur unde reprehenderit aperiam quaerat fugiat repudiandae explicabo animi minima fuga beatae illum eligendi incidunt consequatur. Amet dolores excepturi earum unde iusto.'
    },
]
featured_products = [
    {
        'title': '01.',
        'image': static('public/images/model_1_bg.jpg'),
        'description': [
            'Et tempora id nostrum saepe amet doloribus deserunt totam officiis cupiditate asperiores quasi accusantium voluptatum dolorem quae sapiente voluptatem ratione odio iure blanditiis earum fuga molestiae alias dicta perferendis inventore!',
            'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus soluta assumenda sed optio, error at?'
        ],
        'price': '$269.00',
        'sale_price': '$69.00',
        'details_url': '#',
        'cart_url': '#',
        'classes': ''
    },
    {
        'title': '02.',
        'image': static('public/images/product_1_bg.jpg'),
        'description': [
            'Et tempora id nostrum saepe amet doloribus deserunt totam officiis cupiditate asperiores quasi accusantium voluptatum dolorem quae sapiente voluptatem ratione odio iure blanditiis earum fuga molestiae alias dicta perferendis inventore!',
            'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus soluta assumenda sed optio, error at?'
        ],
        'price': '$269.00',
        'sale_price': '$69.00',
        'details_url': '#',
        'cart_url': '#',
        'classes': 'order-2 order-md-1'
    },
]
def index(request):
    return render(request, template_name='public/index.html', context={
        'blog_posts': blog_posts,
        'company_info': company_info,
        'featured_products': featured_products,
        'product_items': product_items,
        'services': services,
        'testimonials': testimonials,
    })
