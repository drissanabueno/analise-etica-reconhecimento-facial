# Análise ética: reconhecimento facial na segurança pública

Estudo de caso sobre ética em Inteligência Artificial, desenvolvido na disciplina de Design Profissional (Engenharia de Software, Universidade Positivo).

📄 **[Relatório completo em PDF](./Relatorio%20de%20Analise%20Etica%20-%20Drissana%20Rotermel%20Bueno.pdf)** — com referências completas.

## O caso

Em janeiro de 2020, Robert Williams foi preso na frente das filhas, em Detroit, acusado de um furto que não cometeu. A única "prova": um match de reconhecimento facial que confundiu dois homens negros. Ele passou 30 horas detido. O caso virou processo pela ACLU e terminou em acordo em 2024, com a polícia obrigada a mudar as regras de uso da tecnologia.

Não foi um caso isolado: o NIST testou 189 algoritmos e encontrou taxas de erro de 10 a 100 vezes maiores pra rostos negros e asiáticos. No Brasil, onde sistemas como o Smart Sampa se expandem, a maioria das pessoas presas por reconhecimento facial é negra.

## O que a análise cobre

- **Viés e equidade** — os quatro tipos de viés no caso: de dados, de algoritmo, de implantação e de automação
- **Transparência** — a caixa-preta dupla (técnica e comercial) e por que o direito à revisão do artigo 20 da LGPD não funciona na prática
- **Impacto social** — quem carrega o risco da tecnologia e quem colhe o benefício
- **Governança** — o que deveria ter sido feito antes do deploy: testes por grupo demográfico, match como pista e não prova, revisão humana de verdade

## Meu posicionamento

Nem banir, nem liberar como está: suspensão do uso policial até existirem condições verificáveis — taxas de erro publicadas e auditadas por grupo, protocolo que trate match como pista de investigação, revisão humana treinada pra duvidar da máquina e canal real de contestação pra quem for apontado pelo sistema.

A pergunta certa nunca foi "a tecnologia funciona?", e sim "em que condições ela pode decidir sobre pessoas?".

## Por que isso importa pra mim

Trabalho com IA aplicada a recrutamento, onde algoritmos também influenciam decisões sobre pessoas. A regra que sigo na prática — nenhuma decisão sobre gente sem revisão humana — é a mesma que faltou nesse caso.

---
*Drissana Bueno · [github.com/drissanabueno](https://github.com/drissanabueno) · [LinkedIn](https://www.linkedin.com/in/drissanabueno)*
