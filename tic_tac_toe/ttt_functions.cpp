#include <iostream>
#include "ttt_functions.hpp"

std::string board[9] = {
  " ", " ", " ",
  " ", " ", " ",
  " ", " ", " "
};
int player = 1;
int position = 0;

void intro() {

  std::cout << "Tic Tac Toe!\n";
  std::cout << "You'll play best of three, on this grid:\n";
  std::cout << "1_|_2_|_3\n";
  std::cout << "4_|_5_|_6\n";
  std::cout << "7_|_8_|_9\n";

  std::cout << "\ngood luck!\n\n";

}

bool is_winner() {

  bool winner = false;
  // rows
  if ((board[0] == board[1]) && (board[1] == board[2]) && board[0] != " ") {
    winner = true;
  } else if ((board[3] == board[4]) && (board[3] == board[5]) && board[3] != " ") {
    winner = true;
  } else if ((board[6] == board[7]) && (board[6] == board[8]) && board[6] != " ") {
    winner = true;
  }
  // columns
  else if ((board[0] == board[3]) && (board[0] == board[6]) && board[0] != " ") {
    winner = true;
  } else if ((board[1] == board[4]) && (board[1] == board[7]) && board[1] != " ") {
    winner = true;
  } else if ((board[2] == board[5]) && (board[2] == board[8]) && board[2] != " ") {
    winner = true;
  }
  // diagonals
  else if ((board[0] == board[4]) && (board[0] == board[8]) && board[0] != " ") {
    winner = true;
  }
  else if ((board[2] == board[4]) && (board[2] == board[6]) && board[2] != " ") {
    winner = true;
  }

  return winner;

}

bool filled_up() {

  bool filled = true;

  for (int i = 0; i < 9; i++) {
    if (board[i] == " ") {
      filled = false;
    }
  }

  return filled;

}

void print_board() {

  std::cout << "_" << board[0] << "_|_" << board[1] << "_|_" << board[2] << "\n";
  std::cout << "_" << board[3] << "_|_" << board[4] << "_|_" << board[5] << "\n";
  std::cout << "_" << board[6] << "_|_" << board[7] << "_|_" << board[8] << "\n";
  std::cout << "\n";

}

void set_position() {

  std::cout << player << ", enter your move (1-9): ";

  while (!(std::cin >> position)) {
    std::cout << player << ", enter your move (1-9): ";
    std::cin.clear();
    std::cin.ignore();
  }

  std::cout << "\n";

  while (board[position-1] != " ") {
    std::cout << "Invalid move!\n\n";
    std::cout << player << ", enter your move (1-9): ";
    std::cin >> position;
    std::cout << "\n";
  }
}

void update_board() {
  if (player % 2 == 1) {
    board[position-1] = "✖";
  } else {
    board[position-1] = "⊙";
  }
}

void change_player() {
  if (player == 1) {
    player = 2;
  } else {
    player = 1;
  }
}

void take_turn() {

  while ( !is_winner() && !filled_up() ) {
    set_position();
    update_board();
    change_player();
    print_board();
  }

}

void end_game() {

  if (is_winner()) {
    std::cout << "There's a winner!\n";
  }
  else if (filled_up()) {
    std::cout << "There's a tie!\n";
  }

}
