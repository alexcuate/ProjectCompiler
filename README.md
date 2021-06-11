# ProjectCompiler
Para correr el proyecto basta con instalar en un env los paquetes utilizados en el import (ply.lex, ply.yacc), posicionar en archivo analyzer.py y ejecutar python analyzer.py
Para proyecto final de esta materia crearemos un pequeño compilador, para un lenguaje con las siguientes funcionalidades:

    Operaciones permitidas:
        Aritméticas:
            Suma +
            Resta -
            Multiplicación *
            División /
            Exponenciación ^
        Comparación:
            ==
            != 
            >
            <
            >=
            <=
        Booleanas
            and 
            or
        Operaciones de bloques:
            ( )
            {}
    Un sistema de tipos:
        Int
        Float
        String
        Bolean
    Operaciones permitidas entre el sistema de tipos: 
    ![imagen](https://user-images.githubusercontent.com/6651949/121451569-73ff7980-c963-11eb-9381-6a2553b5c615.png)
    Flujos de control existentes, deberan seguir una estructura similar al lenguaje C, por simplicidad todo deberán llevar llaves:
        If , else, elif
        while () {}
        do {} while ();
        for (;;) {}
    Para marcar el final de una sentencia se utilizara ";"
    Es permitido el declarar y asignar una variable en la misma linea
        Flujos de control existentes, deberan seguir una estructura similar al lenguaje C, por simplicidad todo deberán llevar llaves:
        If , else, elif
        while () {}
        do {} while ();
        for (;;) {}
    Para marcar el final de una sentencia se utilizara ";"
    Es permitido el declarar y asignar una variable en la misma linea

Para la entrega de este proyecto es un repositorio de git (puede ser de github, gitlab o bitbucket), los cambios deben ser realizados usando la metodologia gitflow (https://www.atlassian.com/es/git/tutorials/comparing-workflows/gitflow-workflow (Enlaces a un sitio externo.)).

Para la parte de análisis sintáctico https://www.dabeaz.com/ply/ply.html (Enlaces a un sitio externo.)

Ejemplos: https://github.com/dabeaz/ply/blob/master/example/
