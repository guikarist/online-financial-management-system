from django.http import HttpResponseRedirect

# Utility functions
from django.shortcuts import render


def get_alerts(request):
    """
    Collect alerts in session.
    :param request: HttpRequest
    :return: A list of alerts or an empty list
    """
    if 'alerts' in request.session:
        temp = request.session['alerts']
        del request.session['alerts']
        return temp
    else:
        return []


def redirect_with_data(request, data, redirect_link):
    """
    Redirect to another page and save some data into session.
    :param request: HttpRequest
    :param data: A dictionary containing data in view function
    :param redirect_link: A string for redirect url
    :return: HttpResponseRedirect
    """
    request.session['alerts'] = data['alerts']
    return HttpResponseRedirect(redirect_link)


def render_alert_page_with_data(request, data, redirect_link, alert):
    """
    Render alert_and_redirect.html
    :param request: HttpRequest
    :param data: A dictionary containing data in view function
    :param redirect_link: A string for redirect url in alert_and_redirect.html
    :param alert: A tuple containing alert message
    :return: Render
    """
    data['alert'] = alert
    data['redirect_link'] = redirect_link
    return render(request, 'alert_and_redirect.html', data)