1. Initial Setup

1.1 [How to setup a vite react ts project](https://developer.okta.com/blog/2022/03/14/react-vite-number-converter)

```bash
npm init vite@latest la-magia-de-tu-nombre -- --template react-ts
npm install
npm install @mui/material @emotion/react @emotion/styled
npm install @mui/icons-material

```

https://cloud.google.com/community/tutorials/deploy-react-nginx-cloud-run

docker buildx build --platform linux/amd64 -t la-magia-de-tu-nombre .

docker build --platform linux/amd64 -t la-magia-de-tu-nombre .

# docker run -p 3001:8080 la-magia-de-tu-nombre

docker tag la-magia-de-tu-nombre us-east1-docker.pkg.dev/ahueteg-project/ahueteg-registry/la-magia-de-tu-nombre

docker push us-east1-docker.pkg.dev/ahueteg-project/ahueteg-registry/la-magia-de-tu-nombre

# create a gcloud to deploy to cloud run and listen to port 80

gcloud run deploy la-magia-de-tu-nombre --image us-east1-docker.pkg.dev/ahueteg-project/ahueteg-registry/la-magia-de-tu-nombre --region us-east1 --platform managed --allow-unauthenticated --port 8080 --project 	ahueteg-project