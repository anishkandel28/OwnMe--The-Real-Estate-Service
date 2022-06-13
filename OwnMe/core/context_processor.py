
def global_variables(request):
    """
      The context processor must return a dictionary.
    """
    return {
        'domain_name': 'Ownme- The Real Estate',
        'domain': "http://127.0.0.1:8000/en/",
    }
