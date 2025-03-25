import streamlit as st
import random

c1, c2, c3 = st.columns([1, 4, 1])
t1, t2, t3, t4, t5 = st.tabs(["Home🏠", "Experience💼", "Project🎯", "Education📖", "Contact Me📞"])

# Function to get a random color
def get_random_color():
    colors = ["red", "blue", "green", "orange", "purple", "pink", "cyan"]
    return random.choice(colors)

# JavaScript to change color on click
color_changing_script = """
    <script>
        function changeColor() {
            let colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'cyan'];
            let randomColor = colors[Math.floor(Math.random() * colors.length)];
            document.getElementById('hover-name').style.color = randomColor;
        }
        document.addEventListener('click', changeColor);
    </script>
"""

color_changing_name = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&display=swap');
        .hover-name {{
            text-align: center;
            font-weight: bold;
            font-size: 65px;
            font-family: 'Alex Brush', cursive;
            color: {get_random_color()};
        }}
    </style>
    <div id="hover-name" class="hover-name">Siddharth Patel</div>
"""

t1.markdown(color_changing_name + color_changing_script, unsafe_allow_html=True)
#t2.markdown(color_changing_name + color_changing_script, unsafe_allow_html=True)
#t3.markdown(color_changing_name + color_changing_script, unsafe_allow_html=True)
#t4.markdown(color_changing_name + color_changing_script, unsafe_allow_html=True)
#t5.markdown(color_changing_name + color_changing_script, unsafe_allow_html=True)

t1.title(":orange[About Me🙋‍♂️]")
b1, b2 = t1.columns([3, 1])
b1.write('''I am a passionate and dedicated Bachelor of Computer Applications (BCA) student with a strong
            foundation in computer science, programming, and software development. I thrive on learning and
            applying emerging technologies to solve real-world challenges, consistently aiming to innovate and
            excel in the dynamic IT landscape.''')
b2.image("WhatsApp Image 2022-12-17 at 20.57.24.jpg", width=200)
b1.write('''A motivated and skilled Bachelor of Computer Applications graduate with a strong
foundation in software development, programming languages, and emerging
technologies. Passionate about creating innovative technological solutions and 
continuously expanding technical expertise through hands-on projects and learning.''')

t2.title(":orange[Experience💼]")
t2.write('''As a passionate BCA student, I have developed a strong foundation in computer applications,
         programming, and problem-solving. While I do not have formal work experience, I have actively
         engaged in academic projects, coursework, and personal initiatives that showcase my technical and
         collaborative skills.''')

t3.header(":orange[Project🎯]")
t3.write('''As a BCA (Bachelor of Computer Applications) student, I am in the process of building a strong
         foundation in programming, database management, and software development. While I do not
         yet have formal projects to showcase, my coursework and personal learning initiatives have
         equipped me with the skills and knowledge to undertake meaningful projects in the future.''')

t3.header(":orange[Future Project Aspirations🔮]")
t3.write('''I am eager to apply my skills to real-world projects and am actively exploring opportunities to:
           ➡️Develop applications that solve everyday problems,
          Work on collaborative team projects to gain practical experience in software development.
         Build dynamic websites and mobile apps using advanced technologies.''')

t4.title(":orange[Education📖]")
t4.header(":green[Bachelor of Computer Applications (BCA)💻]")
t4.write('''Developed a strong foundation in programming, database management, software development, and web technologies.
             Studied core subjects including Data Structures, Operating Systems, Networking, Software Engineering, and Object-Oriented Programming.
             Participated in workshops, seminars, and tech events to enhance technical and professional knowledge.''')

t4.header(":green[Achievements🏆]")
t4.write(''':red[Second Runner-Up – Internal Hackathon]
            Recognized as part of the second runner-up team in an internal college hackathon.
         This experience honed my skills in teamwork, critical thinking, and quick problem-solving under pressure.''')
t4.link_button("👨‍💻Go to Hackathon Gallery👨‍💻", "https://photos.app.goo.gl/EXJaznETNTwaJ5NJ6")

t4.header(":green[Certification🏅]")
t4.write('''1.) I am thrilled to announce the completion of my User Interface (UI) Design Certification in Figma! This
         certification has strengthened my ability to create visually appealing, user-friendly, and functional digital
         interfaces.''')
t4.link_button("🎓Go to my certificate🎓", "https://simpli-web.app.link/e/dEdG1cri7Qb")

t5.header(":orange[Contact ☎️]")
t5.write('''Whether you have a question, a project collaboration, or a professional opportunity, feel free to reach out to me.''')
t5.subheader(":red[Get in Touch👆🏼]")
t5.info("Contact me any time")
t5.link_button("💻Linkedin", "https://www.linkedin.com/in/siddharth-patel-108581304/")
t5.link_button("📧Email", "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=new")
t5.write("📱+91 70848 99321")
