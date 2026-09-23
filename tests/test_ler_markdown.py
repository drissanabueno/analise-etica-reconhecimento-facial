"""Testes do parser de Markdown do gerador.

Roda com a biblioteca padrão, sem instalar nada além do requirements.txt:

    python -m unittest discover tests
"""

import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))

from gerar_relatorio import ENTRADA_PADRAO, ler_markdown  # noqa: E402


class TestDocumentoReal(unittest.TestCase):
    """O documento entregue na disciplina tem 7 seções e 11 referências."""

    def setUp(self):
        self.secoes = ler_markdown(ENTRADA_PADRAO)

    def test_sete_secoes(self):
        self.assertEqual(len(self.secoes), 7)

    def test_ultima_secao_sao_as_referencias(self):
        titulo, blocos = self.secoes[-1]
        self.assertEqual(titulo, "Referências")
        self.assertEqual(len(blocos), 11)

    def test_secoes_numeradas_na_ordem(self):
        numeros = [titulo.split(".")[0] for titulo, _ in self.secoes[:-1]]
        self.assertEqual(numeros, ["1", "2", "3", "4", "5", "6"])


class TestRegrasDoParser(unittest.TestCase):
    """As poucas regras que o parser conhece, testadas num arquivo pequeno."""

    def escrever(self, texto: str) -> Path:
        caminho = RAIZ / "tests" / "_tmp_parser.md"
        caminho.write_text(texto, encoding="utf-8")
        self.addCleanup(caminho.unlink)
        return caminho

    def test_titulo_e_metadados_ficam_fora_do_corpo(self):
        caminho = self.escrever(
            "# Título do documento\n"
            "> Autora: alguém\n"
            "\n"
            "## Seção A\n"
            "Parágrafo.\n"
        )
        self.assertEqual(ler_markdown(caminho), [("Seção A", ["Parágrafo."])])

    def test_item_de_lista_perde_o_hifen(self):
        caminho = self.escrever("## Referências\n- Uma\n- Duas\n")
        self.assertEqual(ler_markdown(caminho), [("Referências", ["Uma", "Duas"])])

    def test_texto_antes_da_primeira_secao_e_ignorado(self):
        caminho = self.escrever("Linha solta.\n## Seção A\nCorpo.\n")
        self.assertEqual(ler_markdown(caminho), [("Seção A", ["Corpo."])])

    def test_linhas_vazias_nao_viram_blocos(self):
        caminho = self.escrever("## Seção A\n\nUm.\n\n\nDois.\n")
        self.assertEqual(ler_markdown(caminho), [("Seção A", ["Um.", "Dois."])])


if __name__ == "__main__":
    unittest.main()
