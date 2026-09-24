from django.test import TestCase
from django.urls import reverse

from .models import List


class TodoListTests(TestCase):
    def test_home_shows_strike_unstrike_and_delete_links(self):
        List.objects.create(item='Buy milk', completed=False)
        List.objects.create(item='Read book', completed=True)

        response = self.client.get(reverse('home'))

        self.assertContains(response, 'Buy milk')
        self.assertContains(response, 'Read book')
        self.assertContains(response, 'Strike')
        self.assertContains(response, 'Unstrike')
        self.assertContains(response, 'Delete')
        self.assertContains(response, 'Add')
        self.assertContains(response, reverse('add'))
        self.assertContains(response, reverse('strike', args=[1]))
        self.assertContains(response, reverse('unstrike', args=[2]))
        self.assertContains(response, reverse('delete', args=[1]))

    def test_strike_marks_item_completed(self):
        item = List.objects.create(item='Buy milk', completed=False)

        response = self.client.get(reverse('strike', args=[item.id]))

        self.assertEqual(response.status_code, 302)
        item.refresh_from_db()
        self.assertTrue(item.completed)

    def test_unstrike_marks_item_incomplete(self):
        item = List.objects.create(item='Read book', completed=True)

        response = self.client.get(reverse('unstrike', args=[item.id]))

        self.assertEqual(response.status_code, 302)
        item.refresh_from_db()
        self.assertFalse(item.completed)

    def test_add_creates_item(self):
        response = self.client.post(reverse('add'), {'item': 'Write blog post'})

        self.assertEqual(response.status_code, 302)
        self.assertTrue(List.objects.filter(item='Write blog post').exists())

    def test_delete_removes_item(self):
        item = List.objects.create(item='Buy milk', completed=False)

        response = self.client.get(reverse('delete', args=[item.id]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(List.objects.filter(id=item.id).exists())
