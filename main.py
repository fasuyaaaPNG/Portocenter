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
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.image("./profile.jpg", width=160, use_container_width=False)
    
    with col2:
        st.write(""" 
        Hai, saya Dhavin Fasya Alviyanto, seorang siswa dari SMK Negeri 7 Semarang. Saya memiliki minat yang tinggi terhadap teknologi yang terus berkembang. Minat saya dalam bidang pemrograman dan jaringan mendorong saya untuk terus mencoba hal-hal baru yang saya pelajari. Linux, sebagai sistem operasi kedua yang saya gunakan, membuat saya semakin tertarik dengan perkembangan teknologi yang semakin kompleks.
        """)
    
    st.markdown(
        """
        <p align="center">
          <a href="https://github.com/fasuyaaaPNG"><img src="https://readme-typing-svg.herokuapp.com/?lines=011010000110000101101001;CTF%20Player;Full%20Stack%20Developer;Explore%20new%20things;Always%20learning%20new%20technology&font=Pacifico&center=true&width=650&height=120&color=58a6ff&vCenter=true&size=45"></a>
        </p>
        """,
        unsafe_allow_html=True
    )
    
    st.divider()
    st.markdown(
        """
        <h3>
            <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExemgzNXFoNG15N2ViejVyODB0OGdhZjR2dmh3YWI1ZGptdmFjejZ6cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/BiSeh1hFJ2waKPld1p/giphy.gif" width="60" height="60" style="margin-right: 10px;">
            Keahlian
        </h3>
        """,
        unsafe_allow_html=True
    )
    
    # Skills
    skills = {
        "Pemrograman": 85,
        "Jaringan": 80,
        "Linux": 78,
        "Keamanan Siber": 79,
    }

    cols = st.columns(len(skills))
    for idx, (skill, percentage) in enumerate(skills.items()):
        with cols[idx]:
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
    
    st.divider()
    st.markdown(
        """
        <h3>
            <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmVkd2RnYm0zaTRoOGl4eDljaGxxY3BqMmhpeWwycXpwNTNiMWt0YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/Vf3ZKdillTMOOaOho0/giphy.gif" width="60" height="60" style="margin-right: 10px;">
            Proyek Terbaru
        </h3>
        """,
        unsafe_allow_html=True
    )
    
    # Projects
    latest_projects = [
        {"judul": "NATIX", "deskripsi": "Natix merupakan program untuk memudahkan penggunaan Nativefier tanpa perlu menginstal dependensi secara manual satu per satu dan tersedia untuk berbagai platform mulai dari Windows, MacOS (High Sierra ke atas), hingga Linux.", "link": "https://github.com/fasuyaaaPNG/Natix/releases", "image": "./project/natix.png"},
        {"judul": "Tildha AI", "deskripsi": "Tildha.AI, asisten kesehatan berbasis kecerdasan buatan, menggunakan bahasa Python dan berbagai pustaka. Proyek ini dirancang untuk memastikan efektivitas dan stabilitasnya, berdasarkan kumpulan data penelitian kami.", "link": "https://github.com/fasuyaaaPNG/Tildha.ai/blob/main/Tildha_ai_Release.ipynb", "image": "./project/tildha.png"},
        {"judul": "Tripify (Proyek RevoU Course)", "deskripsi": "Web statis ini saya buat untuk melengkapi tugas akhir dari pelatihan 'RevoU Software Engineer' yang diselenggarakan oleh RevoU.", "link": "https://revou-frontend-engineering-gobljd61b-fasuyaaapngs-projects.vercel.app/", "image": "./project/tripify.png"},
    ]

    for project in latest_projects:
        st.image(project["image"], width=300, use_container_width=False)
        st.write(f"**{project['judul']}**")
        st.write(project["deskripsi"])
        st.markdown(f"[Lihat Proyek]({project['link']})")
    
    st.divider()
    st.markdown(
        """
        <h3>
            <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzBkZjNpeWhyMHV0MXRrMmx3bGlvNnBwZGpweWh3eThtYmp2NGZ5ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/7GSmI2v4946YQlOMQj/giphy.gif" width="60" height="60" style="margin-right: 10px;">
            Sertifikat Terbaru
        </h3>
        """,
        unsafe_allow_html=True
    )
    
    # Certificates
    latest_certificates = [
        {"image": "./sertifikat/OracleJava/completionjava.jpg", "caption": "Oracle Completion Java"},
        {"image": "./sertifikat/OracleJava/finalexam.jpg", "caption": "Oracle Final Exam Comulative Java"},
        {"image": "./sertifikat/OracleJava/finalexamcomulative.jpg", "caption": "Oracle Final Exam Java"},
    ]

    cols = cycle(st.columns(3))
    for cert in latest_certificates:
        with next(cols):
            st.image(cert["image"], caption=cert["caption"], use_container_width=True)

    # Garis Pemisah
    st.divider()

    # Subjudul Sosial Media
    st.markdown(
        """
        <h3>
            <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXRmZnZ2NnZidTJsMXhsNDl3OTJlcnh2YmJ2NHB3dDF6M2xqNnJsZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/ivtjsoZxjH0j9p4XOe/giphy.gif" width="60" height="60" style="margin-right: 10px;">
            Sosial Media
        </h3>
        """,
        unsafe_allow_html=True
    )
    st.write("Temukan saya di platform berikut:")

    # Ikon sosial media dengan tautan
    st.markdown(
        """
        <div style="display: flex; gap: 20px;">
            <a href="https://www.linkedin.com/in/dhavin-fasya-alviyanto-20hmsoex00/" target="_blank" style="text-decoration: none;">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40">
            </a>
            <a href="https://github.com/fasuyaaaPNG" target="_blank" style="text-decoration: none;">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="40">
            </a>
            <a href="https://www.instagram.com/vinfasss" target="_blank" style="text-decoration: none;">
                <img src="https://cdn-icons-png.flaticon.com/512/1409/1409946.png" width="40">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Garis Pemisah
    st.divider()

    # Quotes
    st.markdown(
        """
        <h3>
            <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmQyanp0MHl1dXFkMDN5YWJpZDZyZGNwb214YTkwZHU4cTJtcGE0aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/gIfb10foLDtsWg1W3d/giphy.gif" width="50" height="50" style="margin-right: 10px;">
            Quotes
        </h3>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p align="center">
            <img src="https://media.giphy.com/media/3pTtbLJ7Jd0YM/giphy.gif" width="300px" height="180px" alt="GIF">
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p align="center">
          <img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical" alt="Random Quote">
        </p>
        """,
        unsafe_allow_html=True
    )

# Certificate Gallery Page
elif option == "Galeri Sertifikat":
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

    st.header("Galeri Sertifikat")
    
    # Subheading: Competition Certificates
    st.subheader("🏆 Sertifikat Kejuaraan")
    competition_images = [
        "./sertifikat/koalabora.jpg",
        "./sertifikat/ctfunisa.png",
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
    st.subheader("📚 Sertifikat Pelatihan")
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

elif option == "Proyek":
    st.header("📂 Proyek")
    
    on_going = [
        {"judul": "AI PPDB Stemba", "deskripsi": "Sebuah AI untuk membantu proses PPDB sebagai ganti untuk memudahkan admin sekolah dalam menjawab pertanyaan terkait PPDB. Proyek ini sedang dalam proses sehingga belum ada preview untuk proyeknya", "link": "https://github.com/fasuyaaaPNG/AI-ppdb-stemba", "image": "./project/latest.png"},
    ]
    
    projects = [
        {"judul": "NATIX", "deskripsi": "Natix merupakan program untuk memudahkan penggunaan Nativefier tanpa perlu menginstal dependensi secara manual satu per satu dan tersedia untuk berbagai platform mulai dari Windows, MacOS (High Sierra ke atas), hingga Linux.", "link": "https://github.com/fasuyaaaPNG/Natix/releases", "image": "./project/natix.png"},
        {"judul": "Tildha AI", "deskripsi": "Tildha.AI, asisten kesehatan berbasis kecerdasan buatan, menggunakan bahasa Python dan berbagai pustaka. Proyek ini dirancang untuk memastikan efektivitas dan stabilitasnya, berdasarkan kumpulan data penelitian kami.", "link": "https://github.com/fasuyaaaPNG/Tildha.ai/blob/main/Tildha_ai_Release.ipynb", "image": "./project/tildha.png"},
        {"judul": "Tripify (Proyek RevoU Course)", "deskripsi": "Web statis ini saya buat untuk melengkapi tugas akhir dari pelatihan 'RevoU Software Engineer' yang diselenggarakan oleh RevoU.", "link": "https://revou-frontend-engineering-gobljd61b-fasuyaaapngs-projects.vercel.app/", "image": "./project/tripify.png"},
        {"judul": "Linktree SENAKA", "deskripsi": "Situs yang saya buat untuk ekstrakulikuler saya di sekolah. Situs ini bertujuan untuk memudahkan calon anggota menemukan berbagai informasi serta pendaftaran melalui situs ini.", "link": "https://linkhub-senaka-py7f1z1mi-fasuyaaapngs-projects.vercel.app/", "image": "./project/linktreesenaka.jpg"},
        {"judul": "Website SENAKA", "deskripsi": "Situs yang saya buat untuk ekstrakulikuler saya di sekolah. Situs ini bertujuan sebagai pengenalan ekstrakulikuler SENAKA terhadap para anggota baru. Situs ini juga menjadi informasi tambahan untuk para calon anggota yang akan mendftar. ", "link": "https://web-senaka-9ctnrw9al-fasuyaaapngs-projects.vercel.app/", "image": "./project/websenaka.jpg"},
        {"judul": "Website Laporan PKL", "deskripsi": "Situs yang saya buat untuk membantu guru saya dalam menerima laporan magang dari para siswa. Situs ini tidak menggunakan database namun menggunakan drive dan excel sebagai penyimpanannya", "link": "https://form-laporan-plfvblc1f-fasuyaaapngs-projects.vercel.app/", "image": "./project/pkl.png"},
    ]
    
    st.subheader("🛠️ Proyek yang Sedang Dikerjakan")
    st.write("Berikut adalah proyek yang saat ini sedang dalam proses pengerjaan:")
    for project in on_going:
        st.image(project["image"], width=500, use_container_width=False)
        st.write(f"**{project['judul']}**")
        st.write(project["deskripsi"])
        st.markdown(f"[Lihat Proyek]({project['link']})")

    st.divider() 

    st.subheader("✅ Proyek yang Sudah Selesai")
    st.write("Berikut adalah daftar proyek yang telah selesai dikerjakan:")
    for project in projects:
        st.image(project["image"], width=300, use_container_width=False)
        st.write(f"**{project['judul']}**")
        st.write(project["deskripsi"])
        st.markdown(f"[Lihat Proyek]({project['link']})")