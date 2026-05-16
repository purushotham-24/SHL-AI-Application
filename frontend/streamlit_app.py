import streamlit as st
import requests
import pandas as pd

API_URL = "https://shl-ai-application.onrender.com/chat"
 
# Page Configuration
st.set_page_config(
    page_title="SHL AI Assessment Recommendation System",
    page_icon="🤖",
    layout="wide"
)

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:

    st.title("SHL AI")

    st.markdown("### Assessment Recommendation System")

    st.markdown("---")

    st.markdown("### Sample Queries")

    st.markdown("""
    - Hiring senior Java backend engineer
    - Hiring graduate financial analysts
    - Need leadership assessments for CXOs
    - Hiring contact center agents
    - Hiring plant operators for chemical facility
    """)

    st.markdown("---")

    st.info(
        "AI-powered conversational recommendation system for SHL assessments."
    )

# Main Header
st.title("🤖 SHL AI Assessment Recommendation System")

st.markdown(
    "Describe your hiring requirements and receive recommended SHL assessments instantly."
)

st.info(
    "Ask hiring-related questions to receive conversational SHL assessment recommendations."
)

# Display Previous Messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# Chat Input
prompt = st.chat_input(
    "Example: Hiring graduate financial analysts"
)

if prompt:

    # Store User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display User Message
    with st.chat_message("user"):

        st.markdown(prompt)

    # Assistant Response
    with st.chat_message("assistant"):

        with st.spinner("Generating recommendations..."):

            payload = {
                "messages": st.session_state.messages
            }

            try:

                response = requests.post(
                    API_URL,
                    json=payload
                )

                data = response.json()

                reply = data.get(
                    "reply",
                    "No response generated."
                )

                recommendations = data.get(
                    "recommendations",
                    []
                )

                # Assistant Reply
                st.markdown(reply)

                # Recommendations
                if recommendations:

                    st.markdown("### Recommended Assessments")

                    df = pd.DataFrame(recommendations)

                    st.dataframe(
                        df,
                        use_container_width=True
                    )

                    for item in recommendations:

                        st.markdown(
                            f"""
                            ✅ [{item['name']}]({item['url']})
                            """
                        )

                elif recommendations == []:

                    st.warning(
                        "No recommendations available."
                    )

                # Save Assistant Response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": reply
                    }
                )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )

# Footer
st.markdown("---")

st.caption(
    "Built for SHL Research Intern – AI Application Assignment"
)