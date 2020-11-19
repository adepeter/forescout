FROM archlinux
LABEL com.forescout.assignment.collector.version=0.0.1
ARG collector_user=forescout
ENV COLLECTOR_USER=$collector_user
ENV COLLECTOR_PATH /srv/http/$COLLECTOR_USER
ENV PIPENV_VERBOSITY=-1
RUN pacman -Syu --noconfirm base-devel \
python python-{pip,pipenv,setuptools,wheel} && \
pip install --upgrade pip setuptools wheel && \
pacman -Scc --noconfirm
RUN useradd --create-home $collector_user
USER $collector_user
COPY --chown=$COLLECTOR_USER . $COLLECTOR_PATH
WORKDIR $COLLECTOR_PATH
RUN pipenv install && \
pipenv shell && \
pip install -r requirements.txt --no-warn-script-location
CMD ["python", "manage.py", "runserver"]
EXPOSE 8000
