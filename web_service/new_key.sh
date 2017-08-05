#!/usr/bin/env bash
python -c 'import random; import string; print "".join([random.SystemRandom().choice(string.digits + string.letters + "!#$%&\()*+,-./:;<=>?@[]^_{|}~" ) for i in range(100)])'
