"""Monografía académica en Streamlit.

- Textos de cada sección: carpeta  contenido/  (archivos .md)
- Datos de la portada:    contenido/datos.json
- PDF descargable:        main.pdf (opcional, en la raíz del repositorio)

Ejecutar en local:  streamlit run app.py
"""
import html
import json
import re
from pathlib import Path

import streamlit as st

BASE = Path(__file__).parent
CONTENIDO = BASE / "contenido"
PDF = BASE / "main.pdf"

# Orden de las secciones: portada, índice, prólogo, introducción,
# cuerpo, conclusiones, anexos y bibliografía.
SECCIONES = {
    "Portada": None,
    "Índice general": None,
    "Prólogo": "01_prologo.md",
    "Introducción": "02_introduccion.md",
    "Cuerpo del trabajo": "03_cuerpo.md",
    "Conclusiones": "04_conclusiones.md",
    "Anexos": "05_anexos.md",
    "Bibliografía": "06_bibliografia.md",
}


def cargar_datos() -> dict:
    ruta = CONTENIDO / "datos.json"
    return json.loads(ruta.read_text(encoding="utf-8"))


def leer(nombre: str) -> str:
    ruta = CONTENIDO / nombre
    if not ruta.exists():
        return f"> ⚠️ No se encontró el archivo `contenido/{nombre}`."
    return ruta.read_text(encoding="utf-8")


def encabezados(texto: str):
    """Devuelve (nivel, título) de los encabezados #, ## y ###."""
    en_codigo = False
    for linea in texto.splitlines():
        if linea.strip().startswith("```"):
            en_codigo = not en_codigo
            continue
        if en_codigo:
            continue
        m = re.match(r"^(#{1,3})\s+(.*\S)", linea)
        if m:
            yield len(m.group(1)), m.group(2).strip()


def mostrar_portada(d: dict) -> None:
    e = {k: html.escape(str(v)) for k, v in d.items()}
    st.markdown(
        f"""
<div style="text-align:center; padding:2rem 0;">
<h3>{e['universidad'].upper()}</h3>
<p>{e['facultad']}<br>{e['escuela']}</p>
<h1 style="margin:3rem 0;">{e['titulo']}</h1>
<p>Monografía presentada para el curso de<br><em>{e['curso']}</em></p>
<p style="margin-top:3rem;">
<strong>Autor:</strong> {e['autor']}<br>{e['codigo']}<br>
<strong>Docente:</strong> {e['docente']}<br>
<strong>Ciclo:</strong> {e['ciclo']}</p>
<p style="margin-top:3rem;">{e['ciudad']}<br>{e['anio']}</p>
</div>
""",
        unsafe_allow_html=True,
    )


def mostrar_indice() -> None:
    st.header("Índice general")
    lineas = []
    for titulo, archivo in SECCIONES.items():
        if archivo is None:
            continue
        for nivel, texto in encabezados(leer(archivo)):
            lineas.append("  " * (nivel - 1) + f"- {'**' + texto + '**' if nivel == 1 else texto}")
    st.markdown("\n".join(lineas))
    st.caption("El índice se genera solo a partir de los títulos de cada sección.")


def main() -> None:
    d = cargar_datos()
    st.set_page_config(page_title=d["titulo"], page_icon="📄", layout="centered")

    with st.sidebar:
        st.title("📄 Monografía")
        seleccion = st.radio(
            "Secciones", list(SECCIONES), label_visibility="collapsed"
        )
        st.divider()
        if PDF.exists():
            st.download_button(
                "⬇️ Descargar versión PDF",
                data=PDF.read_bytes(),
                file_name="monografia.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
        st.caption(f"{d['autor']} · {d['anio']}")

    if seleccion == "Portada":
        mostrar_portada(d)
    elif seleccion == "Índice general":
        mostrar_indice()
    else:
        st.markdown(leer(SECCIONES[seleccion]))


main()
