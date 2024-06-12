import streamlit as st

# Function to fetch suggestions from a dummy dictionary
def fetch_suggestions(query):
    # Simulated API response with hardcoded data
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
    return out

# Initialize session state for input text and suggestions
if 'input_text' not in st.session_state:
    st.session_state.input_text = ""
if 'suggestions' not in st.session_state:
    st.session_state.suggestions = []
if 'selected_suggestion' not in st.session_state:
    st.session_state.selected_suggestion = None

# Main function to render the Streamlit app
def main():
    st.title("Dynamic Textbox with Suggestions")

    # Textbox for input
    input_text = st.text_input("Enter text:", value=st.session_state.input_text, key="input_text")

    st.session_state.suggestions = fetch_suggestions(input_text)
    st.write(fetch_suggestions(input_text))
    
    # Fetch suggestions based on current input text
    if input_text != st.session_state.input_text:
        st.session_state.input_text = input_text
        st.session_state.suggestions = fetch_suggestions(input_text)
        st.session_state.selected_suggestion = None

    # Display dropdown with suggestions
    if st.session_state.suggestions:
        selected_suggestion = st.selectbox(
            "Suggestions:", 
            options=[""] + st.session_state.suggestions, 
            index=0, 
            key="suggestions"
        )

        # Update the textbox with the selected suggestion
        if selected_suggestion and selected_suggestion != st.session_state.selected_suggestion:
            st.session_state.selected_suggestion = selected_suggestion
            st.session_state.input_text = selected_suggestion
            st.experimental_rerun()

if __name__ == "__main__":
    main()
