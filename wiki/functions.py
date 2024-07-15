from django.conf import settings


def default_context(context: dict) -> dict:
    if 'title' not in context.keys():
        try:
            context['title'] = settings.DEFAULT_TITLE
        except:
            context['title'] = 'No default title'

    return context
