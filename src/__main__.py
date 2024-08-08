from src.initialization.setup import init_app
from src.core.settings import load_settings
from src.core.uvicorn import run_api_uvicorn


def main() -> None:
    settings = load_settings()
    app = init_app(
    )
    run_api_uvicorn(app, settings)


if __name__ == "__main__":
    main()
