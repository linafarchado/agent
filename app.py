import streamlit as st
import requests
import json
from pathlib import Path

st.set_page_config(
    page_title="Chat with Lina - AI Research Engineer",
    page_icon="🤖",
    layout="wide"
)

CONTEXT_KEYWORDS = {
    "projects": ["project", "projects"],
    "experience": ["experience", "work", "job", "position"],
    "skills": ["skills", "skill", "technology", "tools"],
    "education": ["education", "degree", "school", "university"],
    "contact": ["contact", "email", "phone", "linkedin"]
}

FORMATTERS = {
    "overview": lambda data: f"""Professional Overview - Lina Farchado:
• Title: {data['title']}
• Expertise: {data['expertise']}
• Experience: {data['experience_summary']}
• Focus: {data['passion']}""",

    "experience": lambda data: f"""Professional Experience - Lina Farchado:

Current Position:
• {data['current']['role']} at {data['current']['company']} ({data['current']['period']})
{chr(10).join(f"  - {achievement}" for achievement in data['current']['achievements'])}

Previous Position:
• {data['previous']['role']} at {data['previous']['company']} ({data['previous']['period']})
{chr(10).join(f"  - {achievement}" for achievement in data['previous']['achievements'])}""",

    "education": lambda data: f"""Education - Lina Farchado:
• Institution: {data['institution']}
• Location: {data['location']}
• Degree: {data['degree']}
• GPA: {data['gpa']}
• Period: {data['period']}""",

    "skills": lambda data: f"""Technical Skills - Lina Farchado:
• Languages: {', '.join(data['languages'])}
• Programming: {', '.join(data['programming'])}
• Frameworks & Libraries: {', '.join(data['frameworks'])}
• Developer Tools: {', '.join(data['tools'])}""",

    "contact": lambda data: f"""Contact Information - Lina Farchado:
• Phone: {data['phone']}
• Email: {data['email']}
• LinkedIn: {data['linkedin']}
• GitHub: {data['github']}""",

    "projects": lambda data: "Key Projects - Lina Farchado:\n\n" + 
        "\n\n".join(f"""• {project['title']} ({project['period']})
  Type: {project['type']}
  Technologies: {project['technologies']}
{chr(10).join(f"  - {achievement}" for achievement in project['achievements'])}""" 
        for project in data.values())
}

@st.cache_data
def load_profile_data():
    """Loads profile data from JSON with caching"""
    try:
        return json.loads(Path("data.json").read_text(encoding='utf-8'))
    except FileNotFoundError:
        st.error("data.json file not found")
        return {}

def detect_context(prompt):
    """Detects context based on keywords"""
    prompt_lower = prompt.lower()
    for context, keywords in CONTEXT_KEYWORDS.items():
        if any(keyword in prompt_lower for keyword in keywords):
            return context
    return "overview"

def format_profile_info(info_type):
    """Formats profile information"""
    profile_data = load_profile_data()
    if not profile_data or info_type not in profile_data:
        return f"Information '{info_type}' not available"
    
    formatter = FORMATTERS.get(info_type)
    return formatter(profile_data[info_type]) if formatter else str(profile_data[info_type])

def call_huggingface_api(prompt):
    """Optimized HuggingFace API call"""
    context = format_profile_info(detect_context(prompt))
    
    payload = {
        "model": "deepseek-ai/DeepSeek-V3",
        "messages": [
        {"role": "system", "content": f"""You are Lina FARCHADO's assistant. Respond in the same language as the user's question (English or French). Be concise.

{context}

Answer factually and directly."""},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 700,
        "temperature": 0.4
    }
    
    try:
        response = requests.post(
            "https://router.huggingface.co/v1/chat/completions",
            headers={"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"},
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        elif response.status_code == 503:
            return "Model loading, please retry..."
        else:
            return f"API Error: {response.status_code}"
            
    except requests.exceptions.Timeout:
        return "Timeout - Question too long"
    except Exception as e:
        return f"Error: {str(e)}"

def get_response(prompt):
    """Generates final response"""
    if any(word in prompt.lower() for word in ["hello", "hi", "hey"]):
        return "Hello! I'm Lina's assistant, Machine Learning Engineer. What would you like to know about her profile?"
    
    # Use API
    with st.spinner("🤖 Generating..."):
        llm_response = call_huggingface_api(prompt)
        
        if any(word in llm_response.lower() for word in ["error", "timeout", "loading"]):
            fallback = format_profile_info(detect_context(prompt))
            return f"{llm_response}\n\n**Alternative:** {fallback}"
        
        return llm_response

# User interface
st.title("🤖 Chat with Lina")
st.subheader("Machine Learning Engineer - Portfolio Assistant")
st.info("🧠 **Powered by DeepSeek-V3** - Free HuggingFace LLM")

with st.sidebar:
    st.markdown("### 👩‍💻 Lina FARCHADO")
    st.markdown("**Machine Learning Engineer**")
    st.markdown("🐍 Python • PyTorch • TensorFlow")
    st.markdown("🤖 AI Research • Medical Imaging")  
    st.markdown("🏥 GE Healthcare • CastorDoc")
    st.markdown("🎓 EPITA - AI & Data Science")
    
    if st.button("🔄 Reset"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hello! I'm **Lina FARCHADO's** AI assistant, Machine Learning Engineer.\n\nAsk me questions about her professional profile!"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Your question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        response = get_response(prompt)
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("---")
st.markdown("*DeepSeek-V3 via HuggingFace Inference API*")