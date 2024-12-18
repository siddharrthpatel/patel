import streamlit as st
c1,c2,c3 = st.columns([1,4,1])
t1,t2,t3,t4,t5=st.tabs(["Home🏠","Experience💼","Project🎯","Education🎓","Conatact Me📞"])
#home=st.button("Home")
#conatct=st.button("Conatact Me")

t1.title("About Me🙋‍♂️")
b1,b2=t1.columns([3,1])
b1.write('''I am a passionate and dedicated Bachelor of Computer Applications (BCA) student with a strong
            foundation in computer science, programming, and software development. I thrive on learning and
            applying emerging technologies to solve real-world challenges, consistently aiming to innovate and
            excel in the dynamic IT landscape.''')
b2.image("WhatsApp Image 2022-12-17 at 20.57.24.jpg",width=200)
b1.write('''A motivated and skilled Bachelor of Computer Applications graduate with a strong
foundation in software development, programming languages, and emerging
technologies. Passionate about creating innovative technological solutions and 
continuously expanding technical expertise through hands-on projects and learning.''')
