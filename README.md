# Análise ética: reconhecimento facial na segurança pública

Estudo de caso sobre ética em Inteligência Artificial, produzido como Experiência Prática 3 da disciplina de Design Profissional (Bacharelado em Engenharia de Software, Universidade Positivo, 2026). O ponto de partida é o caso Robert Williams, a primeira prisão injusta conhecida causada por um erro de reconhecimento facial nos Estados Unidos.

O repositório tem duas partes: a **análise**, escrita em Markdown, e um **gerador em Python** que transforma esse Markdown no relatório em PDF entregue na disciplina.

- 📝 [Ler a análise completa](docs/analise-etica.md) — cerca de 2.000 palavras, 6 seções, 11 referências
- 📄 [Relatório em PDF](docs/Relatorio%20de%20Analise%20Etica%20-%20Drissana%20Rotermel%20Bueno.pdf) — 6 páginas, com capa institucional

## O caso

Em janeiro de 2020, Robert Williams foi preso em Detroit, na frente da esposa e das filhas, acusado de um furto que não cometeu. A única "prova" era um match do sistema de reconhecimento facial da polícia entre a imagem borrada de uma câmera de loja e a foto da carteira de motorista dele. O algoritmo confundiu dois homens negros. Williams passou 30 horas detido; na delegacia, a diferença entre os dois rostos era visível a olho nu. O caso virou processo movido pela ACLU e terminou em acordo em 2024, com a polícia obrigada a mudar as regras de uso da tecnologia.

O erro não foi um acidente isolado. O NIST avaliou 189 algoritmos de reconhecimento facial (FRVT Part 3, 2019) e encontrou taxas de falso positivo de 10 a 100 vezes maiores para rostos negros e asiáticos. No Brasil, onde sistemas como o Smart Sampa expandem câmeras com reconhecimento facial, os levantamentos da Rede de Observatórios da Segurança mostram que a maioria das pessoas presas por essa tecnologia é negra.

## O que a análise cobre

Quatro eixos, na ordem em que o problema se acumula:

1. **Viés e equidade.** Quatro vieses agindo ao mesmo tempo: de dados (bancos de treino com maioria de rostos brancos e masculinos; o estudo Gender Shades mediu erro abaixo de 1% em homens brancos e de até 34% em mulheres negras), de algoritmo e calibração (as taxas do NIST), de implantação (câmeras concentradas em periferias e no transporte público) e de automação (o match tratado como verdade por quem deveria conferir).
2. **Transparência e explicabilidade.** A caixa-preta é dupla: técnica (redes neurais profundas que devolvem só um número de confiança) e comercial (algoritmos como segredo de negócio, sem taxas de erro publicadas). Para o cidadão a opacidade é total: ele não sabe que foi processado, nem por qual sistema. Isso esvazia, na prática, o direito à revisão de decisão automatizada do art. 20 da LGPD.
3. **Governança.** O que deveria ter existido antes do deploy: testes com resultados separados por grupo demográfico, protocolo que trate match como pista e não como prova, revisão humana treinada para duvidar do sistema e, no contexto brasileiro, base legal para dado biométrico (dado sensível, art. 5º, II da LGPD), Relatório de Impacto à Proteção de Dados e canal real de contestação.
4. **Posicionamento e recomendações.** Nem banir, nem liberar como está: suspensão do uso policial até que existam condições verificáveis. Duas recomendações concretas: condicionar a volta a auditoria pública, com taxas de erro por grupo medidas por avaliador independente e reavaliação periódica; e transformar em regra que match nunca é prova para prender, com evidência independente obrigatória antes de qualquer detenção.

A pergunta que orienta o texto não é "a tecnologia funciona?", e sim "em que condições ela pode decidir sobre pessoas?".

## Como o repositório funciona

```
.
├── docs/
│   ├── analise-etica.md                                   fonte única do texto
│   └── Relatorio de Analise Etica - Drissana Rotermel Bueno.pdf   saída gerada
├── src/
│   └── gerar_relatorio.py                                 Markdown → PDF (ReportLab)
├── assets/fonts/                                          fontes embutidas no PDF + LICENCAS.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

O fluxo é: editar `docs/analise-etica.md`, rodar o script, e o PDF em `docs/` é regenerado. O texto não existe em dois lugares.

### Gerar o PDF

```bash
pip install -r requirements.txt
python src/gerar_relatorio.py
```

Opções: `--entrada` (outro Markdown) e `--saida` (outro caminho de PDF). Os dados da capa (instituição, curso, autora, título) ficam no dicionário `CAPA`, no topo do script.

### O que o script faz

- **Lê o Markdown** com um parser de propósito único (`ler_markdown`): `## ` abre uma seção, `- ` é item de lista (as referências) e qualquer outra linha não vazia vira parágrafo. O título `# ` e as linhas de metadados `> ` ficam fora do corpo. Não é um parser de Markdown completo, e não precisa ser: cobre exatamente o que este documento usa.
- **Monta o documento** com `SimpleDocTemplate` do ReportLab: capa em página própria, seções em sequência e referências em página nova, com estilo próprio.
- **Escapa o texto** com `html.escape` antes de criar cada `Paragraph`, porque o ReportLab interpreta marcação XML dentro dos parágrafos (`&`, `<` e `>` quebrariam a renderização).
- **Registra as fontes** a partir de `assets/fonts`, com caminhos relativos à raiz do repositório. O PDF sai idêntico em qualquer máquina, sem depender de fontes instaladas no sistema.

Verificação feita: o PDF gerado pelo script tem as mesmas 6 páginas e o mesmo texto do relatório entregue (comparação com `pypdf`).

## Por que fiz assim

- **Conteúdo separado do layout.** A primeira versão do script tinha a análise inteira dentro dele, como uma lista de strings: revisar um parágrafo exigia mexer no código. Com o texto em Markdown, ele é legível direto no GitHub, tem diff limpo no git e o script fica pequeno.
- **ReportLab, e não um conversor pronto.** Eu queria controlar capa, margens e tipografia, e entender o que acontece entre o texto e a página. Um conversor como o Pandoc resolveria em uma linha, mas sem me ensinar nada.
- **Fontes dentro do repositório.** Reprodutibilidade: quem clonar gera o mesmo PDF. Todas são de licença aberta (SIL OFL), listadas em `assets/fonts/LICENCAS.md`.

## Limitações e próximos passos

- O parser não entende negrito, links nem listas aninhadas. Se o texto precisar disso, o caminho é trocar por uma biblioteca de Markdown (por exemplo, `markdown-it-py`) e mapear os tokens para os estilos do ReportLab.
- Não há testes automatizados. O primeiro que eu escreveria: `ler_markdown` devolve 7 seções e 11 referências para o documento atual.
- A capa fica em constantes no script. Se houver um segundo relatório, faz sentido mover esses dados para o próprio Markdown (front matter).

## Por que isso importa pra mim

Trabalho com IA aplicada a recrutamento, onde algoritmos também influenciam decisões sobre pessoas. A regra que sigo na prática, nenhuma decisão sobre gente sem revisão humana, é exatamente a que faltou nesse caso.

## Licença

Código sob licença MIT. As fontes em `assets/fonts` são de terceiros, sob SIL Open Font License.

---

*Drissana Bueno · [github.com/drissanabueno](https://github.com/drissanabueno) · [LinkedIn](https://www.linkedin.com/in/drissanabueno)*
