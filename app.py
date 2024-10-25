import streamlit as st
import numpy as np

# Function to generate random predictions
def predict_outcome_random():
    prediction = np.random.randint(2)  # 0 or 1
    prob = np.random.random()  # Random probability between 0 and 1
    return prediction, prob

# Function to provide personalized diet recommendations based on the probability of diabetes
def personalized_diet(prob):
    if 0.0 <= prob < 0.10:
        return """
        **Diet for Very Low Risk (0-10% Probability):**
        - Maintain a balanced diet with diverse food groups.
        - Engage in regular physical activity.
        - Monitor portion sizes to avoid overeating.
        - Stay hydrated with water rather than sugary drinks.
        - Limit intake of processed foods.
        """
    elif 0.10 <= prob < 0.20:
        return """
        **Diet for Low Risk (10-20% Probability):**
        - Increase fiber intake with whole grains, fruits, and vegetables.
        - Choose lean protein sources like chicken, fish, and legumes.
        - Reduce salt intake to maintain healthy blood pressure.
        - Opt for healthy fats, such as those found in nuts and olive oil.
        - Ensure regular consumption of dairy products or alternatives.
        """
    elif 0.20 <= prob < 0.30:
        return """
        **Diet for Mild Risk (20-30% Probability):**
        - Incorporate more anti-inflammatory foods like tomatoes and olive oil.
        - Use herbs and spices instead of salt for flavoring.
        - Drink green tea, known for its antioxidant properties.
        - Avoid fried foods and choose cooking methods like baking or steaming.
        - Focus on whole fruits instead of juices to reduce sugar intake.
        """
    elif 0.30 <= prob < 0.40:
        return """
        **Diet for Moderate Risk (30-40% Probability):**
        - Emphasize low-glycemic index foods to stabilize blood sugar.
        - Limit consumption of high-sugar foods and beverages.
        - Eat regular meals and snacks to prevent blood sugar spikes.
        - Include magnesium-rich foods like leafy greens and whole grains.
        - Reduce the consumption of red meats and opt for fish or poultry.
        """
    elif 0.40 <= prob < 0.50:
        return """
        **Diet for High Risk (40-50% Probability):**
        - Prioritize plant-based proteins and reduce animal fats.
        - Incorporate foods high in omega-3 fatty acids, like salmon and flaxseeds.
        - Limit alcoholic beverages and sugary drinks.
        - Adopt a Mediterranean diet focusing on vegetables, grains, and olive oil.
        - Manage stress levels as part of a holistic approach to health.
        """
    elif 0.50 <= prob < 0.60:
        return """
        **Diet for Higher Risk (50-60% Probability):**
        - Focus on weight management through balanced meals.
        - Increase physical activity to improve metabolic health.
        - Consider a consultation with a dietitian for personalized advice.
        - Monitor blood sugar levels regularly if at risk or diabetic.
        - Explore diabetic-friendly recipes that are low in carbohydrates.
        """
    elif 0.60 <= prob < 0.70:
        return """
        **Diet for Very High Risk (60-70% Probability):**
        - Avoid fast foods and high-calorie snacks.
        - Check blood glucose levels regularly.
        - Plan meals ahead to make healthy choices easier.
        - Consider portion control as a tool to manage calorie intake.
        - Stay informed about new research on diabetes management.
        """
    elif 0.70 <= prob < 0.80:
        return """
        **Diet for Severe Risk (70-80% Probability):**
        - Eliminate sugary desserts and snacks.
        - Incorporate aerobic and resistance training into your routine.
        - Use meal replacements under medical supervision for weight control.
        - Educate yourself on carbohydrate counting.
        - Regular medical check-ups to monitor health indicators.
        """
    elif 0.80 <= prob < 0.90:
        return """
        **Diet for Critical Risk (80-90% Probability):**
        - Adopt a strict low-carb diet to manage blood sugar levels.
        - Regular consultations with endocrinologists and nutritionists.
        - Engage in daily physical activity tailored to individual capacity.
        - Consider medically supervised programs for lifestyle intervention.
        - Regularly monitor and adjust medication under medical supervision.
        """
    elif 0.90 <= prob <= 1.00:
        return """
        **Diet for Extreme Risk (90-100% Probability):**
        - Follow a diabetic diet plan prescribed by healthcare professionals.
        - Regular insulin level checks and adjustments.
        - Continuous education on diabetes management and complication prevention.
        - Implement advanced carbohydrate management techniques.
        - Participation in support groups or counseling for ongoing support.
        """
    return "Check your inputs and try again."

# Read the Base64 image data from a file
def load_base64_image(path):
    with open(path, "r") as file:
        return file.read()

base64_image = load_base64_image("C:/Users/krish/Downloads/Diabetes project/app.base64")

# Using Streamlit's markdown to apply custom CSS directly
st.markdown(f"""
<style>
html, body, [class*="View"] {{
    height: 100%;
    margin: 0;
    color: #FFFFFF; /* White text for better readability */
    background-image: url("data:image/jpg;base64,{base64_image}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
.stTextInput > div > div > input, .stNumberInput > input {{
    color: #000000; /* Black text color for input fields */
    background-color: #FFFFFF; /* White background for input fields */
    border: 1px solid #000000; /* Black border for input fields */
}}
.stButton > button {{
    color: #000000; /* Black text color for buttons */
    background-color: #FFFFFF; /* White background for buttons */
    border-radius: 10px;
    border: 2px solid #000000; /* Black border for buttons */
    padding: 10px 24px;
}}
</style>
""", unsafe_allow_html=True)


st.title('Diabetes Prediction')

# Layout of input fields
col1, col2, col3 = st.columns(3)
with col1:
    pregnancies = st.number_input('Pregnancies', min_value=0, step=1)
with col2:
    glucose = st.number_input('Glucose', min_value=0)
with col3:
    blood_pressure = st.number_input('Blood Pressure', min_value=0)

col1, col2, col3 = st.columns(3)
with col1:
    skin_thickness = st.number_input('Skin Thickness', min_value=0)
with col2:
    insulin = st.number_input('Insulin', min_value=0)
with col3:
    bmi = st.number_input('BMI', min_value=0.0)

dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0)
age = st.number_input('Age', min_value=0, step=1)

if st.button('Predict'):
    prediction, prob = predict_outcome_random()
    st.success(f"Diabetes detected with a probability of {prob:.2f}" if prediction == 1 else f"No diabetes detected with a probability of {1 - prob:.2f}.")
    diet_rec = personalized_diet(prob)
    st.markdown(diet_rec, unsafe_allow_html=True)