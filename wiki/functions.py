from django.conf import settings


def default_context(context: dict, path) -> dict:
    def add_context(key, settings_value, default_value):
        if key not in context.keys():
            try:
                context[key] = settings[settings_value]
            except:
                context[key] = default_value

    def add_default_topbar():
        if 'dashboard_items' not in context.keys():
            context['dashboard_items'] = []
        home = {
            'text': 'Home',
            'href': '/',
            'active': path == '/',
        }
        # home always first
        context['dashboard_items'].insert(0, home)

    add_default_topbar()
    add_context('title', 'DEFAULT_TITLE', 'No default title')

    return context
