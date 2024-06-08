![logo do projeto](assets/logo.png){width="200" .center}
# Notas Musicais

Notas musicais é um CLI para ajudar na formação de escalas e acordes

Temos dois comandos disponíveis: `escala` e `acorde`

## Como usar?

### Escala

Você pode chamar as escalas via linha de comando. Por exemplo:

```bash
poetry run notas-musicais escala
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
poetry run notas-musicais escalas F#
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
poetry run notas-musicais escalas D# menor
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
poetry run notas-musicais acorde C°
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

# Mais informações sobre o CLI

Para descobrir outras opçõesm você pode usar a flag `--help`:

```bash
poetry run escalas --help
```

Resultando em:

```
Usage: escalas [OPTIONS] [TONICA] [TONALIDADE]                                            
                                                                                           
╭─ Arguments ─────────────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica da Escala [default: c]                           │
│   tonalidade      [TONALIDADE]  Tonalidade da Escala [default: maior]                   │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                 │
│ --show-completion             Show completion for the current shell, to copy it or      │
│                               customize the installation.                               │
│ --help                        Show this message and exit.                               │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
```