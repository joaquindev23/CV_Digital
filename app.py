from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Joaquin Cortez"
PAGE_ICON = ":wave:"
NAME = "Joaquin Cortez"
DESCRIPTION = """
Analista de Datos, apoyando a las empresas en la toma de decisiones basadas en datos.
"""
EMAIL = "joaquinbgarg@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/@JoaquinCortez-u6i",
    "LinkedIn": "https://linkedin.com/in/joaquindata777",
    "GitHub": "https://github.com/joaquindev23",
    "X": "https://twitter.com/JoaquinDev777",
}
PROJECTS = {
    "🏆 MVP #526 - Estado: Migrando": "https://youtu.be",
    "🏆 MVP #758 - Estado: Migrando": "https://youtu.be",
    "🏆 MVP #233 - Estado: Migrando": "https://youtu.be",
    "🏆 MVP #128 - Estado: Migrando": "https://youtu.be",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Descargar CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---


st.write('\n')
st.subheader("Sobre mi")
st.write(
    """
🙋‍♂️ Con 29 años y una trayectoria diversa en múltiples
áreas laborales, he desarrollado una mentalidad
orientada al aprendizaje continuo y la adaptación a
desafíos imprevistos. Mis valores fundamentales,
arraigados en mi formación familiar, guían mi
compromiso con la excelencia profesional. Estoy
entusiasmado por colaborar en proyectos
innovadores que integren inteligencia artificial para
generar impacto positivo con valor agregado y soluciones prácticas .
"""
)

st.write("---")

st.write('\n')
st.subheader("Experiencia & Calificaciones")
st.write(
    """
- ✔️ Más de 5 años de experiencia optimizando procesos y extrayendo insights valiosos a partir de datos, mercado y consumidores. Conocimientos avanzados y prácticos en Python y SQL.

- ✔️ Capacidad para liderar equipos y tomar iniciativas estratégicas en proyectos. Experiencia en modelado de procesos y framework para la extranccion de datos.
"""
)

# st.write("---")

# # --- SKILLS ---
# st.write('\n')
# st.subheader("Hard Skills")
# st.write(
#     """
# - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
# - 📊 Data Visulization: PowerBi, MS Excel, Plotly
# - 📚 Modeling: Logistic regression, linear regression, decition trees
# - 🗄️ Databases: Postgres, MongoDB, MySQL
# """
# )

st.write("---")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Experiencia Laboral")


# --- JOB 1
st.write("🚧", "**Auditor Interno | Canal 2 Fiberway**")
st.write("2023 - 2024")
st.write(
    """
- ► Optimizé la estructura del centro de datos, reduciendo los tiempos de respuesta.
- ► Detecté y solucioné fallas críticas en procesos, mejorando la eficiencia operativa.
- ► Implementé estrategias de monitoreo interno para minimizar riesgos operativos.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Jefe de Depósito | Grupo Budeguer - Taller Pronosa**")
st.write("2022 - 2023")
st.write(
    """
- ► Lideré y capacité equipo de 15 personas.
- ► Implementé procesos que mejoraron la gestion de inventarios.
- ► Reestructuré procesos internos para optimizar la eficiencia operativa.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Auditor Empresarial Externo | EstrateIA – Consultora Empresarial**")
st.write("2022 - 2022")
st.write(
    """
- ► Diseñé estrategias de crecimiento empresarial basada en datos.
- ► Analice situaciones críticas para habilitaciones de empresas.
- ► Hice seguimiento de contratos y formulacion de estatutos.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Analista de Datos | Shell**")
st.write("2021 - 2021")
st.write(
    """
- ► Diseñé campañas publicitarias Facebook y Google ADS.
- ► Lideré lanzamiento regional de tarjeta de fidelizacion "GIF CARD SHELL".
- ► Hice seguimiento de actividades digitales y junta directiva.
"""
)

# --- JOB 5
st.write('\n')
st.write("🚧", "**Sub-Director Prensa | Municipio San Pedro de Jujuy**")
st.write("2019 - 2021")
st.write(
    """
- ► Planifiqué, formulé y coordiné estrategicas de comunicación en prensa municipal.
- ► Suervisé base de datos COVID-19 para garantizar integridad".
- ► Enfoque visionario para el crecimiento de la Sub-Secretaria de Modernización.
"""
)

st.write("---")

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("En estos momentos estamos migrando los MVP creados durante todo el 2024 como parte del proyecto empresarial Grupo Business LLC")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
