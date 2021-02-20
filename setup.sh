#!/bin/bash
if [[ -z "${FLASK_APP}" ]]; then
	export FLASK_APP=helloFlask.py
fi
flask run
