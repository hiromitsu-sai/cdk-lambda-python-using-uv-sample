# the image based some image on aws public container repository.
FROM public.ecr.aws/lambda/python:3.12
# installing uv https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
ENV PATH="/app/.venv/bin:$PATH"

# # installing aws cli
# RUN cat /etc/system-release \
#     && yum install -y unzip libpq-devel git \
#     && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
#     && unzip awscliv2.zip \
#     && ./aws/install \
#     && aws --version

# Set Evnvars
ENV APP_NAME=${APP_NAME:-cdk-lambda-python-using-uv-sample}
ENV LOGLEVEL=${LOGLEVEL:-DEBUG}
ENV IS_DEBUG=${IS_DEBUG:-1}
ENV PYTHONUTF8=1

# error: failed to create directory `/home/xxxxx/.cache/uv` Caused by: Read-only file system (os error 30)
#   - https://repost.aws/questions/QUyYQzTTPnRY6_2w71qscojA/read-only-file-system-aws-lambda#ANzVYu4lO8TmGfblJGL40hdg
#   - https://docs.astral.sh/uv/configuration/environment/#environment-variables
ENV UV_CACHE_DIR=/tmp/.uv_cache

# install python packages from lock file
COPY pyproject.toml uv.lock ${LAMBDA_TASK_ROOT}/
RUN uv sync --frozen

# copy the source code to the task root default=/var/task
COPY src/ ${LAMBDA_TASK_ROOT}/

# overrides the default entrypoint runs with uv
ENTRYPOINT ["uv", "run", "/lambda-entrypoint.sh"]
# CMD ["lambda_handler.handler"]
