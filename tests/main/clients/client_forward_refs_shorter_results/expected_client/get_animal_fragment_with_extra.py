from typing import List

from pydantic import Field

from .client_forward_refs_shorter_resultsfragments import ListAnimalsFragment


class GetAnimalFragmentWithExtra(ListAnimalsFragment):
    list_string: List[str] = Field(alias="listString")
