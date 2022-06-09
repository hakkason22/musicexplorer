FROM node:16.13.2-alpine
ENV HOST 0.0.0.0
CMD ["sh", "-c", "npm install && npm run dev"]
EXPOSE 3000
RUN apk update && \
    apk add git

