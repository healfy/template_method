import json
import os
import numpy as np
from typing import Type

from .base import Transposition, GetDeternminant, SumWithMatrix, MatrixCommand
from .settings import Settings


class Worker:
    _handlers = {
        'transpose': Transposition,
        'sum': SumWithMatrix,
        'determinant': GetDeternminant,
    }

    handler: Type[MatrixCommand]

    def __init__(self, source: str, dest: str, method: str):
        self.source = os.path.join(Settings.BASE_DIR, source)
        self.dest = os.path.join(Settings.BASE_DIR, dest)
        self.handler = self._handlers[method]

    def run(self):
        with open(self.source, 'r') as f:
            data = json.load(f)
        result = self.handler.process(np.array(data['matrix']))
        with open(self.dest, 'w+') as file:
            file.write(result.to_json())
        print(f'you can find result in file {self.dest}')
