import streamlit as st
from chatbot_backend import chatbot, get_all_threads
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import uuid



# ************ || utility functions || ************
def generate_thread_id():
   return uuid.uuid4()


def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    return state.values.get('messages', [])


# ************ || Sidebar || ************

def reset_chat():
    st.session_state['thread_id'] = generate_thread_id()
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []



st.sidebar.title("Luffy Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()


st.sidebar.header("My Conversations")


# ************ || Session Setup || ************

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = [] 


if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = get_all_threads()

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()


add_thread(st.session_state['thread_id'] )
CONFIG = {'configurable': {"thread_id": st.session_state['thread_id']}}

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)

        temp_messages = []

        for message in messages:
            
            if isinstance(message, HumanMessage):
                role = 'user'
            elif isinstance(message, AIMessage):
                role = "assistant"
            else:
                continue

            if not message.content:
                continue

            temp_messages.append({"role": role, "content": message.content})

        st.session_state['message_history'] = temp_messages

# ************ Chatbot ***********************************


for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


user_input = st.chat_input('Type here')

if user_input:


    st.session_state['message_history'].append({
            "role": "user",
            "content": user_input
    })
    with st.chat_message('user'):
        st.text(user_input)

    

    with st.chat_message('assistant'):

        status_holder = {"box": None}

        def ai_only_stream():
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]}, 
                stream_mode='messages',
                config=CONFIG
            ):
                if isinstance(message_chunk, ToolMessage):
                    tool_name = getattr(message_chunk, "name", "tool")
                    if status_holder["box"] is None:
                        status_holder['box'] = st.status(
                            f"🔧 Using `{tool_name}` …", expanded=True
                        )
                    else:
                        status_holder["box"].update(
                            label=f"🔧 Using `{tool_name}` …",
                            state="running",
                            expanded=True,
                        )


                if isinstance(message_chunk, AIMessage):
                    yield message_chunk.content
        

        ai_message = st.write_stream(ai_only_stream())

         # Finalize only if a tool was actually used
        if status_holder["box"] is not None:
            status_holder["box"].update(
                label="✅ Tool finished", state="complete", expanded=False
            )

    
    st.session_state['message_history'].append({
            "role": "assistant",
            "content": ai_message
    })