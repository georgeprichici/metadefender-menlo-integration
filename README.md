# MetaDefender Core - Menlo Security Middleware

## Middleware documentation
Make sure you have `python3.5` or above installed. 
This Middleware leverages python's async mechanism introduced in `python3.5`

Before you run it, install all dependencies: 
`pip install -r requirements.txt`

To run the app: 
`python3 -m metadefender_menlo`

Middleware should be configured using the [config](config.yml) file:
```
service: metadefender               # MetaDefender Core service is the only current integration allowed
api: 
  params:
    apikey: null                    # optional, but in case MetaDefender Core is configured to request it
  url: https://localhost:8008       # MetaDefender Core URL - can be HTTP or HTTPS (certificate validation is disabled)
  cert_file: /certs/server.crt      # Absolute path for the certificate -> in case you require Certification validation for MetaDefender
server: 
  port: 3000
  host: "0.0.0.0"
  api_version: /api/v1
  ```

Menlo requires all communication to be done over https, so the Middleware expects the certificates to be in the repository folder, under `certs`: 
* certfile:`certs/server.crt`
* keyfile: `certs/server.key`

The location can be altered also by modifiying `metadefender_menlo/__main__.py` at lines 22-23. 

## MetaDefender Core - Menlo Security Integration Guide

### About This Guide
This document describes the integration of Menlo Security with MetaDefender Core, using the current middleware


### Integration Overview

Menlo Security has the ability to call an external API (called Sanitization API), which allows to offload the file analysis to MetaDefender and retrieve the sanitized file once is available. 

The Sanitization API specification includes: 
* `Submit metadata` - not implemented in this Middleware to maintain a stateless system
* `Check Existing Report` - SHA256 lookup 
* `File Submission` 
* `Analysis Report` - Menlo will keep polling this endpoint until the status is completed
* `Retrieve Sanitized file`

#### Installation Prerequisites

The middleware is using `python3` and requires minimum python3.5 to run. 
A list of all libraries are included in [requirements.txt](requirements.txt)

The application can run on the same VM as MetaDefender Core or a separate system. 
Can also run in a Docker container, a [Dockerfile](Dockerfile) is made available. 

#### Integration Steps


##### Step 1: Deploy Integration Middleware

First, clone this repository: 
`git clone https://github.com/georgeprichici/metadefender-menlo-integration.git`

Second, install all dependencies: 
`pip install -r requirements.txt`

##### Step 2: Configure Middleware
Middleware should be configured using the [config](config.yml) file. 
Make sure you place the certs in the right folder (`certs`) and under the right name, since Menlo requires all communication to be done over https. 

```
service: metadefender
api: 
  params:
    apikey: null 
  url: https://localhost:8008
  cert_file: /certs/server.crt
server: 
  port: 3000
  host: "0.0.0.0"
  api_version: /api/v1
  ```
See the [Middleware Documentation](#Middleware-documentation) for details. 

##### Step 3: Configure Menlo Integration

1. Login to Menlo Admin console (`https://admin.menlosecurity.com`)
2. Go to Web Policy > Content Inspection
3. Edit `Menlo File REST API` 
4. Add the following details: 
    - Plugin Name: `MetaDefender Core`
    - Plugin Description: `MetaDefender Core API Integration`
    - Base URL: The url of the middleware (e.g. `https://1.2.3.4:3000`)
      - :warning: **HTTPS** is required!
    - Certificate: the certificate used for the Middleware 
        - This will be used for certificate validation
    - Type of transfers: 
        - Enable Downloads if MetaDefender is used to scan and sanitize downloaded files
        - Enable Uploads if MetaDefender will be used to also redact uploaded files
    - Authorization Header: you can put any dummy data, since this header will be ignored on the Middleware side
    - Hash Check: leave it unchecked, to force a file analysis and sanitization on every file download
    - Metadata Check: leave it unchecked since is not supported in this integration
    - Allow File Replacement: Enable this functionality if you plan to use MetaDefender to sanitize the downloaded files or redact uploaded files

##### Step 4: Test

1. Navigate to `https://safe.menlosecurity.com`
2. Search for a PDF
3. Try to download the PDF
4. You should see the File Download request in the Admin Console (Logs > Web Logs)
5. Click on the table entry and you'll see the analyis details on the right side. 