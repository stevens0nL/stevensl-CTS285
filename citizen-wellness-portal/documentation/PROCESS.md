## PROCESS.md
LLM-Assisted Prompts
As per the AI-Assisted Learning Protocol, I used Claude (via Anthropic's API) to learn Streamlit concepts. I started with zero prior knowledge, simulating the learning process. Below are the prompts I used, iterations, challenges, and reflections. I compared Streamlit to Flask throughout.

### Prompt 1: 
```
I know Flask but not Streamlit. Explain Streamlit's execution model—how does it differ from Flask's request/response cycle? What happens when a user clicks a button? Give a simple hello world example.
AI Response Summ.: Streamlit runs top-to-bottom on every interaction (rerun), unlike Flask's request/response. Buttons trigger reruns, not callbacks. Example: st.write("Hello, World!").
```
Error: This felt inefficient vs. Flask's routing. Resolution: Accepted it for rapid prototyping; documented that Streamlit trades control for speed.

### Prompt 3:
```
Show me how to create a login form in Streamlit with username and password fields. How do I handle form submission? What's the equivalent of Flask's session management?
AI Response Summary: Use st.text_input, st.button, and st.session_state for persistence. On button click, check logic and update state.
```
Iteration 1: Code didn't persist across reruns. Prompt: "My login form resets after submission. How to fix with session_state?" (AI: Use keys and conditional rendering.)

Iteration 2: Added registration. Prompt: "How to add a registration tab? Should I use st.tabs?" (Yes, with validation.)

Error(s): Password storage. AI suggested in-memory dict but I iterated to add basic validation. Resolution: Added checks for empty fields and duplicates.

Comparison Note: Flask sessions are server-side; Streamlit's session_state is per-user, client-side-ish but managed by Streamlit.

Prompt 3:
```
I need a dashboard that shows after login. How to conditionally render views? Also, add mock metrics with progress bars.
AI Response Summary: Use if st.session_state.logged_in: for conditional rendering. For bars: st.progress(value) or custom text bars.
```
Error: Logout didn't clear state properly. Resolution: Explicitly reset session_state keys.

Prompt 4:
```
I need login, register, and dashboard. Should I use st.tabs, st.sidebar, or multipage? Tradeoffs?
AI Response Summary: Tabs for simple apps like this; multipage for complex. Tradeoffs: Tabs are fast but all in one file; multipage scales better.
```
Overall notes: Balancing simplicity with functionality. Resolved by iterating prompts for edge cases (e.g., invalid login).


Total LLM Interactions: ~15 prompts over sessions. I refined code based on responses, making sure I understood each part before integrating.

