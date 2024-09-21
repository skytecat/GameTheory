# Теория игр
## Дилемма заключённого

Данный проект имитирует простую игру с конфетами, где есть автомат, который
управляет подачей конфет для двух групп людей в зависимости от того, кладет ли их
в него один или оба оператора:

|  | Оба сотрудничают | 1 обманывает, 2 сотрудничает | 1 сотрудничает, 2 обманывает | Оба обманывают |
|------------|----------|----------|----------|---------|
| Оператор 1 | +2 конфеты | +3 конфеты | -1 конфета | 0 конфет |
| Оператор 2 | +2 конфеты | -1 конфета | +3 конфеты | 0 конфет |

Итак, если все сотрудничают и кладут конфеты в автомат, как было условлено,
каждый получает вознаграждение. Но у обоих участников также есть соблазн
схитрить и только притвориться, что они кладут конфету в автомат, потому что в этом случае
их группа получит обратно 3 конфеты, просто взяв одну конфету у второй
группы. Проблема в том, что если оба оператора решат играть грязно, то никто
ничего не получит.

## Типы поведения

В данном проекте представлены 5 моделей поведения:

| Тип поведения | Действия игрока                                                                                                                                                                                         |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cheater       | Всегда обманывает                                                                                                                                                                                          |
| Cooperator    | Всегда сотрудничает                                                                                                                                                                                      |
| Copycat       | Начинает с сотрудничества, но потом просто повторяет то, что делает другой игрок                                                                                                                      |
| Grudger       | Начинает всегда с сотрудничества, но превращается в Cheater навсегда, как только второй игрок обманет хоть раз                                                                                                         |
| Detective     | First four times goes with [Cooperate, Cheat, Cooperate, Cooperate],  and if during these four turns another guy cheats even once -  switches into a Copycat. Otherwise, switches into Cheater himself |

-----

## Project Requirments

Need to model a system with seven
classes - `Game`, `Player` and five behavior types (subclassed from `Player`).

Here, `registry` is used to keep track of the current number of candy
during the game, while `player1` and `player2` are instances of 
subclasses of `Player` (each being one of 5 behavior types). Calling 
`play()` method of a `Game` instance should perform a simulation
of a specified number of matches between players of a given behavior.

Method `top3()` should print current top three player's behaviors
along with their current score.

By default, code when run should simulate 10 matches (one call of
`play()`) between every pair of two players with *different* behavior
types (total 10 rounds by 10 matches each, no matches between two
copies of the same behavior) and print top three winners after the 
whole game.

