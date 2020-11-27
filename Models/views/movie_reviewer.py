from django.shortcuts import render
from Models.ai_handlers.functions import clean_text, stem_text
from Models.forms import MovieReviewerForm
from Models.ai_handlers.assess_review import review_assessment


def actual_movie_reviewer_view(request):

    if request.method == 'GET':
        form = MovieReviewerForm()
        context = {'form': form}
        return render(request, 'models/actual_movie_reviewer.html', context)

    else:
        form = MovieReviewerForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            cleaned = clean_text(text)
            stemmed = stem_text(cleaned)
            result = review_assessment(stemmed)
            context = {'result': result, 'form': MovieReviewerForm()}
            return render(request, 'models/actual_movie_reviewer.html', context)


