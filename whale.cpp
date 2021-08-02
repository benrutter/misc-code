#include <iostream>
#include <vector>
#include <string>

int main() {
  // Whale, whale, whale.
  // What have we got here?
  std::string human_talk = "turpentine and turtles";
  std::vector<char> vowels = {'a', 'e', 'i', 'o', 'u'};
  std::vector<char> double_vowels = {'e', 'u'};
  std::vector<char> whale_talk;

  // whaley good translation
  for (int i = 0; i < human_talk.size(); i++) {
    for (int j = 0; j < vowels.size(); j++) {
      if (human_talk[i] == vowels[j]) {
        whale_talk.push_back(human_talk[i]);
      }
    }
    for (int j = 0; j < double_vowels.size(); j++) {
      if (human_talk[i] == vowels[j]) {
        whale_talk.push_back(human_talk[i]);
      }
    }
  }

  // whaley good output
  for (int i = 0; i < whale_talk.size(); i++) {
    std::cout << whale_talk[i];
  }
  std::cout << "\n";
}
