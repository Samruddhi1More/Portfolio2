import streamlit as st

st.set_page_config(layout="wide")

# ---- NAVBAR ----
st.markdown(
    """
    <style>
    .navbar {
        display: flex;
        justify-content: right;
        gap: 30px;
        background-color: #111;
        padding: 15px 25px;
        font-size: 18px;
        font-weight: bold;
    }
    .navbar a {
        text-decoration: none;
        color: white;
    }
    .navbar a:hover {
        color: #00c0f0;
    }
    .heading {
        font-size: 50px;
        font-weight: bold;
        background: linear-gradient(90deg, #ff6ec4, #ff9a9e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: left;
        margin: 5px 0;
    }
    .heading2 {
        font-size: 32px;
        background: linear-gradient(90deg, #ff6ec4, #ff9a9e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: left;
    }
    .gradient-gray {
        font-size: 18px;
        background: linear-gradient(90deg, #b0b0b0, #e0e0e0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>

    <div class="navbar">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#projects">Projects</a>
        <a href="#industries">Industries</a>
        <a href="#skills">Skills</a>
        <a href="#education">Education</a>
        <a href="#contact">Contact</a>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- SECTIONS ----
st.markdown("<h3 class='heading'>Samruddhi More</h3>", unsafe_allow_html=True)

col1,col2,col3 = st.columns([4,3,3])
with col2:
    st.markdown("<h3 id='home'>Home</h3>", unsafe_allow_html=True)

with col1:
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.markdown("<h3 class='heading2'>Hello, I'm </h3>",unsafe_allow_html=True)
    st.markdown("<h1>Samruddhi More</h1>",unsafe_allow_html=True)
    st.markdown("<h3 class='heading2'>Machine Learning Engineer</h3>", unsafe_allow_html=True)
    st.markdown("<p class='gradient-gray'>Specializing in AI-powered solutions, chatbots, computer vision, and data science to solve complex problems.</p>",unsafe_allow_html=True)
    left,middle,right = st.columns(3)
    with left:
        st.markdown(
    """
    <a href="#contact">
        <button style="
            background: none;
            border: 2px solid #ff6ec4;
            border-radius: 12px;
            padding: 12px 28px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
            background-image: linear-gradient(90deg, #ff6ec4, #ff9a9e);
        ">
            Get in Touch
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )
    with middle:
        st.markdown(
    """
    <a href="#projects">
        <button style="
            background: none;
            border: 2px solid #ff6ec4;
            border-radius: 12px;
            padding: 12px 28px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
            background-image: linear-gradient(90deg, #ff6ec4, #ff9a9e);
        ">
            View Projects
        </button>
    </a>
    """,
    unsafe_allow_html=True
    )
    with right:
        st.markdown(
    """
    <a href="static/Resume_Samruddhi More (7).pdf" target="_blank" style="text-decoration: none;">
        <button style="
            background: none;
            border: 2px solid #ff6ec4;
            border-radius: 12px;
            padding: 12px 28px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
            background-image: linear-gradient(90deg, #ff6ec4, #ff9a9e);
        ">
            View Resume
        </button>
    </a>
    """,
    unsafe_allow_html=True
)



st.markdown("<h1 id='about'>🙋 About</h1>", unsafe_allow_html=True)
st.write("I am a Machine Learning Engineer with expertise in ...")

st.markdown("<h1 id='projects'>💻 Projects</h1>", unsafe_allow_html=True)
st.write("1. Project A\n2. Project B")

st.markdown("<h1 id='industries'></h1>", unsafe_allow_html=True)
st.write("Worked in AI, Data Science, Security Surveillance...")

with col2:
    st.markdown("<h1 id='skills'>🛠️ Skills</h1>", unsafe_allow_html=True)
    st.write("Python, PyTorch, Streamlit, AWS...")

st.markdown("<h1 id='education'>🎓 Education</h1>", unsafe_allow_html=True)
st.write("Bachelor in Data Science - Symbiosis Skills and Professional University")

st.markdown("<h1 id='contact'>📩 Contact</h1>", unsafe_allow_html=True)
st.write("Email: yourname@email.com")
