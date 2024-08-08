
from typing import Any, Optional, Tuple

from fastapi import FastAPI


from src.core.logger import log


def init_app(
        *sub_apps: Tuple[str, FastAPI, Optional[str]],
        **kw: Any,
) -> FastAPI:
    log.info("Initialize General")
    app = FastAPI(**kw)

    for apps in sub_apps:
        app.mount(*apps)

    return app
