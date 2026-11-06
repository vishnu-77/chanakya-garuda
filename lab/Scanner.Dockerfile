FROM alpine:3.20
RUN apk add --no-cache nmap
USER 65534:65534
ENTRYPOINT ["nmap"]
