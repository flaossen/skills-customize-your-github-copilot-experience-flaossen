
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Pratique manipulação de strings, loops, condicionais, entrada de dados e seleção aleatória em Python ao criar um jogo da Forca completo.

## 📝 Tarefas

### 🛠️ Implementar o jogo da Forca

#### Descrição

Escreva um programa que escolha uma palavra aleatoriamente de uma lista predefinida e permita que o jogador tente adivinhar suas letras antes de ficar sem tentativas.

#### Requisitos

O programa concluído deve:

- Selecionar uma palavra aleatoriamente de uma lista com pelo menos cinco palavras.
- Aceitar palpites de letras usando entrada do usuário.
- Exibir o progresso da palavra oculta após cada palpite, mantendo as letras ainda não descobertas como `_`.
- Informar quando uma letra já tiver sido utilizada e evitar que ela seja contada novamente.
- Rastrear e exibir a quantidade de tentativas incorretas restantes.
- Encerrar quando o jogador descobrir todas as letras ou esgotar as tentativas incorretas.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra correta.

Exemplo de progresso:

```text
Palavra: _ _ a _ _
Digite uma letra: e
Tentativas restantes: 5
```