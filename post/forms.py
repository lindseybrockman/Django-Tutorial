# STEP 1:
# Here, we are going to create our first ModelForm.
# A ModelForm is just like a regular Django Form,
# but it allows us to hook directly into a model
# we have already created, so we don't need to redefine
# all of the same fields we already created in our model.
# Remember when we added Posts in our Django admin?
# That form we used was a ModelForm (Django just built it for us!)
from django import forms

from post.models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        # Here we say the Model associated to this ModelForm is the Comment model
        model = Comment

    # This is the only field we are going to override. If we let Django create it for us,
    # we would see the form input as a drop down (go ahead and comment this line out after
    # step 2 & 3, and load the post page in your browser to see what I'm talking about.)
    # Since we are only going to show comment forms on a specific post page, we already
    # know that the comment will belong to that post. So let's hide that field (using the 
    # HiddenInput widget), and handle adding the specific Post pk to the form in the view.
    post = forms.ModelChoiceField(queryset=Post.objects.all(), widget=forms.HiddenInput())

# Relevent info can be found Here
# https://docs.djangoproject.com/en/1.6/ref/forms/api/
# and here
# https://docs.djangoproject.com/en/1.6/topics/forms/modelforms/
