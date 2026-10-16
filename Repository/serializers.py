from rest_framework import serializers
from Repository.models import QuestionsDB

class QuestionSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=200)
    language=serializers.ChoiceField(choices=QuestionsDB.Language_CHOICES,default="python")
    difficulty_level=serializers.ChoiceField(choices=QuestionsDB.DIFFICULTY_CHOICES,default="easy")
    topic=serializers.CharField(max_length=100)
    notes=serializers.CharField()
    published_date=serializers.DateTimeField(read_only=True)
    sample_input=serializers.CharField()
    sample_output=serializers.CharField()
    is_activate=serializers.BooleanField(default=True)