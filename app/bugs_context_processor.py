def init_data(request):

    user_type = ''
    name = ''
    if 'user_type' in request.session:
        user_type = request.session['user_type']

    if 'name' in request.session:
        name = request.session['name']

    return {
        'root': '',
        'name': name,
        'user_type': user_type
    }