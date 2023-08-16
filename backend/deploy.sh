

(cd $BACKEND_HOME && \
docker build -t la-magia-de-tu-nombre-backend . --platform linux/amd64)

(cd $BACKEND_HOME && \
PORT=8080 && \
docker run -p 8080:${PORT} \
-e PORT=${PORT} \
la-magia-de-tu-nombre-backend
)


docker tag la-magia-de-tu-nombre-backend us-east1-docker.pkg.dev/ahueteg-project/ahueteg-registry/la-magia-de-tu-nombre-backend

docker push us-east1-docker.pkg.dev/ahueteg-project/ahueteg-registry/la-magia-de-tu-nombre-backend

gcloud run deploy la-magia-de-tu-nombre-backend --image us-east1-docker.pkg.dev/ahueteg-project/ahueteg-registry/la-magia-de-tu-nombre-backend \
 --region us-east1 --platform managed --allow-unauthenticated --port 8080 --project 	ahueteg-project