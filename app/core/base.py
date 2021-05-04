import abc
from abc import ABC
import numpy as np

from .results import Result


class MatrixCommand(ABC):

    @classmethod
    @abc.abstractmethod
    def process(cls, matrix: np.ndarray) -> Result:
        pass


class Transposition(MatrixCommand):

    @classmethod
    def process(cls, matrix: np.ndarray) -> Result:
        return Result(value=matrix.transpose())


class SumWithMatrix(MatrixCommand):

    @classmethod
    def process(cls, matrix: np.ndarray) -> Result:
        return Result(value=(matrix + matrix))


class GetDeternminant(MatrixCommand):

    @classmethod
    def process(cls, matrix: np.ndarray) -> Result:
        return Result(value=np.linalg.det(matrix))
