from urlparse import urlparse

def camelize(variable_to_rename):
    components = variable_to_rename.split(' ')
    return components[0] + "".join(x.title() for x in components[1:])

def encode_string(string_to_encode):
    return string_to_encode.encode('ascii', 'ignore')

def is_url(url):
    parser_response = urlparse(url)
    return not parser_response.scheme and not parser_response.netloc == ''
