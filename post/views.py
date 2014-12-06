# STEP 2:
# Let's add the comment form to our post view. If we create it
# in the view, we can add it to that view's context dictionary,
# which will allow us to pass it along to the template to be
# rendered. 

# Rememeber to import the `redirect` shortcut on the line below, along with `render`
from django.shortcuts import render, redirect
from post.models import Post
# Import the new form here:
from post.forms import CommentForm


def index(request):
    # let's show all the posts, with newest first
    posts = Post.objects.all().order_by('-published')
    context = {'posts': posts}
    return render(request, 'index.html', context)


def post(request, post_id):
    post = Post.objects.get(id=post_id)

    # Instantiate the CommentForm class here. At this
    # point in our workflow, the user has already made
    # a request to view, so we know what the post_id
    # is that they are viewing. Since our Comment Model
    # (and likewise, the Comment ModelForm) are tied to 
    # a specific Post pk, we can just pass in that pk
    # to our form (this means the user won't have to
    # select the post they want to comment on from
    # a dropdown.)
    form = CommentForm(initial={'post': post.pk})
    
    # Remember how I said we have access to everything
    # about the request in the view? Well this comes in
    # handy when dealing with forms! When you make a GET
    # request to a post URL, we load the form. If you submit
    # the form via a POST, we can use this if condition to
    # reinitialize our CommentForm with the data from the POST
    # (IE, the comment text).
    if request.method == "POST":
        # At this point in the workflow,
        # we are dealing with a bound form. A bound form has
        # data associated with it. 
        form = CommentForm(request.POST)
        # Next, Django makes it REALLY easy to check if our form is
        # valid. By calling form.is_valid(), we know if the form was
        # submitted correctly, or if it should be rerendered with
        # the appropriate errors (for example, if you didn't
        # submit the form with all of the required fields filled in) 
        if form.is_valid():
            # remember, a bound, valid ModelForm is just a model instance
            # ready to be saved to the database! Rememeber when we called
            # post.save() in the shell and the post was committed to the
            # database? That's exactly what we're doing here.
            form.save()
            # Finally, let's redirect the user back to the post they were just on.
            return redirect('/post/{}/'.format(post_id))

    # Woa, what's this "comment_set" nonsense? It's a helper method Django gives
    # us that allows us to grab the _set_ of _comments_ associated to a post!
    # It's the same as using "Comment.objects.filter(post=post)"
    # 
    # https://docs.djangoproject.com/en/dev/topics/db/queries/#following-relationships-backward
    comments = post.comment_set.all() 

    # Finally, here is our updated context! 
    # Along with post, we're passing in `form` and `comments`
    context = {'post': post, 'form': form, 'comments': comments}
    return render(request, 'post.html', context)

