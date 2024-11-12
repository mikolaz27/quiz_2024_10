#!/bin/sh

celery -A config worker -l ${CELERY_LOG_LEVEL} -c ${CELERY_WORKERS_NUMBER}