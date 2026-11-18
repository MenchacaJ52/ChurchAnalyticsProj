from ninja import NinjaAPI

api = NinjaAPI(title="Koinonia API", version="0.1.0")


@api.get("/health", auth=None, tags=["meta"])
def health(request):
    return {"status": "ok"}
