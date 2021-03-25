from rest_framework.serializers import ModelSerializer, SerializerMethodField

from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Comment


class CommentSerializer(ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'

		def create(self, validated_data):
			listing = Listing.objects.get(listing=listing.id)
			user = User.objects.get(listing.author==user.id)

			comment = Comment.objects.create(
				author=validated_data.get('author'), 
				listing=validated_data.get('listing'), 
				content =validated_data.get('content '), 
				timestamp=validated_data.get('timestamp'), 
				)

			if user.othernoti == True:
				send_mail(
					subject = 'That’s your subject',
					message = 'That’s your message body',
					from_email = 'from@yourdjangoapp.com',
					recipient_list = ['to@yourbestuser.com',]
				)

			return comment



class CommentDetailSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

