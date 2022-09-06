from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe, Comments
from .forms import CommentForm, RecipeForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(
            approved=True).order_by('-created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class RecipeLike(View):

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


# def add_recipe(request):
#     if request.method == 'POST':
#         recipe_form = RecipeForm(request.POST)
#         if recipe_form.is_valid():
#             recipe_form.save()
#             return redirect('home')
#     recipe_form = RecipeForm
#     context = {
#         'recipe_form': recipe_form
#     }
#     return render(request, 'add_recipe.html', context)

    
# def edit_recipe(request, slug):
#     recipe = get_object_or_404(Recipe, slug=slug)
#     if request.method == 'POST':
#         recipe_form = RecipeForm(request.POST, instance=recipe)
#         if recipe_form.is_valid():
#             recipe_form.save()
#             return redirect('home')
#     recipe_form = RecipeForm
#     context = {
#         'recipe_form': recipe_form
#     }
#     return render(request, 'edit_recipe.html', context)


class AddRecipe(generic.CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'add_recipe.html'


class EditRecipe(generic.UpdateView):
    model = Recipe
    template_name = 'edit_recipe.html'
    fields = ['title', 'ingredients', 'preparation_content', 'featured_image', 'status']
