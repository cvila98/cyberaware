
def update_user(user, jsonBody):
    try:
        if 'name' in jsonBody.keys():
            user.name = jsonBody['name']
        user.save()

        user_object = {
            'email': user.email,
            'name': user.name,
            'username': user.username,
            'if_admin': user.if_admin,
            'empresa': user.empresa.nom,
        }
        result = {'user': user_object}
        return None, result

    except Exception as e:
        return {'error': 'API error'}, None