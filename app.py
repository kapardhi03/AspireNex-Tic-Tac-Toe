import streamlit as st
from tictactoe_ai import find_best_move, evaluate, is_moves_left

st.set_page_config(page_title="Tic-Tac-Toe AI", page_icon="🎮", layout="centered")

# Custom CSS for improved styling and mobile responsiveness
st.markdown("""
<style>
    .stButton > button {
        width: 80px;
        height: 80px;
        font-size: 30px !important;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #f0f0f0;
        color: #333;
        border: 2px solid #333;
    }
    .stButton > button:hover {
        background-color: #e0e0e0;
    }
    .game-over {
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
        padding: 10px;
        border-radius: 5px;
    }
    .result-o { background-color: #a8f0a8; color: #0f5f0f; }
    .result-x { background-color: #f0a8a8; color: #5f0f0f; }
    .result-draw { background-color: #f0f0a8; color: #5f5f0f; }
    .player-names {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    @media (max-width: 600px) {
        .stButton > button {
            width: 60px;
            height: 60px;
            font-size: 24px !important;
        }
        .game-over {
            font-size: 18px;
        }
        .player-names {
            font-size: 20px;
        }
    }
</style>
""", unsafe_allow_html=True)

st.title("Tic-Tac-Toe: Human vs. AI")

# Initialize session state variables
if 'board' not in st.session_state:
    st.session_state.board = [[' ' for _ in range(3)] for _ in range(3)]
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'result' not in st.session_state:
    st.session_state.result = None
if 'username' not in st.session_state:
    st.session_state.username = ""

# Function to reset the game
def reset_game():
    st.session_state.board = [[' ' for _ in range(3)] for _ in range(3)]
    st.session_state.game_over = False
    st.session_state.result = None

# Username input
if not st.session_state.username:
    st.session_state.username = st.text_input("Enter your name:", max_chars=20)

if st.session_state.username:
    st.markdown(f"<div class='player-names'>{st.session_state.username} vs Kapardhi</div>", unsafe_allow_html=True)

    # Create a 3x3 grid of buttons
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            if cols[j].button(st.session_state.board[i][j], key=f"button_{i}_{j}", 
                              disabled=st.session_state.game_over or st.session_state.board[i][j] != ' '):
                st.session_state.board[i][j] = 'O'
                
                # Check if human wins
                if evaluate(st.session_state.board) == -10:
                    st.session_state.result = "O"
                    st.session_state.game_over = True
                elif not is_moves_left(st.session_state.board):
                    st.session_state.result = "Draw"
                    st.session_state.game_over = True
                else:
                    # AI's move
                    move = find_best_move(st.session_state.board)
                    st.session_state.board[move[0]][move[1]] = 'X'
                    
                    # Check if AI wins
                    if evaluate(st.session_state.board) == 10:
                        st.session_state.result = "X"
                        st.session_state.game_over = True
                    elif not is_moves_left(st.session_state.board):
                        st.session_state.result = "Draw"
                        st.session_state.game_over = True
                
                st.experimental_rerun()

    # Display game result
    if st.session_state.game_over:
        if st.session_state.result == "O":
            st.markdown(f'<div class="game-over result-o">{st.session_state.username} wins! Congratulations!</div>', unsafe_allow_html=True)
        elif st.session_state.result == "X":
            st.markdown('<div class="game-over result-x">Kapardhi wins! Better luck next time.</div>', unsafe_allow_html=True)
        elif st.session_state.result == "Draw":
            st.markdown('<div class="game-over result-draw">It\'s a draw!</div>', unsafe_allow_html=True)

    # Reset button
    if st.button("New Game"):
        reset_game()
        st.experimental_rerun()

    st.write(f"{st.session_state.username}, you are 'O'. Kapardhi is 'X'. Good luck!")
else:
    st.write("Please enter your name to start the game.")