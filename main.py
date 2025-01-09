import streamlit as st
from itertools import cycle
import math

# Title
st.title("Portofolio")

# Navigation
option = st.radio(
    "Pilih bagian: ",
    ["Beranda", "Galeri Sertifikat", "Proyek"],
    horizontal=True,
    key="main_page_radio"
)

if option == "Beranda":
    # Title and introduction
    st.header("Beranda")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.image("./profile.jpg", width=160, use_container_width=False)
    
    with col2:
        st.write(""" 
        Hai, saya Dhavin Fasya Alviyanto, seorang siswa dari SMK Negeri 7 Semarang. Saya memiliki minat yang tinggi terhadap teknologi yang terus berkembang. Minat saya dalam bidang pemrograman dan jaringan mendorong saya untuk terus mencoba hal-hal baru yang saya pelajari. Linux, sebagai sistem operasi kedua yang saya gunakan, membuat saya semakin tertarik dengan perkembangan teknologi yang semakin kompleks.
        """)
    st.divider()
    st.subheader("💻 Keahlian")
    
    skills = {
        "Pemrograman": 85,
        "Jaringan": 80,
        "Linux": 78,
        "Keamanan Siber": 79,
    }

    cols = st.columns(len(skills))  # Create enough columns for each skill
    for idx, (skill, percentage) in enumerate(skills.items()):
        with cols[idx]:
            # Circular Progress with Percentage inside
            st.markdown(
                f"""
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <svg width="100" height="100">
                        <circle cx="50" cy="50" r="40" stroke="#D3D3D3" stroke-width="8" fill="none" />
                        <circle cx="50" cy="50" r="40" stroke="#00BFFF" stroke-width="8" fill="none" stroke-dasharray="{2 * math.pi * 40}" stroke-dashoffset="{2 * math.pi * 40 * (1 - percentage / 100)}" />
                        <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="18" font-weight="bold" fill="#00BFFF">{percentage}%</text>
                    </svg>
                    <p style="margin: 0; font-size: 16px; font-weight: bold;">{skill}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    
    # Add spacing
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.divider()
    st.subheader("📁 Proyek Terbaru")
    latest_projects = [
        {"judul": "Portfolio Website", "deskripsi": "A personal portfolio built using Streamlit.", "link": "#", "image": "./sertifikat/OracleJava/completionjava.jpg"},
        {"judul": "CTF Challenge Solver", "deskripsi": "A Python tool to solve CTF challenges.", "link": "#", "image": "./sertifikat/OracleJava/completionjava.jpg"},
        {"judul": "DevOps Pipeline", "deskripsi": "A CI/CD pipeline setup using GitHub Actions.", "link": "#", "image": "./sertifikat/OracleJava/completionjava.jpg"},
    ]

    for project in latest_projects:
        # Show project image
        st.image(project["image"], width=450, use_container_width=False)
        st.write(f"**{project['judul']}**")
        st.write(project["deskripsi"])
        st.markdown(f"[Lihat Proyek]({project['link']})")

    st.divider()
    st.subheader("🎓 Sertifikat Terbaru")
    latest_certificates = [
        {"image": "./sertifikat/OracleJava/completionjava.jpg", "caption": "Oracle Completion Java"},
        {"image": "./sertifikat/OracleJava/finalexam.jpg", "caption": "Oracle Final Exam Comulative Java"},
        {"image": "./sertifikat/OracleJava/finalexamcomulative.jpg", "caption": "Oracle Final Exam Java"},
    ]

    cols = cycle(st.columns(3))
    for cert in latest_certificates:
        with next(cols):
            st.image(cert["image"], caption=cert["caption"], use_container_width=True)

# Certificate Gallery Page
elif option == "Certificate Gallery":
    # Custom CSS for consistent image height
    st.markdown(
        """
        <style>
        [data-testid="stImage"] img {
            height: 300px;
            object-fit: cover;
            border-radius: 10px;
            margin-bottom: 15px;
            border: 3px solid gray;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.header("Certificate Gallery")
    
    # Subheading: Competition Certificates
    st.subheader("🏆 Competition Certificates")
    competition_images = [
        "./sertifikat/wreckit.jpg",
        "./sertifikat/wreckit.jpg",
        "./sertifikat/wreckit.jpg"
    ]
    competition_captions = [
        "2nd Place Hackathon Pijar",
        "3rd Place CTF UNISA",
        "2nd Place CTF Wreck It"
    ]

    cols = cycle(st.columns(3))
    for idx, image in enumerate(competition_images):
        with next(cols):
            st.image(image, caption=competition_captions[idx], use_container_width=True)

    # Subheading: Training Certificates
    st.subheader("📚 Training Certificates")
    training_images = [
        "./sertifikat/revou.jpg",
        "./sertifikat/DicodingDevOps/dicodingdevops.jpg",
        "./sertifikat/DicodingJaringan/dicodingjaringan.jpg",
        "./sertifikat/OracleJava/completionjava.jpg",
        "./sertifikat/OracleJava/finalexamcomulative.jpg",
        "./sertifikat/OracleJava/finalexam.jpg",
        "./sertifikat/itessential.jpg",
        "./sertifikat/solointro.jpg",
        "./sertifikat/solointrojava.jpg",
        "./sertifikat/sololearnweb.jpg",
        "./sertifikat/sololearntech.jpg",
        "./sertifikat/skilvulgit.jpg",
        "./sertifikat/skilvulintro.jpg",
        "./sertifikat/skilvulhtml.jpg",
        "./sertifikat/skilvulcss.jpg",
        "./sertifikat/skilvuljavascriptdsr.jpg",
        "./sertifikat/skilvulpythondsr.jpg",
        "./sertifikat/skilvulreactdsr.jpg",
        "./sertifikat/skilvulcppdsr.jpg",
        "./sertifikat/algo.jpg",
        "./sertifikat/c#dsr.jpg",
        "./sertifikat/skilvuliotfundamental.jpg",
        "./sertifikat/skilvuliothardware.jpg",
        "./sertifikat/skilvuliotsoftwareandplatform.jpg",
        "./sertifikat/skilvulbuild.jpg",
        "./sertifikat/skilvuljavascriptintermediate.jpg",
        "./sertifikat/skilvulpythonlanjutan.jpg",
    ]
    training_captions = [
        "RevoU Software Engineer",
        "Dicoding Dasar-Dasar DevOps",
        "Dicoding Jaringan Komputer",
        "Oracle Completion Java",
        "Oracle Final Exam Comulative Java",
        "Oracle Final Exam Java",
        "IT Essential Cisco",
        "Sololearn Intro to SQL",
        "Sololearn Intro to JAVA",
        "Sololearn Web Development",
        "Sololearn Tech for Everyone",
        "Skilvul Git & Github",
        "Skilvul Intro to Coding",
        "Skilvul HTML Dasar",
        "Skilvul CSS Dasar",
        "Skilvul JavaScript Dasar",
        "Skilvul Python Dasar",
        "Skilvul React Dasar",
        "Skilvul C++ Dasar",
        "Skilvul Data Structures Python",
        "Skilvul C# Dasar",
        "Skilvul IoT Fundamental",
        "Skilvul IoT Hardware",
        "Skilvul IoT Software and Platforms",
        "Skilvul IoT Monitoring System",
        "Skilvul JavaScript Intermediate",
        "Skilvul Python Lanjutan",
    ]

    cols = cycle(st.columns(3))
    for idx, image in enumerate(training_images):
        with next(cols):
            st.image(image, caption=training_captions[idx], use_container_width=True)

# Project Page
elif option == "Project":
    st.header("Project")
    st.write("This is the Project page.")
