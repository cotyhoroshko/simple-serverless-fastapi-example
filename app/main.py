from fastapi import FastAPI

from app.api.api_v1.api import router as api_router
from app.core import config
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Тобі вдалося, красень! Ти найшикарніша істота на світі!!!"
                       f" \n Secret Key: {config.settings.secret_key}"}


app.include_router(api_router, prefix=config.settings.prefix)
handler = Mangum(app)
