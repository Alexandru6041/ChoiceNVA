class ClientInternal(object):
    def getIPv4(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0] # return client IP
        else:
            ip = request.META.get('REMOTE_ADDR') # return client IP
    
        return ip