

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser
from .models import Blog
# Create your tests here.

class BlogTest(TestCase):
    # def test_home_status(self):
    #     url = reverse('home')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'pages/home.html')



    def setUp(self):

        self.user=CustomUser.objects.create_user(
            username='ibrahimanaseer',
            email='ibrahim@test.com',
            password='test')

        self.blog=Blog.objects.create(
            title='test',
            body='rrrrrrrrrr',
            author=self.user 
        )


    def test_str_method(self):
        self.assertEqual(str(self.blog),'test')    

    def test_detail_view(self):
        url = reverse('blog_detail',args=[self.blog.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'blog_detail.html')


    def test_create_view(self):

        data={
            'title':'test',
            'body':'test',
            'author':self.user.email

         }
        url = reverse('blog_create')
        response= self.client.post(path=url,data=data,follow=True)
        self.assertRedirects(response,reverse('home'))


    