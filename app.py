import streamlit as st

# ----------------------------------------
# Drone Chatbot Classes (same logic as yours)
# ----------------------------------------

class Greeting:
    def __init__(self, name):
        self.name = name

class ChatBot(Greeting):
    def __init__(self, name):
        super().__init__(name)

class DroneChatBot(ChatBot):
    def __init__(self, name):
        super().__init__(name)
        self.answers = {
            "flight time": "28-32 minutes per battery (depends on wind & payload).",
            "range": "6-8 kilometers with clear line of sight.",
            "gps": "Yes — built-in GPS + GLONASS.",
            "camera": "4K Ultra HD camera (30 fps) with 3-axis gimbal.",
            "camera removable": "Yes — camera is removable and upgradeable.",
            "payload": "500-700 grams safely without affecting stability.",
            "speed": "Up to 60 km/h (Sport Mode).",
            "weather": "Weather-resistant (IP43): light rain & dust okay, not waterproof.",
            "fpv": "Yes — supports FPV (First Person View).",
            "in the box": "Drone, remote, battery, charger, spare props, manual."
        }

    def get_response(self, text):
        text = text.lower()
        for key, ans in self.answers.items():
            if key in text:
                return ans
        return "❗ Please ask about drone specs (flight time, range, GPS, camera, payload, etc.)."

    def suggestions(self):
        return list(self.answers.keys())


# ----------------------------------------
# Streamlit UI
# ----------------------------------------

bot = DroneChatBot("AeroBot")

st.title("🚁 AeroBot – Drone FAQ Chatbot")
st.write("Ask me anything about this drone.")

st.markdown("### **Suggestions:**")
for s in bot.suggestions():
    st.markdown(f"- **{s}**")

# Chat input
user_input = st.text_input("You:")

if user_input:
    response = bot.get_response(user_input)
    st.markdown(f"### 🤖 Bot: {response}")
