import streamlit as st
import requests
import time

st.set_page_config(
    page_title="Chat avec Lina - AI Research Engineer",
    page_icon="🤖",
    layout="wide"
)

def get_lina_profile_info(info_type: str) -> str:
    """
    Get accurate information about Lina Farchado's professional profile.

    Args:
        info_type: Type of information requested ('experience', 'education', 'skills', 'projects', 'contact', 'overview')
    Returns:
        Formatted accurate information from Lina's CV
    """
    profile_data = {
        "overview": {
            "title": "Machine Learning Engineer",
            "expertise": "Generative modeling, computer vision, and production system deployment",
            "experience_summary": "Proven track record building end-to-end ML pipelines from research prototyping to scalable applications serving millions of requests",
            "passion": "Transforming complex data challenges into impactful, production-ready solutions while continuously expanding technical expertise across emerging AI domains"
        },
        "experience": {
            "current": {
                "role": "R&D Intern in AI for Medical Imaging",
                "company": "GE Healthcare France",
                "period": "February 2025 – August 2025",
                "achievements": [
                    "Developed 3+ super-resolution models for CT scan enhancement, achieving up to 14% PSNR improvement and 12% SSIM improvement over bicubic interpolation baseline",
                    "Integrated models into browser-based inference pipeline using ONNX.js and WebGPU, enabling real-time processing",
                    "Built interactive dashboards for model performance monitoring and clinical validation across deployment environments",
                    "Ensured clinical-grade standards through robust testing and validation in constrained medical imaging contexts"
                ]
            },
            "previous": {
                "role": "Full-Stack Engineering Intern",
                "company": "CastorDoc France",
                "period": "September 2023 – January 2024",
                "achievements": [
                    "Shipped 20+ major features including External Links API serving 1M+ calls/month and Chrome Extension used by 300+ users",
                    "Added 100+ unit and integration tests across TypeScript/React/Node.js codebase ensuring robust code quality",
                    "Collaborated in an Agile/Scrum environment with cross-functional teams, participating in explorations, code reviews, and sprint planning"
                ]
            }
        },
        "education": {
            "institution": "EPITA School of Engineering and Computer Science",
            "location": "Paris, France",
            "degree": "MSc in Computer Science - AI & Data Science Specialization",
            "gpa": "3.9/4.0",
            "period": "2020 – 2025"
        },
        "projects": {
            "brain_mri": {
                "title": "Brain MRI Generation",
                "type": "Research Project",
                "technologies": "Generative models, PyTorch, Segmentation",
                "period": "February 2024 – January 2025",
                "achievements": [
                    "Engineered generative AI pipeline processing 3D MRI volumes, increasing dataset size by 3x through synthetic data generation",
                    "Achieved up to 70% improvement in white matter segmentation accuracy and 40% in gray matter through optimized synthetic data generation pipeline",
                    "Validated synthetic data quality through downstream segmentation tasks, achieving clinical-grade performance on medical imaging benchmarks"
                ]
            },
            "ai_image_service": {
                "title": "AI Image Generation Web Service and Discord Bot",
                "type": "Group Project",
                "technologies": "Hugging Face, Flask, Docker, CUDA, MLOps",
                "period": "December 2024 – January 2025",
                "achievements": [
                    "Deployed production-ready text-to-image service using Stability AI's SDXL Turbo model supporting unlimited simultaneous users",
                    "Implemented multi-threaded architecture for handling parallel requests with seamless concurrent processing",
                    "Optimized inference pipeline achieving consistent 30-second response times for AI-generated images"
                ]
            },
            "hackathon_winner": {
                "title": "AI vs Human Text Classification - Hackathon Winner",
                "type": "IA Data Hack",
                "technologies": "CNN, Transformer, PyTorch, NLP",
                "period": "February 2024",
                "achievements": [
                    "Led 4-person cross-functional team to develop award-winning AI solution within 48-hour constraint",
                    "Secured 1st place victory among 30+ competing teams through technical excellence and innovative approach",
                    "Benchmarked 4+ deep learning architectures: 1D-adapted CNN and custom mini-transformer models"
                ]
            },
            "stock_market_dashboard": {
                "title": "Stock Market Data Pipeline and Dashboard",
                "type": "Group Project",
                "technologies": "SQL, TimescaleDB, Docker, Dash",
                "period": "March – June 2024",
                "achievements": [
                    "Designed and implemented a full data pipeline to clean, process, and batch-load large-scale stock market data into a TimescaleDB time-series database",
                    "Built an interactive dashboard with Dash to visualize market trends, compare multiple companies, and analyze data using various formats"
                ]
            },
            "bomberman_backend": {
                "title": "JWS - Online Bomberman Game Backend",
                "type": "Solo Project",
                "technologies": "Java, Quarkus, Hibernate, PostgreSQL, Maven",
                "period": "February 2023",
                "achievements": [
                    "Developed a REST API backend for an online multiplayer Bomberman game following layered architecture principles (data, domain, presentation layers)",
                    "Implemented core game mechanics including player movement, bomb placement/explosion, game state management, and turn-based gameplay",
                    "Built multiple REST endpoints for game creation, player management, game state retrieval, and player actions using Quarkus framework",
                    "Designed and implemented database schema with Hibernate ORM for persistent storage of games, players, and game maps in PostgreSQL"
                ]
            },
            "film_recommender": {
                "title": "Film Recommender System",
                "type": "Solo Project",
                "technologies": "Scikit-learn, Pandas, SQL, IMDb",
                "period": "July 2024",
                "achievements": [
                    "Integrated and cleaned movie ratings, metadata, and IMDb data into a unified database for accurate and scalable recommendation generation",
                    "Engineered features and implemented hybrid recommendation algorithm combining SVD-based collaborative filtering and content-based similarity"
                ]
            }
        },
        "skills": {
            "languages": ["English", "French", "Arabic"],
            "programming": ["Python", "Javascript", "Typescript", "HTML/CSS", "SQL", "PostgreSQL", "No SQL"],
            "frameworks": ["React", "Jest", "Flask", "PyTest", "PyTorch", "TensorFlow", "Pandas", "Scikit-learn", "OpenCV"],
            "tools": ["Git", "GitHub Actions", "CI/CD", "Docker"]
        },
        "contact": {
            "phone": "+33 6 69 22 60 47",
            "email": "l.farchado@gmail.com",
            "linkedin": "linkedin.com/in/lina-farchado",
            "github": "Github"
        }
    }
    
    info = profile_data.get(info_type.lower())
    if not info:
        return f"Information type '{info_type}' not available. Available types: experience, education, skills, projects, contact, overview"

    if info_type.lower() == "overview":
        return f"Professional Overview - Lina Farchado:\n\n" \
               f"• Title: {info['title']}\n" \
               f"• Expertise: {info['expertise']}\n" \
               f"• Experience: {info['experience_summary']}\n" \
               f"• Focus: {info['passion']}"
    
    elif info_type.lower() == "experience":
        current = info['current']
        previous = info['previous']
        result = f"Professional Experience - Lina Farchado:\n\n"
        result += f"Current Position:\n• {current['role']} at {current['company']} ({current['period']})\n"
        for achievement in current['achievements']:
            result += f"  - {achievement}\n"
        result += f"\nPrevious Position:\n• {previous['role']} at {previous['company']} ({previous['period']})\n"
        for achievement in previous['achievements']:
            result += f"  - {achievement}\n"
        return result
    
    elif info_type.lower() == "education":
        return f"Education - Lina Farchado:\n\n" \
               f"• Institution: {info['institution']}\n" \
               f"• Location: {info['location']}\n" \
               f"• Degree: {info['degree']}\n" \
               f"• GPA: {info['gpa']}\n" \
               f"• Period: {info['period']}"
    
    elif info_type.lower() == "projects":
        result = "Key Projects - Lina Farchado:\n\n"
        for project_key, project in info.items():
            result += f"• {project['title']} ({project['period']})\n"
            result += f"  Type: {project['type']}\n"
            result += f"  Technologies: {project['technologies']}\n"
            for achievement in project['achievements']:
                result += f"  - {achievement}\n"
            result += "\n"
        return result
    
    elif info_type.lower() == "skills":
        return f"Technical Skills - Lina Farchado:\n\n" \
               f"• Languages: {', '.join(info['languages'])}\n" \
               f"• Programming: {', '.join(info['programming'])}\n" \
               f"• Frameworks & Libraries: {', '.join(info['frameworks'])}\n" \
               f"• Developer Tools: {', '.join(info['tools'])}"
    
    elif info_type.lower() == "contact":
        return f"Contact Information - Lina Farchado:\n\n" \
               f"• Phone: {info['phone']}\n" \
               f"• Email: {info['email']}\n" \
               f"• LinkedIn: {info['linkedin']}\n" \
               f"• GitHub: {info['github']}"
    
    return str(info)

def get_context_for_prompt(prompt: str) -> str:
    """Détermine quel contexte utiliser selon la question"""
    prompt_lower = prompt.lower()
    
    if any(word in prompt_lower for word in ["projet", "project"]):
        return get_lina_profile_info("projects")
    elif any(word in prompt_lower for word in ["expérience", "experience", "travail", "poste"]):
        return get_lina_profile_info("experience")
    elif any(word in prompt_lower for word in ["compétence", "skill", "technologie", "outil"]):
        return get_lina_profile_info("skills")
    elif any(word in prompt_lower for word in ["formation", "education", "diplôme", "école"]):
        return get_lina_profile_info("education")
    elif any(word in prompt_lower for word in ["contact", "email", "téléphone", "linkedin"]):
        return get_lina_profile_info("contact")
    else:
        # Contexte général pour toute autre question
        return get_lina_profile_info("overview")

def call_huggingface_llm(prompt: str) -> str:
    """Utilise un vrai LLM gratuit de HuggingFace avec le vrai contexte"""
    
    # Récupérer le contexte approprié selon la question
    relevant_context = get_context_for_prompt(prompt)
    
    # Instructions système avec le vrai contexte
    context = f"""Tu es l'assistant de Lina FARCHADO. Réponds UNIQUEMENT en français ou anglais, de manière concise.

Informations professionnelles de Lina :
{relevant_context}

IMPORTANT: Réponds toujours en français, sois bref et factuel."""

    try:
        API_URL = "https://router.huggingface.co/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {st.secrets['HF_TOKEN']}",
        }
        
        payload = {
            "model": "deepseek-ai/DeepSeek-V3",
            "messages": [
                {"role": "system", "content": context},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 700,
            "temperature": 0.4
        }
        
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        
        elif response.status_code == 503:
            return "⏳ Le modèle se charge... Réessayez dans quelques secondes."
        
        else:
            return f"Erreur API: {response.status_code} - {response.text}"
            
    except requests.exceptions.Timeout:
        return "⏱️ Timeout - Réessayez avec une question plus courte."
    except Exception as e:
        return f"Erreur: {str(e)}"

def fallback_response(prompt: str) -> str:
    """Réponse de secours avec vraies données"""
    prompt_lower = prompt.lower()
    
    if "compétence" in prompt_lower or "skill" in prompt_lower:
        return get_lina_profile_info("skills")
    elif "projet" in prompt_lower:
        return get_lina_profile_info("projects")
    elif "expérience" in prompt_lower:
        return get_lina_profile_info("experience")
    elif "formation" in prompt_lower or "education" in prompt_lower:
        return get_lina_profile_info("education")
    else:
        return get_lina_profile_info("overview")

def get_response(prompt: str) -> str:
    """Génère réponse avec LLM + fallback"""
    
    # Pour questions très simples, pas besoin du LLM
    prompt_lower = prompt.lower()
    if any(word in prompt_lower for word in ["bonjour", "salut", "hello"]):
        return "Bonjour ! Je suis l'assistant de Lina, Machine Learning Engineer. Que voulez-vous savoir sur son profil ?"
    
    # Utiliser le LLM pour réponses élaborées
    with st.spinner("🤖 Génération avec DeepSeek-V3..."):
        llm_response = call_huggingface_llm(prompt)
        
        if llm_response is None or llm_response == "":
            return f"**Réponse de secours :** {fallback_response(prompt)}"
        
        # Si LLM échoue, utiliser fallback
        if any(word in llm_response.lower() for word in ["erreur", "timeout", "charge"]):
            return f"{llm_response}\n\n**Réponse alternative :** {fallback_response(prompt)}"
        
        return llm_response

# Interface
st.title("🤖 Chat avec Lina")
st.subheader("Machine Learning Engineer - Portfolio Assistant")

# Informations sur le modèle
st.info("🧠 **Powered by DeepSeek-V3** - LLM gratuit HuggingFace")

with st.sidebar:
    st.markdown("### 👩‍💻 Lina FARCHADO")
    st.markdown("**Machine Learning Engineer**")
    st.markdown("🐍 Python • PyTorch • TensorFlow")
    st.markdown("🤖 AI Research • Medical Imaging")  
    st.markdown("🏥 GE Healthcare • CastorDoc")
    st.markdown("🎓 EPITA - AI & Data Science")
    
    st.markdown("---")
    st.markdown("**🧠 Modèle IA :**")
    st.markdown("**DeepSeek-V3**")
    st.markdown("- 3 milliards de paramètres")
    st.markdown("- Spécialisé instruction")
    st.markdown("- API gratuite HuggingFace")
    
    if st.button("🔄 Reset"):
        st.session_state.messages = []
        st.rerun()

# Messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Bonjour ! Je suis l'assistant IA de **Lina FARCHADO**, Machine Learning Engineer, propulsé par **DeepSeek-V3**.\n\nPosez-moi vos questions sur son profil professionnel !"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Votre question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        response = get_response(prompt)
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("---")
st.markdown("🤖 *DeepSeek-V3 via HuggingFace Inference API - Gratuit*")