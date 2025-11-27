from django.test import TestCase
from .models import Todo

class TodoModelTests(TestCase):

    def setUp(self):
        # Setup run before every test method
        self.todo = Todo.objects.create(
            title="Initial Task", 
            description="Do something"
        )

    def test_create_todo(self):
        """Test that a todo is created correctly."""
        self.assertEqual(self.todo.title, "Initial Task")
        self.assertFalse(self.todo.resolved)

    def test_edit_todo(self):
        """Test editing/updating a todo."""
        self.todo.title = "Updated Task"
        self.todo.save()
        
        # Fetch from DB to confirm save
        updated_todo = Todo.objects.get(id=self.todo.id)
        self.assertEqual(updated_todo.title, "Updated Task")

    def test_mark_resolved(self):
        """Test marking a todo as resolved."""
        self.todo.resolved = True
        self.todo.save()
        
        resolved_todo = Todo.objects.get(id=self.todo.id)
        self.assertTrue(resolved_todo.resolved)
