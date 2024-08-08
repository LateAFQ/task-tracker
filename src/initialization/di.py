from typing import Callable, TypeVar

from fastapi import FastAPI


DependencyType = TypeVar("DependencyType")


def singleton(dependency: DependencyType) -> Callable[[], DependencyType]:
    def singleton_factory() -> DependencyType:
        return dependency

    return singleton_factory


def init_dependencies(app: FastAPI) -> None:
    pass
