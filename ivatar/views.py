'''
views under /
'''
import io
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from . ivataraccount.models import ConfirmedEmail, ConfirmedOpenId


class AvatarImageView(TemplateView):
    '''
    View to return (binary) image, based for OpenID/Email (both by digest)
    '''

    def get(self, request, *args, **kwargs):
        '''
        Override get from parent class
        '''
        model = ConfirmedEmail
        if len(kwargs['digest']) == 32:
            # Fetch by digest from mail
            pass
        elif len(kwargs['digest']) == 64:
            # Fetch by digest from OpenID
            model = ConfirmedOpenId
        else:
            raise Exception('Digest provided is wrong: %s' % kwargs['digest'])

        email = model.objects.get(digest=kwargs['digest'])
        if not email.photo:
            raise Exception('No photo assigned to "%s"' % email.email)

        return HttpResponse(
            io.BytesIO(email.photo.data), content_type='image/%s' % email.photo.format)