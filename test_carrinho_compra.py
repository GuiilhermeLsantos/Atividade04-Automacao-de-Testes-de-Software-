import pytest
from pytest_bdd import scenarios, given, when, then
from carrinho_compra import CarrinhoCompras 

scenarios('carrinho.feature')

@pytest.fixture
def carrinho():
    return CarrinhoCompras()

@given('que tenho um carrinho de compras com o item "Camiseta" e preço R$ 29.99')
def adicionar_camiseta(carrinho):
    carrinho.adicionar_itens("Camiseta", 29.99)

@when('eu adiciono o item "Calça" com o preço R$ 49.99')
def adicionar_calca(carrinho):
    carrinho.adicionar_itens("Calça", 49.99)

@then('o total do carrinho deve ser R$ 79.98')
def verificar_total(carrinho):
    assert carrinho.total() == 79.98

@when('eu removo o item "Camiseta" do carrinho')
def remover_camiseta(carrinho):
    carrinho.remover_item(0)

@then('o carrinho de compras deve estar vazio')
def verificar_carrinho_vazio(carrinho):
    assert carrinho.esta_vazio()
