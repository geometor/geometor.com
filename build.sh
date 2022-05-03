#!/usr/bin/env bash

ablog clean
ablog build
echo 'geometor.com' > docs/CNAME
ablog serve

