from __future__ import annotations
import argparse
from dataclasses import dataclass
import re
from typing import Optional

@dataclass
class ArithmeticParser:
    operator: Optional[str] = None
    leftexp: Optional[ArithmeticParser] = None
    rightexp: Optional[ArithmeticParser] = None
    __ADD: str = "+"
    __SUB: str = "-"
    __MUL: str = "*"
    __DIV: str = "/"


    def __post_init__(self):
        op_list = [self.__ADD, self.__SUB, self.__MUL, self.__DIV]
        if self.operator not in op_list and self.operator is not None:
            raise ValueError(f"[{self.operator}] is not a valid operator")


def args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "command",
            help="Arithmetic input to be calculated",
    )
    return parser.parse_args()

def parse_input(input:str) -> ArithmeticParser:
    input = re.split('\+|-|\*|\/', input)
    print(input)
    root = ArithmeticParser()
    for idx, val in enumerate(input):
        ...



        
if __name__ == '__main__':
    input = args().command
    parse_input(input)
    
