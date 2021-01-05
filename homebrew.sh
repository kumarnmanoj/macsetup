#!/usr/bin/env sh

set -e

if [[ ! -f "/usr/local/bin/brew" ]]; then
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

brew update
brew tap neovim/homebrew-neovim
brew tap AdoptOpenJDK/openjdk

if [[ -f "brew_applications.txt" ]]; then
  cat brew_applications.txt | while read line
  do
    brew install $line
  done
fi


if [[ -f "cask_applications.txt" ]]; then
  cat cask_applications.txt | while read line
  do
    brew install --cask $line
  done
fi


