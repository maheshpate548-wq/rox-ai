
import streamlit as st
import ollama

# Page configuration
st.set_page_config(
    page_title="Midnight AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
<style>
.stApp {
    background: #0b0b12;
    color: #f5f5f7;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: #12121c;
    border-right: 1px solid #29293b;
}

.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -1px;
}

.subtitle {
    color: #9999ad;
    font-size: 15px;
}

[data-testid="stChatMessage"] {
    background: #171725;
    border: 1px solid #29293b;
    border-radius: 16px;
    padding: 15px;
    margin-bottom: 12px;
}

[data-testid="stChatInput"] {
    border: 1px solid #7770ff;
    border-radius: 16px;
}

button[kind="primary"] {
    background: #7065ff;
    border: none;
    border-radius: 10px;
}

h1, h2, h3, p {
    color: #f5f5f7;
}

</style>
""", unsafe_allow_html=True)

# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.markdown("## 🤖 MIDNIGHT AI")
    st.caption("Your personal AI workspace")

    st.divider()

    if st.button("＋ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("### Settings")
    st.markdown("🧠 Model: `gemma4:e2b`")
    st.markdown("🟢 Engine: Ollama")
    st.markdown("🔒 Processing: Local")

    st.divider()
    st.caption("Built on your MacBook Air M5")

# Main interface
st.markdown(
    '<div class="main-title">Midnight AI ✨</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">A smarter space for your ideas and conversations.</div>',
    unsafe_allow_html=True
)

st.write("")

# Welcome screen
if not st.session_state.messages:
    st.markdown("### Welcome! 👋")
    st.write("I'm your personal AI assistant. What would you like to explore today?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("💡 **Learn**\n\nUnderstand new topics.")
    with col2:
        st.info("💻 **Create**\n\nWrite code and build projects.")
    with col3:
        st.info("🧠 **Explore**\n\nBrainstorm new ideas.")

# Display conversation
for message in st.session_state.messages:
    avatar = "🧑‍💻" if message["role"] == "user" else "🤖"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Message Midnight AI..."):

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking... ✨"):
            try:
                response = ollama.chat(
                    model="gemma4:e2b",
                    messages=st.session_state.messages
                )

                answer = response["message"]["content"]
                st.markdown(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as e:
                st.error(f"Something went wrong: {e}")
