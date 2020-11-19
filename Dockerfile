FROM archlinux
LABEL com.forescout.assignment.collector.version=1.0
ARG collector_user=forescout
ENV COLLECTOR_USER=$collector_user
ENV COLLECTOR_PATH /srv/http/$COLLECTOR_USER
RUN pacman -Syu --noconfirm base-devel \
python python-{pip,setuptools,wheel} && \
pip install --upgrade pip setuptools wheel && \
pacman -Scc --noconfirm
RUN useradd --create-home $collector_user
USER $collector_user
COPY --chown=$COLLECTOR_USER . $COLLECTOR_PATH
WORKDIR $COLLECTOR_PATH
RUN pip install -r requirements.txt --no-warn-script-location
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]
