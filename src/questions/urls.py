from django.conf.urls.defaults import patterns, url




urlpatterns = patterns('questions.views',
    url(r'^$',
        'question_list',
        name='questions_question_list'),
    url(r'^tagged/(?P<tag>[^/]+)/$',
        'question_list',
        name='questions_question_list'),
    url(r'^question-(?P<question_key>[^/]+)/$',
        'question_details',
        name='questions_question_details'),
    url(r'^question-(?P<question_key>[^/]+)/upvote/$',
        'question_vote',
        kwargs={'upvote': True},
        name='questions_question_upvote'),
    url(r'^question-(?P<question_key>[^/]+)/downvote/$',
        'question_vote',
        kwargs={'upvote': False},
        name='questions_question_downvote'),
    url(r'^new/$',
        'question_new',
        name='questions_question_new'),
)
