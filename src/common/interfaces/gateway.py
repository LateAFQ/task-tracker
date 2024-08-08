import abc
from types import TracebackType
from typing import Optional, Type, TypeVar

from src.common.interfaces.uow import AbstractUnitOfWork

GatewayType = TypeVar("GatewayType", bound="BaseGateway")


class BaseGateway(abc.ABC):
    __slots__ = ("_uow",)

    def __init__(self, uow: AbstractUnitOfWork) -> None:
        self._uow = uow

    async def __aenter__(self: GatewayType) -> GatewayType:
        await self._uow.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        await self._uow.__aexit__(exc_type, exc_value, traceback)
