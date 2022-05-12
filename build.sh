#!/usr/bin/env bash
source ~/.bashrc

tools_git
ablog clean
ablog build
echo 'geometor.com' > docs/CNAME
ablog serve

