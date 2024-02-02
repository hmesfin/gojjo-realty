from gojjo_realty.pages.models import SiteInfo, Links, BusinessSocial, ContactPage

def site_info(request):
    return {'site_info': SiteInfo.objects.first()}

def site_links(request):
    return {'links': Links.objects.filter(is_published=True)}

def site_socials(request):
    return {'social': BusinessSocial.objects.filter(type="primary").first()}

def contact_info(request):
    return {'contact_info': ContactPage.objects.first()}