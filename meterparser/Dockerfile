ARG BUILD_FROM
# Build arguments
ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_DESCRIPTION
ARG BUILD_NAME
ARG BUILD_REF
ARG BUILD_REPOSITORY
ARG BUILD_VERSION

# hadolint ignore=DL3006
FROM ${BUILD_FROM}

# Copy root filesystem

RUN apt-get clean \
    && apt-get update \
    # apt-get install -y --no-install-recommends gnupg2 
    # curl -s https://notesalexp.org/debian/alexp_key.asc | gpg --dearmor > /usr/share/keyrings/tesseract-archive-keyring.gpg 
    # echo "deb [signed-by=/usr/share/keyrings/tesseract-archive-keyring.gpg] https://notesalexp.org/tesseract-ocr5/bullseye/ bullseye main" >> /etc/apt/sources.list.d/tesseract.list 
    && apt-get install -y build-essential autoconf libtool pkg-config python3-full python3-pip python3-dev cmake git wget curl unzip \
    && apt-get install -y --no-install-recommends ffmpeg \
    && rm -fr /tmp/* /var/{cache,log}/* /var/lib/apt/lists/* 
    # tesseract-ocr 

COPY rootfs /
COPY src/requirements.txt /tmp

RUN pip3 install --no-cache-dir -r /tmp/requirements.txt \
    && rm -fr /tmp/* /var/{cache,log}/* /var/lib/apt/lists/* 

COPY src /src

# Labels
LABEL \
    io.hass.name="${BUILD_NAME}" \
    io.hass.description="${BUILD_DESCRIPTION}" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="Marcos Junior <junalmeida@gmail.com>" \
    org.opencontainers.image.title="${BUILD_NAME}" \
    org.opencontainers.image.description="${BUILD_DESCRIPTION}" \
    org.opencontainers.image.vendor="Marcos Junior" \
    org.opencontainers.image.authors="Marcos Junior <junalmeida@gmail.com>" \
    org.opencontainers.image.licenses="MIT" \
    org.opencontainers.image.url="https://github.com/${BUILD_REPOSITORY}" \
    org.opencontainers.image.source="https://github.com/${BUILD_REPOSITORY}" \
    org.opencontainers.image.documentation="https://github.com/${BUILD_REPOSITORY}/blob/main/README.md" \
    org.opencontainers.image.created=${BUILD_DATE} \
    org.opencontainers.image.revision=${BUILD_REF} \
    org.opencontainers.image.version=${BUILD_VERSION}
