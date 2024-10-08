FROM public.ecr.aws/lambda/python:3.12
# Copy function code
COPY ./app/ ${LAMBDA_TASK_ROOT}/
# Install the function's dependencies using file requirements.txt
# from your project folder.
COPY requirements.txt .
RUN pip3 install --target "${LAMBDA_TASK_ROOT}" --upgrade --no-cache-dir -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]