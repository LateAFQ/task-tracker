from typing import Any, Optional, Tuple

from fastapi import FastAPI

from src.api.endpoints import root_router


#from src.api.common.exceptions import setup_exception_handlers
#from src.api.common.responses import DefaultJSONResponse
#from src.api.v1.dependencies import setup_dependencies
#from src.api.v1.endpoints import setup_routers
#from src.core.logger import log
#from src.core.settings import Settings


def init_app_v1(
        #settings: Settings,
        title: str = "FastAPI",
        version: str = "0.1.0",
        #swagger_ui_oauth2_redirect_url: Optional[str] = "/docs/oauth2-redirect",
        **kw: Any,
) -> Tuple[str, FastAPI, Optional[str]]:
    #log.info("Initialize V1 API")
    app = FastAPI (
        title=title,
        version=version,
        #default_response_class=DefaultJSONResponse,
        #swagger_ui_oauth2_redirect_url=swagger_ui_oauth2_redirect_url,
        **kw,
    )

    app.include_router(root_router)

    return "/api/v1", app, None
