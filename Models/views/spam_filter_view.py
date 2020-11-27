from django.shortcuts import render

from Models.ai_handlers.functions import clean_text, stem_text
from Models.ai_handlers.spam_filter import check_for_spam
from Models.forms import SpamFilterForm


def actual_spam_filter_view(request):
    if request.method == 'GET':
        form = SpamFilterForm()
        context = {'form': form}
        return render(request, 'models/actual_spam_filter.html', context)
    else:
        form = SpamFilterForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            cleaned_text = clean_text(text)
            stemmed_text = stem_text(cleaned_text)
            result = check_for_spam(stemmed_text)
            context = {'form': form, 'result': result}
            return render(request,'models/actual_spam_filter.html', context)
