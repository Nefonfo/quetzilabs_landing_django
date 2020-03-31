from .models import SocialMedia, Member

def get_social_media(request):
    data = SocialMedia.objects.all()
    return { 'SOCIAL_DATA' : data }

def get_contact_info(request):
    data = Member.objects.all().values('name', 'phone', 'email')
    return { 'CONTACT_DATA': data }