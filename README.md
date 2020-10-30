# elp-to-html

Script que convierte una serie de archivos .elp en htmls de una única página.

Para correr este script, coloca las carpetas con los cursos en la carpeta `exes`, por ejemplo:

```bash
exes
├── curso-1
│   ├── m1.elp
│   ├── m2.elp
│   └── modulo1
│       └── m1-1.elp
└── curso-2
    ├── m1.elp
    └── m2.elp
```

Después, con python3 instalado y ubicado en la carpeta raíz de este proyecto ejecuta:

```bash
python elpToHtml.py
```

Al usar sólo librerías estandar de python no es necesario crear ningún entorno virtual.
