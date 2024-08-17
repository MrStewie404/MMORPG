from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .filters import AdsFilter
from .forms import AdForm, ReviewForm
from .models import User, Ads, Category, Reviews
from django.contrib.auth.decorators import login_required 

class UserDetail(DetailView):
    model = User
    template_name = 'user.html'
    context_object_name = 'user'

@login_required
def user_detail(request):
    user = request.user
    ads = Ads.objects.filter(user_id=user)
    my_reviews = Reviews.objects.filter(user_id=user)
    them_reviews = Reviews.objects.filter(advert_id__in=ads.values('id'))
    
    context = {
        'user': user,
        'ads': ads,
        'my_reviews': my_reviews,
        'them_reviews': them_reviews,
    }
    
    return render(request, 'user.html', context)

class AdsDetail(DetailView):
    model = Ads
    template_name = 'ad.html'
    context_object_name = 'ad'

class AdsUpdate(UpdateView):
    form_class = AdForm
    model = Ads
    template_name = 'ad_edit.html'

class AdsDelete(DeleteView):
    model = Ads
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('ads_view')

class ReviewsCreate(CreateView):
    form_class = ReviewForm
    model = Reviews
    template_name = 'review_create.html'

class AdsView(ListView):
    model = Ads
    ordering = 'id'
    template_name = 'ads.html'
    context_object_name = 'ads'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        user = User.objects.get(username=request.user.username) 
        if form.is_valid:
            Ads.objects.create(
                user_id=user.id, 
                title=request.POST.get('title') , 
                text=request.POST.get('text'), 
                content_type=request.POST.get('content_type')
            )
            return HttpResponseRedirect('/')
    else:
        form = AdForm()
    return render(request, 'create_ad.html', {'form': form})

class ReviewDetail(DetailView):
    model = Reviews
    template_name = 'review_detail.html'
    context_object_name ='review'

class ReviewUpdate(UpdateView):
    form_class = ReviewForm
    model = Reviews
    template_name = 'review_edit.html'

def review_create(request, pk):
       ad = get_object_or_404(Ads, pk=pk) 
       user = request.user.id
       if request.method == 'POST':
           form = ReviewForm(request.POST)
           if form.is_valid():
               review = form.save(commit=False) 
               review.advert = ad
               review.user_id = user
               review.save() 
               return redirect('ad_detail', pk=ad.id) 
       else:
           form = ReviewForm()
       return render(request, 'review_create.html', {'form': form, 'ad': ad})