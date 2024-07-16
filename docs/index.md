![logo do projeto](assets/logo.png){width="200" .center}
# Notas Musicais

Notas musicais é um CLI para ajudar na formação de escalas, acordes e campos harmônicos.

Toda a aplicação é baseada em um comando chamado `notas-musicais`. Esse comando tem um subcomando relacionado a cada ação que a aplicação pode realizar. Como `escalas`, `acordes` e `campo-harmonico`.

{% include "templates/cards.html" %}
{% include "templates/instalacao.md" %}

## Como usar?

### Escala

Você pode chamar as escalas via linha de comando. Por exemplo:

```bash
{{ commands.run }} escala
```
Retornando os graus e as notas correspondentes a essa escala

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII   ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B     │
└───┴────┴─────┴────┴───┴────┴───────┘
```

#### Alteração tônica na escala

O primeiro parâmetro do CLI é a tônica da escala que deseja exibir. Desta forma, você pode alterar a escala retornada. Por exemplo, a escala de `F#`:

```bash
{{ commands.run }} escalas F#
```
Resultando em:

```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII   ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F     │
└────┴────┴─────┴────┴────┴────┴───────┘
```

#### Alteração na tonalidade da escala

Você também pode alterar a tonalidade da escala. Esse é o segundo parâmetro da linha de comando. Por exemplo, a escala de `D#` maior:

```bash
{{ commands.run }} escalas D# menor
```

Resultando em:

```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII    ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━━━━┩
│ D# │ F  │ F#  │ G# │ A# │ B  │ C#     │
└────┴────┴─────┴────┴────┴────┴────────┘
```

### Acorde

Uso básico

```bash
poetry run notas-musicias acorde
```

Resultando em:

```
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

Variações na cifra:
```bash
{{ commands.run }} acorde C°
```

Resultando em:
```
┏━━━┳━━━━━━┳━━━━┓
┃ I ┃ III- ┃ V- ┃
┡━━━╇━━━━━━╇━━━━┩
│ C │ D#   │ F# │
└───┴──────┴────┘
```

Até o momento você pode usar acordes maiores, menores, diminutos e aumentados.

### Campo harmônico

Você pode chamar os campos harmônicos via o subcomando `campo-harmonico`. Por exemplo:

```bash
{{ commands.run }} campo-harmonico

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ vii° ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ C │ Dm │ Em  │ F  │ G │ Am │ B°   │
└───┴────┴─────┴────┴───┴────┴──────┘
```

Por padrão os parâmetros utilizados são a tônica de `C` e o campo harmônico `maior`.

#### Alterações nos campos harmônicos

Você pode alterar os parâmetros da tônica e da tonalidade.

```bash
{{ commands.run }} campo-harmonico [TONICA] [TONALIDADE]
```

#### Alteração na tônica do campo harmônico

Um exemplo com o campo harmônico de `E`:

```bash
{{ commands.run }} campo-harmonico E

┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii° ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#°  │
└───┴─────┴─────┴────┴───┴─────┴──────┘
```

#### Alteração na tonalidade do campo harmônico

Um exemplo com o campo harmônico de `G` na tonalidade `menor`:

```bash
{{ commands.run }} campo-harmonico G menor

┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii° ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Gm │ A°  │ A#  │ Cm │ Dm │ D# │ F   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```

# Mais informações sobre o CLI

Para descobrir outras opçõesm você pode usar a flag `--help`:

```bash
{{ commands.run }} --help
```

Resultando em:

```
Usage: notas-musicais [OPTIONS] [TONICA] [TONALIDADE]                                  
                                                                                           
╭─ Commands ─────────────────────────────────────────────────────────────────────╮
│ acorde                                                                         │
│ campo-harmonico                                                                │
│ escala                                                                         │
╰────────────────────────────────────────────────────────────────────────────────╯
```

## Mais informações sobre os subcomandos

As informações sobre os subcomandos podem ser acessadas usando a flag `--help` após o nome do parâmetro. Um exemplo:

```bash
{{ commands.run }} campo-harmonico --help
                                                                                  
 Usage: notas-musicais campo-harmonico [OPTIONS] [TONICA] [TONALIDADE]            
                                                                                  
╭─ Arguments ────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica do campo harmônico [default: C]         │
│   tonalidade      [TONALIDADE]  Tonalidade do campo harmônico [default: maior] │
╰────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                    │
╰────────────────────────────────────────────────────────────────────────────────╯
```