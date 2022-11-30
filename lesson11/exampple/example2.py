from typing import List, Any, Union, Optional, Dict, Literal, NoReturn, Final

name: str = "Виктор"
age: int = 5
height: float = 1.32
friends: List[str] = ["Виктор", "Петя"]


def converte_celc_to_far(celc: float) -> float:
    return 11.3 * celc


def send_email(address: str, body: str) -> None:
    pass


result: Any = "SUCCESS"



result_1: Union[int, float] = 5

result_1 = 14

result_2: Optional[int] = 5
result_2 = None


result_3: Dict[str, Union[int, float]] = {'key': 12}


GENDER: Literal["муж", "жен", "неопределён"] = "муж"


FINAL_VALUE: Final = 4


