from rest_framework import serializers
from sub_skill.models import SubSkill

class SubSkillSerializer(serializers.ModelSerializer):
  skill = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')

  class Meta:
    model = SubSkill
    fields = ('id', 'name', 'skill')
