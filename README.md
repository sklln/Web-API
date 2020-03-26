# Web-API
Wrapper for python based APIs

## Testing locally
you can use Uvicorn start it up \
`pip install uvicorn`\
cd to where you main.py file is for the web app then run: \
`uvicorn main:app --reload`

## Docker
cd into project with your Dockerfile (should be outside your py package) and run \
`docker build -t sympt_new . `

Run the new image in a container (sympt_new is imageName) \
`docker run -d --name symtp_container_2 -p 80:80 imageName`

Pushing the image to some repo, this will push to Dockerhub \
`docker tag imageName YourPrivateDockerRepo/deploy_symp_v0.1:imageName` \
`docker push YourPrivateDockerRepo/deploy_symp_v0.1`

Pulling image from Dockerhub \
`docker pull YourPrivateDockerRepo/deploy_symp_v0.1:imageName`