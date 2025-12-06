import streamlit as st

# -------------------------------
# Drone Chatbot Logic
# -------------------------------

class DroneChatBot:
    def __init__(self):
        self.name = "AeroBot"
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

        if text in ["bye", "exit", "quit"]:
            return "👋 Goodbye! Thanks for chatting."

        # Greeting phase answer
        if text not in ("y", "n") and st.session_state.phase == "greeting":
            return "❌ Invalid choice.\n📞 Company Helpline: **+1-800-555-1234**"

        # User said No
        if text == "n":
            st.session_state.phase = "end"
            return "Alright! Have a great day! 👋"

        # Switch to question phase
        if text == "y":
            st.session_state.phase = "chat"
            return (
                "Great! You can ask about:\n"
                "- flight time\n- range\n- gps\n- camera\n- camera removable\n"
                "- payload\n- speed\n- weather\n- fpv\n- in the box"
            )

        # Chat phase: look for matching keywords
        if st.session_state.phase == "chat":
            for key, ans in self.answers.items():
                if key in text:
                    return ans
            return "❗ Please ask about drone specs."

        return "I didn't understand that."

# -------------------------------
# Streamlit UI
# -------------------------------

st.title("🚁 AeroBot – Drone FAQ Chatbot")

# Keep chat history
if "history" not in st.session_state:
    st.session_state.history = []
if "phase" not in st.session_state:
    st.session_state.phase = "greeting"   # greeting → chat → end

bot = DroneChatBot()

# Initial greeting message (only once)
if st.session_state.phase == "greeting" and len(st.session_state.history) == 0:
    greeting_text = (
        f"Hello, I am {bot.name}. Would you like to ask me a question about the drone?\n"
        "👉 Enter **y** for Yes\n"
        "👉 Enter **n** for No"
    )
    st.session_state.history.append(("bot", greeting_text))

# Display chat history
for sender, msg in st.session_state.history:
    if sender == "bot":
        st.markdown(f"**🤖 AeroBot:** {msg}")
    else:
        st.markdown(f"**🧑 You:** {msg}")

# Input box
user_input = st.text_input("You:")

if user_input:
    # Save user message
    st.session_state.history.append(("user", user_input))

    # Get bot response
    response = bot.get_response(user_input)

    # Save bot response
    st.session_state.history.append(("bot", response))

    # Force Streamlit to rerun (to show updated chat)
    st.rerun()
