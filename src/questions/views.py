import logging

from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from google.appengine.api import users

from misc.shortcuts import render, login_required, get_object_or_404

from questions.models import Question, QuestionVote, QuestionTag
from questions.forms import NewQuestionForm, AnswerForm




def question_list(request, tag=None):
    ctx = {}

    # TODO - pagination
    questions = Question.all()
    # TODO - multiple tags filter support
    if tag:
        questions = questions.filter('tags =', tag)

    tags = QuestionTag.all().order('-ref_count')

    ctx['questions'] = questions
    ctx['tags'] = tags
    return render(request, 'questions/question_list.html', ctx)

def question_details(request, question_key):
    ctx = {}

    question = get_object_or_404(Question, key=question_key)

    if request.method == 'POST':
        user = users.get_current_user()
        if user is None:
            return redirect(users.create_login_url(request.path))

        initial = {
            'author': users.get_current_user(),
            'question': question,
        }
        form = AnswerForm(request.POST, initial=initial)
        if form.is_valid():
            # XXX FIXME - why initial data does not exist in cleaned data?
            form.cleaned_data.update(initial)

            form.save()

            return redirect(reverse('questions_question_list'))
        ctx['answer_form'] = form

    else:
        ctx['answer_form'] = AnswerForm()


    ctx['question'] = question
    return render(request, 'questions/question_details.html', ctx)

@login_required
def question_vote(request, question_key, upvote):
    question = get_object_or_404(Question, key=question_key)
    user = users.get_current_user()

    # check it not already voted..
    vote = QuestionVote.all() \
            .filter('question =', question).filter('user =', user).get()

    if vote is None:
        vote = QuestionVote(question=question, user=user, upvote=upvote)
        vote.put()
        question.score += 1 if upvote else -1
        question.put()
    else:
        logging.info('Duplicated vote: %s;;%s', question, user)

    redirect_url = request.META.get('HTTP_REFERER', None)
    if redirect_url is None:
        logging.warning('No referer. Fallback to questions list')
        redirect_url = reverse('questions_question_list')
    return redirect(redirect_url)

@login_required
def question_new(request):
    # TODO - user has to be logged in
    ctx = {}

    if request.method == 'POST':
        initial = {'author': users.get_current_user()}
        form = NewQuestionForm(request.POST, initial=initial)

        if form.is_valid():

            # XXX FIXME - why author property does not exist in cleaned data?
            form.cleaned_data['author'] = users.get_current_user()

            question = form.save()
            QuestionTag.increment_tags(question.tags)
            redirect_url = reverse('questions_question_details',
                    kwargs={'question_key': question.key()})
            return redirect(redirect_url)

        ctx['form'] = form

    else:
        ctx['form'] = NewQuestionForm()

    return render(request, 'questions/question_new.html', ctx)
