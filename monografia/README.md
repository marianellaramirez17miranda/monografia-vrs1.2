# Monografía académica en LaTeX

Plantilla lista para GitHub con la estructura clásica de una monografía:

1. Portada
2. Índice general
3. Prólogo
4. Introducción
5. Cuerpo del trabajo (3 capítulos)
6. Conclusiones
7. Anexos
8. Bibliografía

## Estructura

```
.
├── main.tex                  # Documento principal (orden de las secciones)
├── config/
│   ├── datos.tex             # ← EDITE AQUÍ: título, autor, universidad, curso...
│   └── preambulo.tex         # Paquetes, idioma y formato
├── capitulos/
│   ├── 00_portada.tex
│   ├── 01_prologo.tex
│   ├── 02_introduccion.tex
│   ├── 03_capitulo1.tex      # Marco teórico
│   ├── 04_capitulo2.tex      # Desarrollo del tema
│   ├── 05_capitulo3.tex      # Resultados y discusión
│   ├── 06_conclusiones.tex
│   └── 07_anexos.tex
├── bibliografia/
│   ├── referencias.bib       # Sus fuentes (las actuales son ejemplos)
│   └── apalike-es.bst        # Estilo autor-año en español
├── figuras/                  # Imágenes (y logo.png opcional para la portada)
├── app.py                    # App de Streamlit (versión web de la monografía)
├── requirements.txt          # Dependencias de la app (streamlit)
├── contenido/                # Textos de la app en Markdown + datos.json
├── .streamlit/config.toml    # Tema de la app
├── main.pdf                  # PDF compilado (descargable desde la app)
├── Makefile
├── latexmkrc
└── .github/workflows/compilar.yml
```

## Cómo empezar

1. Edite `config/datos.tex` con sus datos (aparecen en la portada y en los metadatos del PDF).
2. Reemplace el texto de ejemplo de cada archivo de `capitulos/`.
3. Agregue sus fuentes en `bibliografia/referencias.bib` y cítelas con `\citep{clave}` o `\citet{clave}`.
4. Si desea logo en la portada, guarde `figuras/logo.png`.

## Compilar

Requiere una distribución TeX Live (o MiKTeX) con `latexmk` y `babel-spanish`.

```bash
make        # genera main.pdf
make clean  # elimina archivos auxiliares
```

Sin Make: `latexmk main.tex`.

**En línea:** suba la carpeta a [Overleaf](https://www.overleaf.com) (Nuevo proyecto → Subir proyecto) y compile `main.tex`.

## GitHub

```bash
git init
git add .
git commit -m "Monografía: estructura inicial"
git branch -M main
git remote add origin https://github.com/USUARIO/REPOSITORIO.git
git push -u origin main
```

Cada vez que haga `push`, **GitHub Actions** compila el documento y deja el PDF como artefacto descargable (pestaña *Actions* → ejecución → *monografia-pdf*).

## Publicar en Streamlit Community Cloud (con tu cuenta de GitHub)

La carpeta incluye una app lista para publicar: muestra la portada, el índice
general (automático), el prólogo, la introducción, el cuerpo, las conclusiones,
los anexos y la bibliografía, con botón para descargar el PDF.

1. Suba el **contenido** de esta carpeta a la **raíz** de su repositorio de GitHub
   (`app.py`, `requirements.txt`, `contenido/`, `main.pdf`, etc. deben verse al abrir el repositorio).
2. Entre a <https://share.streamlit.io> e inicie sesión con GitHub.
3. Pulse **Create app** → *Deploy a public app from GitHub*.
4. Elija su repositorio, la rama `main` y en **Main file path** escriba `app.py`
   (si subió la carpeta completa, `monografia/app.py`).
5. Pulse **Deploy**. En 1–2 minutos tendrá una URL `https://...streamlit.app`.

Para editar la app: cambie los textos en `contenido/*.md` y los datos de la portada
en `contenido/datos.json`; al hacer `git push`, la app se actualiza sola.
Probar en local: `pip install -r requirements.txt` y `streamlit run app.py`.

Para actualizar el PDF de la app: compile con `make` y suba el nuevo `main.pdf`.

## Personalización rápida

| Qué cambiar | Dónde |
|---|---|
| Márgenes e interlineado | `config/preambulo.tex` (`geometry`, `\onehalfspacing`) |
| Agregar un capítulo | Crear `capitulos/06_nuevo.tex` y añadir `\input{...}` en `main.tex` |
| Índices de figuras/tablas | Quitar el `%` de `\listoffigures` / `\listoftables` en `main.tex` |
| Estilo de citas | `\bibliographystyle` en `main.tex` |

> Verifique con su institución la norma exigida (APA, ISO 690, Vancouver, etc.) y ajuste márgenes y estilo de citación si es necesario.
