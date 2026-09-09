# -*- coding: utf-8 -*-
"""Gera o relatório em PDF a partir de docs/analise-etica.md.

Uso:
    python src/gerar_relatorio.py
    python src/gerar_relatorio.py --entrada docs/analise-etica.md --saida docs/relatorio.pdf

O texto da análise fica no Markdown. Este script só cuida da capa, da
tipografia e da montagem das páginas, usando a biblioteca ReportLab.
"""
from __future__ import annotations

import argparse
import html
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer

RAIZ = Path(__file__).resolve().parents[1]
FONTES = RAIZ / "assets" / "fonts"
ENTRADA_PADRAO = RAIZ / "docs" / "analise-etica.md"
SAIDA_PADRAO = RAIZ / "docs" / "Relatorio de Analise Etica - Drissana Rotermel Bueno.pdf"

# Dados da capa. O corpo do relatório vem inteiro do Markdown.
CAPA = {
    "instituicao": "UNIVERSIDADE POSITIVO",
    "curso": "Bacharelado em Engenharia de Software",
    "autora": "Drissana Rotermel Bueno",
    "rgm": "RGM 49338218",
    "titulo": "RELATÓRIO DE ANÁLISE ÉTICA:<br/>o uso de reconhecimento facial na segurança pública",
    "subtitulo": "Experiência Prática 3 da disciplina de Design Profissional",
    "local_ano": "Curitiba<br/>2026",
}

GRAPHITE = HexColor("#2A2A28")
INK = HexColor("#6E6C66")


def registrar_fontes() -> None:
    """Registra as fontes de assets/fonts com os nomes usados nos estilos."""
    arquivos = {
        "Sans": "InstrumentSans-Regular.ttf",
        "SansB": "InstrumentSans-Bold.ttf",
        "Serif": "Gloock-Regular.ttf",
        "Mono": "GeistMono-Regular.ttf",
    }
    for nome, arquivo in arquivos.items():
        pdfmetrics.registerFont(TTFont(nome, str(FONTES / arquivo)))


def estilos() -> dict[str, ParagraphStyle]:
    return {
        "titulo": ParagraphStyle("h", fontName="SansB", fontSize=13, leading=17,
                                 textColor=GRAPHITE, spaceBefore=16, spaceAfter=6),
        "paragrafo": ParagraphStyle("p", fontName="Sans", fontSize=10.5, leading=16,
                                    textColor=GRAPHITE, spaceAfter=8, alignment=4),
        "referencia": ParagraphStyle("r", fontName="Sans", fontSize=9.5, leading=14,
                                     textColor=INK, spaceAfter=5),
        "capa_top": ParagraphStyle("ct", fontName="SansB", fontSize=12, leading=17,
                                   textColor=GRAPHITE, alignment=1),
        "capa_nome": ParagraphStyle("cn", fontName="Sans", fontSize=12, leading=17,
                                    textColor=GRAPHITE, alignment=1),
        "capa_titulo": ParagraphStyle("cti", fontName="Serif", fontSize=19, leading=25,
                                      textColor=GRAPHITE, alignment=1),
        "capa_sub": ParagraphStyle("cs", fontName="Sans", fontSize=11, leading=16,
                                   textColor=INK, alignment=1),
    }


def ler_markdown(caminho: Path) -> list[tuple[str, list[str]]]:
    """Lê o Markdown e devolve uma lista de (título da seção, blocos de texto).

    Entende só o que este documento usa: "## " abre uma seção, "- " é item
    de lista (as referências) e qualquer outra linha não vazia é parágrafo.
    O título "# " e as linhas de metadados "> " não entram no corpo.
    """
    secoes: list[tuple[str, list[str]]] = []
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith(("# ", "> ")):
            continue
        if linha.startswith("## "):
            secoes.append((linha[3:], []))
        elif secoes:
            secoes[-1][1].append(linha[2:] if linha.startswith("- ") else linha)
    return secoes


def montar_capa(st: dict[str, ParagraphStyle]) -> list:
    return [
        Spacer(1, 40),
        Paragraph(CAPA["instituicao"], st["capa_top"]),
        Paragraph(CAPA["curso"], st["capa_nome"]),
        Spacer(1, 30),
        Paragraph(CAPA["autora"], st["capa_nome"]),
        Paragraph(CAPA["rgm"], st["capa_nome"]),
        Spacer(1, 120),
        Paragraph(CAPA["titulo"], st["capa_titulo"]),
        Spacer(1, 20),
        Paragraph(CAPA["subtitulo"], st["capa_sub"]),
        Spacer(1, 220),
        Paragraph(CAPA["local_ano"], st["capa_nome"]),
        PageBreak(),
    ]


def gerar(entrada: Path, saida: Path) -> Path:
    registrar_fontes()
    st = estilos()
    doc = SimpleDocTemplate(
        str(saida), pagesize=A4,
        leftMargin=25 * mm, rightMargin=25 * mm, topMargin=24 * mm, bottomMargin=22 * mm,
        title="Relatório de Análise Ética — Reconhecimento Facial na Segurança Pública",
        author=CAPA["autora"],
    )
    elementos = montar_capa(st)
    for titulo, blocos in ler_markdown(entrada):
        eh_referencias = titulo.lower().startswith("refer")
        if eh_referencias:
            elementos.append(PageBreak())
        elementos.append(Paragraph(titulo, st["titulo"]))
        estilo = st["referencia"] if eh_referencias else st["paragrafo"]
        elementos += [Paragraph(html.escape(b, quote=False), estilo) for b in blocos]
    doc.build(elementos)
    return saida


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera o relatório em PDF a partir do Markdown.")
    parser.add_argument("--entrada", type=Path, default=ENTRADA_PADRAO,
                        help="arquivo Markdown da análise")
    parser.add_argument("--saida", type=Path, default=SAIDA_PADRAO,
                        help="caminho do PDF a gerar")
    args = parser.parse_args()
    print(f"PDF gerado: {gerar(args.entrada, args.saida)}")


if __name__ == "__main__":
    main()
