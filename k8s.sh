#!/usr/bin/env sh

set -e

brew install --cask virtualbox
brew install --cask hyperkit

if [[ ! -f "/usr/local/bin/kubectl" ]]; then
  curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl
  chmod +x ./kubectl
  mv ./kubectl /usr/local/bin/kubectl
fi


brew install minikube
brew install helm