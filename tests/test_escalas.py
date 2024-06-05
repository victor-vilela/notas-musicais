"""
AAA - 3A - A3
Arrange - Act - Assets
Arrumar - Agir - Garantir
"""
from pytest import mark, raises

from notas_musicais.escala import ESCALAS, NOTAS, escala


def test_deve_funcionar_notas_minusculas():
    # Arrumar
    tonica = 'c'
    tonalidade = 'maior'

    # Act
    result = escala(tonica, tonalidade)

    # Assert
    assert result


def test_deve_retornar_erro_nota_nao_existe():
    tonica = 'X'
    tonalidade = 'maior'

    mensagem_erro = f'Essa nota não existe, tente uma dessas {NOTAS}'

    with raises(ValueError) as error:
        escala(tonica, tonalidade)
    assert mensagem_erro == error.value.args[0]


def test_deve_retornar_erro_escala_nao_existe():
    tonica = 'c'
    tonalidade = 'tonalidade'

    mensagem_erro = (
        'Essa escala não existe ou não foi implementada. '
        f'Tente uma dessas {list(ESCALAS.keys())}'
    )

    with raises(KeyError) as error:
        escala(tonica, tonalidade)
    assert mensagem_erro == error.value.args[0]


@mark.parametrize(
    'tonica, esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_deve_retornar_notas_corretas(tonica, esperado):
    resultado = escala(tonica, 'maior')
    assert resultado['notas'] == esperado


def test_deve_retornar_sete_graus():
    tonica = 'c'
    tonalidade = 'maior'
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    resultado = escala(tonica, tonalidade)

    assert resultado['graus'] == esperado
