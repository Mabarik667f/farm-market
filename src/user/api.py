from ninja import Router

router = Router()

@router.get('/')
def new_func(request):
    return "HELLO WORLD"
