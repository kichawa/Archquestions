from google.appengine.ext.db import djangoforms

from questions.models import Question, Answer


class NewQuestionForm(djangoforms.ModelForm):

    class Meta:
        model = Question
        exclude = ('author', 'create', 'is_solved', 'score')


class AnswerForm(djangoforms.ModelForm):

    class Meta:
        model = Answer
        fields = ('text', )
