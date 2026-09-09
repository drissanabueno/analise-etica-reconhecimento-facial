# Relatório de análise ética: o uso de reconhecimento facial na segurança pública

> Experiência Prática 3 da disciplina de Design Profissional — Bacharelado em Engenharia de Software, Universidade Positivo. Curitiba, 2026.

> Autora: Drissana Rotermel Bueno


## 1. O caso escolhido

O caso analisado é o uso de reconhecimento facial pela polícia, a partir da história de Robert Williams, o primeiro homem que se sabe ter sido preso injustamente por erro de Inteligência Artificial nos Estados Unidos.

Em janeiro de 2020, Williams foi preso na frente da esposa e das filhas pequenas, em Detroit, acusado de um furto que não cometeu. A “prova” era um match do sistema de reconhecimento facial da polícia, que comparou a imagem borrada de uma câmera de loja com a foto da carteira de motorista dele. O algoritmo confundiu dois homens negros. Ele passou 30 horas preso, e na delegacia, quando colocaram a foto do suspeito do lado do rosto dele, dava pra ver a diferença a olho nu. O caso virou processo pela ACLU e terminou em acordo em 2024, com a polícia de Detroit obrigada a mudar as regras de uso da tecnologia.

E não foi azar de um caso isolado. O NIST, instituto de padrões dos EUA, testou 189 algoritmos de reconhecimento facial e encontrou taxas de erro de 10 a 100 vezes maiores pra rostos negros e asiáticos. O problema também já chegou ao Brasil: sistemas como o Smart Sampa estão espalhando câmeras com reconhecimento facial pelas cidades, e os levantamentos da Rede de Observatórios da Segurança mostram que a grande maioria das pessoas presas por reconhecimento facial no país é negra. Pela LGPD, dado biométrico é dado pessoal sensível, com regras mais duras de tratamento: além do problema ético, há um problema jurídico andando junto.


## 2. Escopo e partes interessadas

O escopo da análise é o uso de reconhecimento facial pela segurança pública, com o caso Robert Williams como âncora e a expansão da tecnologia no Brasil como pano de fundo. Fica de fora o uso comercial da mesma tecnologia (desbloquear celular, marcar foto em rede social), porque o dilema muda de tamanho quando o erro do algoritmo pode custar a liberdade de alguém em vez de um inconveniente.

As partes interessadas têm pesos muito diferentes. De um lado, as pessoas identificadas erroneamente pelos sistemas, com dano concentrado na população negra, e as pessoas comuns que circulam por espaços vigiados sem saber que seus rostos viram dados sensíveis processados em tempo real. Do outro, as polícias e governos que compram a tecnologia prometendo eficiência, as empresas que a desenvolvem e vendem (como a DataWorks Plus, do caso Williams), e quem deveria regular e fiscalizar: legisladores, a ANPD no contexto da LGPD, e organizações como a ACLU e a Rede de Observatórios da Segurança.

O problema central: um sistema de IA com taxas de erro desiguais entre grupos raciais está sendo usado para decisões que envolvem liberdade e presunção de inocência, sem transparência para quem é analisado e sem regras claras de responsabilidade quando o sistema erra. A pergunta que orienta a análise não é se a tecnologia funciona, e sim se ela deveria ser usada nesse contexto, em que condições, e quem responde pelos erros.


## 3. Viés e equidade

Estudando o caso, entendi que não existe “o” viés do sistema: são pelo menos quatro tipos diferentes agindo ao mesmo tempo, e é a soma deles que torna tudo tão grave.

O primeiro é o viés de dados. Esses algoritmos aprendem com bancos de imagens, e os bancos usados historicamente tinham muito mais rostos brancos e masculinos. O estudo Gender Shades, do MIT Media Lab, mediu o resultado: sistemas comerciais erravam menos de 1% com homens brancos e até 34% com mulheres negras. O que me impressionou é que o algoritmo não “escolheu” discriminar: ele só aprendeu menos sobre os rostos que viu menos, e passou a errar mais justamente com quem já é mais vulnerável.

O segundo é o viés do algoritmo e da calibração. Os testes do NIST mostraram falsos positivos de 10 a 100 vezes maiores pra rostos negros e asiáticos. Um falso positivo, nesse contexto, não é um inconveniente: é uma pessoa inocente virando suspeita de crime. No caso do Robert Williams, ninguém questionou o nível de confiança do match antes de prender um pai de família na frente das filhas.

O terceiro é o viés de implantação: onde e sobre quem a tecnologia é usada. As câmeras se concentram em regiões periféricas e no transporte público, então a população que mais circula nesses espaços é a mais vigiada e a mais exposta ao erro. No Brasil, a grande maioria das pessoas presas com uso de reconhecimento facial é negra. O sistema erra mais com essas pessoas e é mais apontado pra elas: um problema multiplica o outro.

O quarto é o viés de automação, que é humano: a tendência de tratar a resposta da máquina como verdade. Em Detroit, o match do algoritmo virou praticamente prova, e a investigação que deveria confirmar ou descartar a suspeita não aconteceu direito.

Sobre a distribuição de benefícios e riscos, o desequilíbrio é claro: o benefício prometido (investigações mais rápidas) fica com o Estado e com as empresas que vendem os sistemas; o risco fica concentrado na população negra, que já é a mais afetada por abordagens policiais e que menos participou das decisões sobre a adoção da tecnologia.


## 4. Transparência e explicabilidade

Transparente, esse sistema não é em nenhum dos níveis que importam.

Pro cidadão, a opacidade é total. Quem circula por uma área vigiada não sabe que seu rosto está sendo capturado e comparado em tempo real, e quem vira suspeito por um match não fica sabendo que foi uma máquina que o apontou. O Robert Williams só descobriu porque um policial comentou, durante o interrogatório, que “o computador” tinha dito que era ele. É impossível se defender de um acusador que você nem sabe que existe.

Pra auditores e pesquisadores, a caixa-preta é dupla. A primeira camada é técnica: sistemas de reconhecimento facial modernos usam redes neurais profundas, e nem os próprios fabricantes conseguem explicar por que o modelo considerou dois rostos parecidos, só apresentam um número de confiança. A segunda camada é comercial: os algoritmos são segredo de negócio das empresas, e as polícias que os usam quase nunca publicam taxas de erro, critérios de uso ou estatísticas. Nem quem tem o dever de fiscalizar consegue enxergar dentro do sistema.

Essa opacidade atinge a autonomia das pessoas de um jeito silencioso. Saber que há câmeras identificando rostos muda o comportamento em espaço público: a pessoa pensa duas vezes antes de ir a um protesto, a um ato político, a um culto religioso. A vigilância que não se explica limita liberdades sem precisar proibir nada. E atinge também o mercado de trabalho: uma prisão injusta, mesmo desfeita depois, vira registro, notícia e mancha no nome, e antecedente criminal é um dos filtros mais cruéis dos processos seletivos.

Do ponto de vista da proteção de dados, a falta de explicabilidade esbarra na LGPD em vários pontos. O dado biométrico facial é dado pessoal sensível, com tratamento sujeito a regras reforçadas. A lei garante os princípios da transparência e da finalidade e, no artigo 20, o direito de solicitar revisão de decisões tomadas unicamente de forma automatizada. No reconhecimento facial policial, nenhum desses direitos consegue ser exercido na prática: a pessoa não sabe que foi processada, não sabe qual sistema a apontou, não conhece a taxa de erro daquele sistema pro perfil dela e não tem canal pra pedir revisão. O direito existe no papel, mas a caixa-preta o anula na realidade.


## 5. Governança: o que deveria ter sido feito

Olhando o caso de trás pra frente, o que mais me chamou atenção é que quase nenhum erro foi inevitável. Em cada etapa existia uma decisão que poderia ter sido diferente.

Antes de lançar, a equipe deveria ter testado o sistema separando os resultados por grupo: qual a taxa de erro pra rostos negros, pra rostos asiáticos, pra mulheres? O NIST fez esse teste depois e encontrou diferenças de 10 a 100 vezes; se os próprios desenvolvedores tivessem medido isso antes, saberiam que o produto não estava pronto pra decidir nada sobre pessoas. Testar com dados diversos e publicar as taxas de erro deveria ser pré-requisito pra vender um sistema desses, do mesmo jeito que remédio não chega na farmácia sem teste.

Na implantação, faltou a regra mais básica: deixar claro que um match de reconhecimento facial é uma pista, nunca uma prova. Se o protocolo exigisse investigação independente antes de qualquer prisão, o Williams não teria sido preso, porque o caso contra ele era só o match. E a revisão humana precisa ser de verdade: um policial olhando duas fotos e confirmando o que a máquina disse não é revisão, é carimbo. Esse efeito tem nome, viés de automação, e a forma de combater é treinar quem usa o sistema pra duvidar dele.

Pela LGPD, se o caso fosse no Brasil, vários instrumentos deveriam ter sido aplicados antes: base legal específica pro tratamento de dado sensível, o Relatório de Impacto à Proteção de Dados (um estudo prévio dos riscos que o sistema cria pros titulares) e o canal de revisão de decisão automatizada do artigo 20.

No fim, governança nesse caso é responder três perguntas antes de ligar o sistema: quem autoriza o uso e com que limites? Quem audita os resultados e com que frequência? E quem responde quando o sistema erra? Em Detroit, nenhuma das três tinha resposta, e foi preciso um processo judicial e quatro anos pra polícia aceitar regras que deveriam existir desde o primeiro dia. É isso que o conceito de Ethical AI by Design propõe: essas respostas precisam nascer junto com o produto, não depois do primeiro inocente preso.


## 6. Posicionamento e recomendações

Meu posicionamento: nem banir de vez, nem liberar como está. Defendo a suspensão do uso policial da tecnologia até que regras mínimas existam e sejam comprovadas. O problema do caso não é o reconhecimento facial existir, é ele decidir sobre a liberdade de pessoas sem teste adequado, sem transparência e sem responsável pelos erros. Suspender até provar segurança é o que já fazemos com qualquer produto de risco, de remédio a avião.

Recomendação 1: condicionar a volta do uso a testes e auditoria pública. A fornecedora teria que publicar as taxas de erro separadas por grupo (raça, gênero, idade), medidas por avaliador independente como o NIST, e o contrato só valeria com taxas equivalentes entre os grupos e reavaliação periódica. Hoje o poder público compra esses sistemas sem saber quanto erram e com quem erram mais.

Recomendação 2: transformar em regra o que o caso Williams provou: match é pista de investigação, nunca prova pra prender. O protocolo deveria exigir evidência independente antes de qualquer detenção, e revisão humana treinada pra duvidar da máquina. No Brasil, somam-se as exigências da LGPD pra dado sensível: relatório de impacto antes de implantar e canal real de contestação, como manda o artigo 20.

A pergunta certa nunca foi “a tecnologia funciona?”, e sim “em que condições ela pode decidir sobre pessoas?”. Enquanto essas condições não existirem, a resposta responsável é: ainda não.


## Referências

- HILL, Kashmir. Wrongfully Accused by an Algorithm. The New York Times, 24 jun. 2020.
- ACLU. Williams v. City of Detroit — acordo judicial sobre uso de reconhecimento facial, 2024.
- NIST. Face Recognition Vendor Test (FRVT) Part 3: Demographic Effects. NISTIR 8280, 2019.
- BUOLAMWINI, Joy; GEBRU, Timnit. Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification. MIT Media Lab, 2018.
- REDE DE OBSERVATÓRIOS DA SEGURANÇA. Retrato da violência: monitoramento do reconhecimento facial no Brasil, 2019.
- BRASIL. Lei nº 13.709/2018 (Lei Geral de Proteção de Dados Pessoais), art. 5º, II e art. 20.
- PREFEITURA DE SÃO PAULO. Programa Smart Sampa — documentação pública do sistema de videomonitoramento.
- SILVA, Tarcízio. Racismo algorítmico: inteligência artificial e discriminação nas redes digitais. São Paulo: Edições Sesc, 2022.
- O'NEIL, Cathy. Algoritmos de destruição em massa: como o big data aumenta a desigualdade e ameaça a democracia. Santo André: Rua do Sabão, 2020.
- GARVIE, Clare; BEDOYA, Alvaro; FRANKLE, Jonathan. The Perpetual Line-Up: Unregulated Police Face Recognition in America. Washington: Georgetown Law, Center on Privacy & Technology, 2016.
- INSTITUTO IGARAPÉ. Reconhecimento facial no Brasil: mapeamento das experiências de uso. Rio de Janeiro, 2021.
