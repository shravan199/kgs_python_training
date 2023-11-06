def alpha(ref):
    print('Inside alhpa()')
    ref()


def beta():
    print('Inside beta')


alpha(beta)