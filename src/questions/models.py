from google.appengine.ext import db



class Question(db.Model):
    title = db.StringProperty(required=True)
    text = db.TextProperty(required=True)
    author = db.UserProperty(required=True)
    tags = db.StringListProperty()
    is_solved = db.BooleanProperty(required=True, default=False)
    created = db.DateTimeProperty(auto_now_add=True)
    score = db.IntegerProperty(default=0)

    def sorted_answers(self):
        """Return asnwers sorted by their score and creation date
        """
        answers = Answer.all().filter('question =', self).order('-score')
        return answers.fetch(200)


class QuestionVote(db.Model):
    user = db.UserProperty(required=True)
    upvote = db.BooleanProperty(required=True)
    question = db.ReferenceProperty(Question, required=True)


class QuestionTag(db.Model):
    name = db.StringProperty(required=True)
    ref_count = db.IntegerProperty(required=True)

    @classmethod
    def increment_tags(klass, names):
        """Increment tags with given names by one. If tag does not exist,
        create new one.

        Return incremented tags instances.
        """
        instances = []

        # TODO - fetch at once
        for name in names:
            tag = klass.all().filter('name =', name).get()

            if tag is None:
                tag = klass(name=name, ref_count=0)

            tag.ref_count += 1
            tag.put()
            instances.append(tag)

        return instances


class Answer(db.Model):
    question = db.ReferenceProperty(Question, required=True)
    text = db.TextProperty(required=True)
    author = db.UserProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    score = db.IntegerProperty(default=0)


class AnswerVote(db.Model):
    user = db.UserProperty(required=True)
    upvote = db.BooleanProperty(required=True)
    answer = db.ReferenceProperty(Answer, required=True)
