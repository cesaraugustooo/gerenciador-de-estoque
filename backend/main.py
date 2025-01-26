from fastapi import FastAPI
from routers.categorias import router as categoria_routers
from config.database import end_connect,connect_database
from routers.fornecedores import router as fornecedores_routers
from routers.produtos import router as produtos_router
app = FastAPI()

app.add_event_handler(event_type='startup',func=connect_database)
app.add_event_handler(event_type='shutdown',func=end_connect)

app.include_router(categoria_routers)
app.include_router(fornecedores_routers)
app.include_router(produtos_router)


