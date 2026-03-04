"""
Pacote do Core do Sistema de Serviços do Aplicativo.

Este módulo centraliza as ferramentas de cálculos antropométricos (IMC/TMB),
serviços de autenticação de usuários, gestão de dados pessoais e de planos alimentares.
"""

from .calculator import CalculatorIMC
from .calculator import CalculatorTMB
from .auth import Autenticacao
from .user_service import UserService
from .diet_service import DietService

__all__ = [
    "CalculatorIMC",
    "CalculatorTMB",
    "Autenticacao",
    "UserService",
    "DietService",
]
