import streamlit as st
import subprocess
import json

# Function to run diagnosis.pl and capture output
def run_diagnosis(symptoms):
    try:
        # Run diagnosis.pl with symptoms as input
        result = subprocess.run(['perl', 'diagnosis.pl'], input='\n'.join(symptoms), capture_output=True, text=True)
        output = result.stdout.strip()
        return output
    except subprocess.CalledProcessError as e:
        st.error(f"Error running diagnosis: {e}")
        return None

# Main Streamlit app
def main():
    st.title('Diagnosa Kesehatan Mental Remaja')

    # Display form
    st.markdown(open('index.html', 'r', encoding='utf-8').read(), unsafe_allow_html=True)

    # Handle form submission
    if st.button('Diagnosa'):
        selected_symptoms = st.session_state.selected_symptoms
        if selected_symptoms:
            # Run diagnosis.pl with selected symptoms
            result = run_diagnosis(selected_symptoms)
            if result:
                try:
                    # Parse JSON result from diagnosis.pl
                    result_dict = json.loads(result)
                    diagnosis = result_dict.get('diagnosis', '')
                    recommendations = result_dict.get('recommendations', '')

                    # Display diagnosis and recommendations
                    st.header('Hasil Diagnosa:')
                    st.write(f"Diagnosis: {diagnosis}")
                    st.write(f"Rekomendasi: {recommendations}")
                except json.JSONDecodeError as e:
                    st.error(f"Error decoding JSON result: {e}")
            else:
                st.error("Gagal melakukan diagnosa.")
        else:
            st.warning('Silakan pilih setidaknya satu gejala untuk melakukan diagnosa.')

if __name__ == '__main__':
    main()
