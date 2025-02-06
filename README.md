<div align="center">
# Mi Diario de Codigo
</div>


## Los numerales o almoadillas

Son titulos y separadores de textos. <br> Por ejm:


### Listas

Se elaboran colocando el signo (*) <br> Por ejm:
* Daniel Lopez
* Developer Beginner
* Sena



Para darle negrilla a la palabra son dos (**) **negrilla**; para cursiva es un (*) *cursiva* 



## Para llamar un codigo dentro de MK

Se elabora con tilde cerrada <br>

```py
import Flask, render_template, request # type: ignore
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

```

## Se puede enviar por discord el codigo de esa manera

```py
if __name__ == '__main__':
    app.run(debug=True)

```
# Dato Curioso sobre metodos encadenados:
* **.lower()** <br>
Convierte todos los caracteres del texto ingresado por el usuario a minúsculas.
Esto es útil porque permite manejar respuestas como "SI", "Si", o "sI" de forma consistente, tratándolas como "si".

* **.strip()** <br>
Elimina los espacios en blanco al inicio y al final de la cadena. Esto es importante si el usuario accidentalmente escribe espacios extra antes o después de su respuesta.


# Variables que no se pueden crear para definir un valor o un string

['False', 'None', 'True', 'and', 'as', 'assert',
'async', 'await', 'break', 'class', 'continue',
'def', 'del', 'elif', 'else', 'except', 'finally',
'for', 'from', 'global', 'if', 'import', 'in', 'is',
'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']

## f-string (literal de cadena de formato)
* Desde la versión Python 3.6

```py
print(f"Hola {my_name}, tengo {age + 5} años")
```

Se puede utilizar para interpolar variables, objetos y expresiones directamente en cadenas que pueden incrustar expresiones entre llaves (), que se evalúan en tiempo de ejecución. fF{}

## Nosotros hemos utilizado en ocasiones <br>
```py
print("\n Hola Mundo \n") #Se puede utilizar de un uso o varios
```

## Split ()
Specifies the separator to use when splitting the string. By default any whitespace is a separator
```py
print("Obtener múltiples valores a la vez")
country, city = input("¿En qué país y ciudad vives?\n").split() #Los establece por espacios: Ejm: Colombia(country) Valledupar(city)
```

## ¿GIT Y GitHub No son lo mismo?

Pues no, Git es un controlador de versiones, esta herramienta te permite registrar cada cambio que se realiza en el codigo fuente de un proyecto.
GitHub es un sitio donde puedes hospedar tu codigo fuente. Es decir es un servicio de alojamiento en la nube de tu codigo fuente o proyectos. (Donde puedes hospedar ese control de versiones que has realizado con Git.

```json
    "terminal.integrated.profiles.windows": {
        "PowerShell": {
            "source": "PowerShell",
            "icon": "terminal-powershell"
        },
        "Command Prompt": {
            "path": [
                "${env:windir}\\Sysnative\\cmd.exe",
                "${env:windir}\\System32\\cmd.exe"
            ],
            "args": [],
            "icon": "terminal-cmd"
        },
        "Git Bash": {
            "source": "Git Bash",
            "icon": "github-inverted",
            "color": "terminal.ansiGreen"
        }
    },
    "terminal.integrated.defaultProfile.windows": "Git Bash"
```

## Dato curioso:
```py
    nombre = "Danny"
    edad = 23
    altura = "1.90 metros"

    print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura}")
```
