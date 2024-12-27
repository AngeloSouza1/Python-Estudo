from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.models.user_model import User
from app.models.task_model import Task
from app.api.api_v1.router import router
from beanie.odm.fields import PydanticObjectId
import logging

# Configurando o logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("main")

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.on_event("startup")
async def app_init():
    logger.info("Application startup initiated.")
    cliente_db = AsyncIOMotorClient(
        settings.MONGO_CONNECTION_STRING
    ).todoapp
    
    await init_beanie(
        database=cliente_db,
        document_models=[User, Task]
    )
    logger.debug("Connected to MongoDB at: %s", settings.MONGO_CONNECTION_STRING)
    logger.info("Beanie initialized with models: User, Task.")

app.include_router(
    router,
    prefix=settings.API_V1_STR
)

# Custom OpenAPI
cached_openapi_schema = None

def custom_openapi():
    global cached_openapi_schema
    if cached_openapi_schema is not None:
        return cached_openapi_schema

    # Adicionando suporte para PydanticObjectId no esquema OpenAPI
    def pydantic_object_id_schema():
        return {"type": "string", "format": "objectid"}

    PydanticObjectId.__get_pydantic_json_schema__ = pydantic_object_id_schema

    try:
        logger.info("Generating custom OpenAPI schema.")
        cached_openapi_schema = get_openapi(
            title=settings.PROJECT_NAME,
            version="1.0.0",
            description="Custom OpenAPI schema for Todo FastAPI app",
            routes=app.routes,
        )
        logger.info("Custom OpenAPI schema generated successfully.")
        return cached_openapi_schema
    except Exception as e:
        logger.error(f"Error generating OpenAPI schema: {e}", exc_info=True)
        raise

app.openapi = custom_openapi
