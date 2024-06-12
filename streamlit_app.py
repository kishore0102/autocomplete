import streamlit as st
import requests

# Function to fetch suggestions from an API
def fetch_suggestions(query):
    # Simulated API response
    data = {
        "status": "SUCCESS",
        "response": {
            "suggestions": [
                {
                    "id": 0,
                    "sentence": "with created time this quarter ",
                    "index_to_replace": 30
                },
                {
                    "id": 0,
                    "sentence": "with modified time this quarter ",
                    "index_to_replace": 30
                },
                {
                    "id": 0,
                    "sentence": "with created time yesterday ",
                    "index_to_replace": 30
                },
                {
                    "id": 0,
                    "sentence": "with created time this year ",
                    "index_to_replace": 30
                },
                {
                    "id": 0,
                    "sentence": "with created time this month ",
                    "index_to_replace": 30
                },
                {
                    "id": 0,
                    "sentence": "with created time today ",
                    "index_to_replace": 30
                }
            ]
        }
    }
    out = []
    for suggestion in data["response"]["suggestions"]:
        out.append(suggestion["sentence"])
    print(out)
    return out

# Initialize session state for input text and suggestions
if 'input_text' not in st.session_state:
    st.session_state.input_text = ""
if 'suggestions' not in st.session_state:
    st.session_state.suggestions = []

# Main function to render the Streamlit app
def main():
    st.title("Dynamic Textbox with Suggestions")

    # Textbox for input
    input_text = st.text_input("Enter text:", value=st.session_state.input_text, key="input_text")

    # Fetch suggestions based on current input text
    suggestions = fetch_suggestions(input_text)
    st.session_state.suggestions = suggestions

    # # Display dropdown with suggestions
    # if suggestions:
    #     selected_suggestion = st.selectbox("Suggestions:", options=suggestions, key="suggestions")

    #     # Update the textbox with the selected suggestion
    #     if selected_suggestion and selected_suggestion != st.session_state.input_text:
    #         st.session_state.input_text = selected_suggestion
    #         st.experimental_rerun()

if __name__ == "__main__":
    main()

