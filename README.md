### Contribution
Before start coding make sure you installed all packages and the git pre-commit hook.
In order to install git pre-commit hook run `pre-commit install`.(Make sure you do this after installing pre-commit python package)

### Celery on dev:
To run Celery worker server, make sure you set related env variables `CELERY_*` in `.source` and then:
1. Considering that you're in root of the project, cd to `src`.
2. Run `celery -A core worker -l INFO`. This should be always running while you're using it.
3. To test first go to Django shell `src/manage.py shell`.
4. `from core.celery import debug_task` and then `debug_task.delay()`
5. On server you should see the relevant logs about running the task.


### Celery Beat on dev:
Make sure that you configured Celery as mentioned above, and also make sure Celery is up and running because the tasks
are actually executed in Celery and Celery Beat is only in charge of scheduling the tasks, then:
1. Considering that you're in root of the project, cd to `src`.
2. Run `celery -A core beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`. This should be always running while you're using it.
3. You can create periodic tasks in Django Admin panel, from `Periodic Tasks` section and see the result.


### Import cities data
To use django-cities data we need to import countries and cities:
`python src/manage.py import_country_if_not_exists && python src/manage.py cities --import=city`


### Load fixtures
in `src` path:
```
manage.py loaddata company_settings
manage.py loaddata banks
manage.py loaddata services
manage.py loaddata packages
manage.py loaddata trade_locations
manage.py loaddata crontabs
manage.py loaddata periodic_tasks
manage.py loaddata service_tariffs
manage.py loaddata invoice_templates
manage.py loaddata invoice_template_items
manage.py loaddata service_tariffs_doc_cntr_detail
```
