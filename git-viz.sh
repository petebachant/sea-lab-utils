#!/bin/bash
# show simplified tree of remote branches only
git log --graph --decorate --oneline --simplify-by-decoration --remotes --decorate-refs=refs/remotes/
